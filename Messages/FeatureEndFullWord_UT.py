import FeaturesEnd

def main():

    # real word
    sentence = "I want to go home"
    is_known_last_token = FeaturesEnd.full_word_indication(sentence)
    if is_known_last_token > 0:
        print 'pass: last token is a known full word'
    else:
        print 'failed: last token is a known full word'

    # non word
    sentence = "you want to go hom"
    is_known_last_token = FeaturesEnd.full_word_indication(sentence)
    if is_known_last_token == 0:
        print 'pass: last token is not a known full word'
    else:
        print 'failed: last token is not a known full word'

    # contraction
    sentence = "you should go, but I can't"
    is_known_last_token = FeaturesEnd.full_word_indication(sentence)
    if is_known_last_token > 0:
        print 'pass: last token is a known contraction'
    else:
        print 'failed: last token is a known contraction'

    # emoticon
    sentence = "you should go, but I can't :)"
    is_known_last_token = FeaturesEnd.full_word_indication(sentence)
    if is_known_last_token > 0:
        print 'pass: last token is an emoticon'
    else:
        print 'failed: last token is an emoticon'

    # punctuation
    sentence = "you should go, but I can't,"
    is_known_last_token = FeaturesEnd.full_word_indication(sentence)
    if is_known_last_token == 0:
        print 'pass: last token is a punctuation mark'
    else:
        print 'failed: last token is a punctuation mark'

    # test
    sentence = "you to feel comfortable. I am P"
    is_known_last_token = FeaturesEnd.full_word_indication(sentence)
    if is_known_last_token == 0:
        print 'pass: temp test'
    else:
        print 'failed: temp test'



if __name__ == "__main__":
    main()