import nltk
import enchant
import re

PARTIAL_WORDS_SCORE = 5
MIDDLE_IN_SERIAL = 10

middle_serial = []

def cut_from_both_sides(segment):
    tokenized = nltk.word_tokenize(segment)
    first_token = (tokenized[0]).lower()
    last_token = (tokenized[-1]).lower()
    d = enchant.Dict("en_US")
    if first_token.isalpha() and last_token.isalpha() and \
            not d.check(first_token)and not d.check(last_token):
        return PARTIAL_WORDS_SCORE
    else:
        return 0

def serial_number(key, segment):
    global beginning_serial
    pattern = re.compile(r"(\(([2-9])\/([0-9])\))|(([2-9])\/([0-9])\-\-\-OL)")
    serial_found = re.match(pattern, segment)
    if serial_found:
        if serial_found.group(2):
            serial = int(serial_found.group(2))
        elif serial_found.group(5):
            serial = int(serial_found.group(5))
        if serial_found.group(3):
            total = int(serial_found.group(3))
        elif serial_found.group(6):
            total = int(serial_found.group(6))
        if serial < total:
            middle_serial.append(key)
            return MIDDLE_IN_SERIAL
        else:
            return 0
    return 0

def calculate_segment_level_middle_score(key, text):
    score = cut_from_both_sides(text) + \
            serial_number(key, text)
    return score