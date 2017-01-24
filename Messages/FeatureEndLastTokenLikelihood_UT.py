import FeaturesEndSegmentLevel

def main():

    # expected results is (frequency as last / frequency as not last)
    # last token is capitalized
    sentence = "I want to go HOME"
    ratio = FeaturesEndSegmentLevel.last_token_likelihood(sentence)
    if ratio == 20*(float(9)/float(365-9)):
        print 'pass: capitalized'
    else:
        print 'failed: capitalized'

    # lowercase first token
    sentence = "you want to go there"
    ratio = FeaturesEndSegmentLevel.last_token_likelihood(sentence)
    if ratio == 20*(float(83)/float(2698-83)):
        print 'pass: lowercase'
    else:
        print 'failed: lowercase'

    # test
    # sentence = "Was there anything else I could help with?"
    # ratio = FeaturesBeginning.first_token_likelihood(sentence)
    # if ratio == 20*(float(857)/float(17878-857)):
    #     print 'pass: was'
    # else:
    #     print 'failed: was'

if __name__ == "__main__":
    main()