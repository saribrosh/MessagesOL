from nltk.tag import pos_tag
import nltk
import csv
import enchant
import re

CAP_SCORE = 5
FACTOR = 20
FULL_WORD_SCORE = 2
COMMON_FIRST_TOKEN_SCORE = 2.5
FIRST_IN_SERIAL = 10


def capitalization(segment):
    seg = nltk.word_tokenize(segment)
    proper_nouns_pos_tags = ['NNP', 'NNPS']
    tagged_segment = pos_tag(seg)
    first_token = seg[0]
    first_char = (seg[0])[0]

    # proper noun
    if tagged_segment[0][1] in proper_nouns_pos_tags:
        return 0

    # all caps <includes 'I' case>
    if first_token.isupper():
        return 0

    # lowercase
    if first_char.islower():
        return 0

    return CAP_SCORE


def first_token_likelihood(segment):
    tokenized = nltk.word_tokenize(segment)
    first_token = (tokenized[0]).lower()

    token_total_count = 0
    token_count_as_first = 0

    with open('unigram_count.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for unigram in reader:
            if (unigram[0]) == first_token:
                token_total_count = int(unigram[1])
                break

    with open('first_tokens_dict.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for token in reader:
            if (token[0]) == first_token:
                token_count_as_first = int(token[1])
                break

    diff = (token_total_count - token_count_as_first)
    if (diff == 0):
        return 0

    ratio = float(token_count_as_first) / float(diff)
    return ratio*FACTOR

def full_word_indication(segment):
    segment = nltk.word_tokenize(segment)
    first_token = (segment[0]).lower()
    d = enchant.Dict("en_US")
    if d.check(first_token):
        return FULL_WORD_SCORE
    else:
        return 0

def common_first_word(segment):
    wh_question_words = ['who', 'what', 'where', 'why', 'when', 'how', 'whose', 'whom', 'which']
    aux_words = ['am', 'is', 'are', 'was', 'were', 'had', 'have', 'has', 'do', 'does', 'did', 'could', 'would', 'should', 'will']
    greetings = ['hi', 'hello', 'thank', 'hey', 'thanks']
    common_first_words_list = wh_question_words + aux_words + greetings
    segment = nltk.word_tokenize(segment)
    first_token = (segment[0]).lower()
    if first_token in common_first_words_list:
        return COMMON_FIRST_TOKEN_SCORE
    else:
        return 0

def serial_number(segment):
    pattern = re.compile(r"\((1\/[0-9]\))|(1\/[0-9]\-\-\-OL)")
    serial_found = re.match(pattern, segment)
    if serial_found:
        return FIRST_IN_SERIAL
    else:
        return 0
