from nltk.corpus import webtext, nps_chat, twitter_samples
from nltk import word_tokenize
import csv
import unicodedata

def create_owner_listens_resource(messages_list):
    resource = []
    resource_relevant_codes = ['6', '8', '12', '13', '19']
    for message in messages_list:
        if message[4] in resource_relevant_codes:
            text = (message[5]).decode('unicode-escape')
            print text
            tokenized_sentence = (word_tokenize(text))
            ascii_sentence = []
            for token in tokenized_sentence:
                ascii_token = unicodedata.normalize('NFKD', token).encode('ascii','ignore')
                if ascii_token:
                    ascii_sentence.append(ascii_token)
            if ascii_sentence and ((ascii_sentence) > 1 or ascii_sentence[0]):
                resource.append(ascii_sentence)

    return resource

def remove_speaker_or_reference(sentence, max_index):
    if ":" in sentence:
        colon_index = sentence.index(":")
    else:
        return sentence
    if (colon_index < max_index):
        return sentence[colon_index+1:]
    else:
        return sentence

def create_webtext_resource():
    resource = []
    raw = webtext.raw()
    sentences = raw.splitlines()
    for item in sentences:
        tokenized_sentence = word_tokenize(item)
        tokenized_sentence = remove_speaker_or_reference(tokenized_sentence, 5)
        if tokenized_sentence:
            ascii_sentence = []
            for token in tokenized_sentence:
                ascii_token = unicodedata.normalize('NFKD', token).encode('ascii','ignore')
                if ascii_token:
                    ascii_sentence.append(ascii_token)
            if len(ascii_sentence) > 0:
                resource.append(ascii_sentence)
    return resource

def create_nps_chat_resource():
    resource = []
    irrelevant_data = ['PART', 'JOIN']
    posts = nps_chat.posts()
    sentences = list(posts)
    for sen in sentences:
        if sen[0] not in irrelevant_data or len(sen) > 1:
            ascii_sentence = []
            for token in sen:
                ascii_token = unicodedata.normalize('NFKD', token).encode('ascii','ignore')
                if ascii_token:
                    ascii_sentence.append(ascii_token)
            if len(ascii_sentence) > 0:
                resource.append(ascii_sentence)
    return resource

def remove_retweet_data(sentence):
    rt_tokens = ['RT', ':', '.']
    tag_chars = ['@', '#']
    potential_metadata_ids = []
    for i in range(0,len(sentence)):
        if sentence[i] in rt_tokens:
            potential_metadata_ids.append(i)
        if (sentence[i])[0] in tag_chars:
            potential_metadata_ids.append(i)

    if ((not potential_metadata_ids) or (0 not in potential_metadata_ids)):
        return sentence

    start_from = 0
    list_length = len(potential_metadata_ids)
    for i in range(0,list_length-1):
        if potential_metadata_ids[i]+1 == potential_metadata_ids[i+1]:
            start_from = start_from+1
        else:
            start_from = potential_metadata_ids[i]
            break
    return sentence[(start_from+1):]

def create_twitter_resource():
    resource = []
    original_sentences = twitter_samples.tokenized()
    for sentence in original_sentences:
        sentence_content = remove_retweet_data(sentence)
        sentence_content = remove_speaker_or_reference(sentence_content, 3)
        if len(sentence_content) > 0:
            ascii_sentence = []
            for token in sentence_content:
                ascii_token = unicodedata.normalize('NFKD', token).encode('ascii','ignore')
                if ascii_token:
                    ascii_sentence.append(ascii_token)
            if len(ascii_sentence) > 0:
                resource.append(ascii_sentence)
    return resource

def create_resource_csv(resource):
    with open("resource.csv", "wb") as f:
        writer = csv.writer(f)
        for row in resource:
            row = ['<begin>'] + row + ['<end>']
            writer.writerow(row)