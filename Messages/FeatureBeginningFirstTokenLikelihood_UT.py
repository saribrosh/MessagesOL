import FeaturesBeginning

def main():

    # expected results is (frequency as first / frequency as not first)
    # first token is capitalized
    sentence = "I want to go home"
    ratio = FeaturesBeginning.first_token_likelihood(sentence)
    if ratio == 20*(float(5497)/float(26268-5497)):
        print 'pass: I'
    else:
        print 'failed: I'

    # lowercase first token
    sentence = "you want to go home"
    ratio = FeaturesBeginning.first_token_likelihood(sentence)
    if ratio == 20*(float(857)/float(17878-857)):
        print 'pass: you'
    else:
        print 'failed: you'

    # test
    # sentence = "Was there anything else I could help with?"
    # ratio = FeaturesBeginning.first_token_likelihood(sentence)
    # if ratio == 20*(float(857)/float(17878-857)):
    #     print 'pass: was'
    # else:
    #     print 'failed: was'

if __name__ == "__main__":
    main()