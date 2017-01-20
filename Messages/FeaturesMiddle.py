import nltk
import enchant

PARTIAL_WORDS_SCORE = 5

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
