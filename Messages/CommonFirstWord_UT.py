import FeaturesBeginningSegmentLevel

def main():

    # first token in lexicon
    sentence = "Were you at the bar last night"
    result = FeaturesBeginningSegmentLevel.common_first_word(sentence)
    if result == FeaturesBeginningSegmentLevel.COMMON_FIRST_TOKEN_SCORE:
        print 'pass: word in lexicon'
    else:
        print 'failed: word in lexicon'

    # first token not in lexicon
    sentence = "you want to go home"
    result = FeaturesBeginningSegmentLevel.common_first_word(sentence)
    if result == FeaturesBeginningSegmentLevel.COMMON_FIRST_TOKEN_SCORE:
        print 'failed: word not in lexicon'
    else:
        print 'pass: word not in lexicon'

    # test
    # sentence = "Was there anything else I could help with?"
    # ratio = FeaturesBeginning.first_token_likelihood(sentence)
    # if ratio == 20*(float(857)/float(17878-857)):
    #     print 'pass: was'
    # else:
    #     print 'failed: was'

if __name__ == "__main__":
    main()