import nltk
import enchant
import csv

EOS_PUNCT_SCORE = 4
FACTOR = 22
FULL_WORD_SCORE = 2
UNCOMMON_LAST_TOKEN_SCORE = -2.5


def EOSPunctuation(segment):
    EOS_punctuation_list = [".", "?", "!", "..."]

    tokenized = nltk.word_tokenize(segment)
    last_token = tokenized[-1]
    if last_token in EOS_punctuation_list:
        return EOS_PUNCT_SCORE
    else:
        return 0

def full_word_indication(segment):
    legal_contractions_list = ["n\'t", "\'s"]
    emoticons_list = [":-)", ":)", ":-]", ":]", ":o)", "=]", "=)", ":-D", ":D", "XD",
                      ":-(", ":(", ":-[", ":[", ":-o", ":-O", ":o", ":-O", ":-*", ":*",
                      ";-)", ";)", ":-P", ":P", ":-p", ":p", ":-\\", ":\\", "=\\", ":s",
                      ":S", ":/", ":-/", ":-|", ":|", "O_O", "O_o", "o_O", "o_o", "^_^"]
    known_single_char_words_list = ['i']
    tokenized = nltk.word_tokenize(segment)
    last_token = (tokenized[-1]).lower()
    d = enchant.Dict("en_US")
    if (len(last_token) > 1):
        if d.check(last_token) or last_token in legal_contractions_list:
            return FULL_WORD_SCORE
    elif d.check(last_token) and last_token in known_single_char_words_list:
        return FULL_WORD_SCORE
    else:
        segment_as_list = segment.split(" ")
        if segment_as_list[-1] in emoticons_list:
            return FULL_WORD_SCORE

    return 0

def last_token_likelihood(segment):
    tokenized = nltk.word_tokenize(segment)
    last_token = (tokenized[-1]).lower()

    token_total_count = 0
    token_count_as_last = 0

    with open('unigram_count.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for unigram in reader:
            if (unigram[0]) == last_token:
                token_total_count = int(unigram[1])
                break

    with open('last_tokens_dict.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for token in reader:
            if (token[0]) == last_token:
                token_count_as_last = int(token[1])
                break

    diff = (token_total_count - token_count_as_last)
    if (diff == 0):
        return 0

    ratio = float(token_count_as_last) / float(diff)
    return ratio*FACTOR

def unlikely_last_token_penalty(segment):
    unlikely_last_tokens_list = ['but', 'and', ',']
    unlikely_non_emoticon_last_chars = ["(", "[", "<"]
    tokenized = nltk.word_tokenize(segment)
    last_token = (tokenized[-1]).lower()
    if last_token in unlikely_last_tokens_list:
        return UNCOMMON_LAST_TOKEN_SCORE
    else:
        segment_as_list = segment.split(" ")
        if segment_as_list[-1] in unlikely_non_emoticon_last_chars:
            return UNCOMMON_LAST_TOKEN_SCORE

    return 0

