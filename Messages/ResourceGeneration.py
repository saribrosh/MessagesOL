from nltk.corpus import webtext, nps_chat, twitter_samples
from nltk import word_tokenize
import re
import unicodedata
import TwitterResourceCleaning
import InputCleaning
from operator import itemgetter


def create_owner_listens_resource(messages_list):
    resource = ''
    resource_relevant_codes = ['6', '8', '12', '13', '19']
    for message in messages_list:
        if message[4] in resource_relevant_codes:
            text = message[5]
            utext = text.decode("utf-8")
            text = utext.encode("ascii","ignore")
            text = InputCleaning.generalize_URLs(text)
            text = 'BEGINMARK ' + text + ' ENDMARK '
        resource = resource + text
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
    resource = ''
    irrelevant_data = ['PART', 'JOIN']
    posts = nps_chat.posts()
    sentences = list(posts)
    for sen in sentences:
        text = ''
        if sen[0] not in irrelevant_data or len(sen) > 1:
            ascii_sentence = []
            for token in sen:
                ascii_token = unicodedata.normalize('NFKD', token).encode('ascii','ignore')
                if ascii_token:
                    ascii_sentence.append(ascii_token)
            if len(ascii_sentence) > 0:
                for valid_token in ascii_sentence:
                    text = text + valid_token + ' '
                text = 'BEGINMARK ' + text + ' ENDMARK '
        resource = resource + text
    return resource

def create_twitter_resource():
    resource = ''
    tweets_list = []
    tweets = sorted(list(twitter_samples.strings()))
    for tweet in tweets:
        # print '1: ', tweet
        tweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
        # print '2: ', tweet
        tweet = InputCleaning.generalize_URLs(tweet)
        # print '3: ', tweet
        tweet = TwitterResourceCleaning.mark_cut_content(tweet)
        # print '4: ', tweet
        tweet = InputCleaning.white_space_replacements(tweet)
        tweets_list.append(tweet)

    unique_tweets_indices = []
    unique_tweets_indices.append(0)
    for i in range(0,len(tweets_list)-1):
        is_duplicate = TwitterResourceCleaning.calculate_string_differences(tweets_list[i], tweets_list[i+1])
        if is_duplicate == False:
            unique_tweets_indices.append(i+1)

    no_dup_tweets = itemgetter(*unique_tweets_indices)(tweets_list)

    for tweet in no_dup_tweets:
        tweet = TwitterResourceCleaning.remove_retweet_data(tweet)
        tweet = TwitterResourceCleaning.remove_tags_from_ending(tweet)
        marked_tweet = 'BEGINMARK ' + tweet + ' ENDMARK '
        resource = resource + marked_tweet
    return resource


def create_resource_csv(resource):
    with open("resource.txt", "w") as text_file:
        resource = re.sub('\n', ' ',resource)
        resource = re.sub('\r', ' ',resource)
        resource = re.sub('  ', ' ', resource)
        text_file.write(resource)