import FeaturesEnd

def main():

    # last token is predefined as unlikely to be last
    sentence = "I want to go home but"
    res = FeaturesEnd.unlikely_last_token_penalty(sentence)
    if res < 0:
        print 'pass: unlikely last token'
    else:
        print 'failed: unlikely last token'

    # last token is not predefined as unlikely to be last
    sentence = "I want to go home"
    res = FeaturesEnd.unlikely_last_token_penalty(sentence)
    if res == 0:
        print 'pass: regular last token'
    else:
        print 'failed: regular last token'

    # last token is a right bracket that's part of an emoticon
    sentence = "I want to go home :("
    res = FeaturesEnd.unlikely_last_token_penalty(sentence)
    if res == 0:
        print 'pass: right bracket as part of emoticon'
    else:
        print 'failed: right bracket as part of emoticon'

    # last token is a right bracket that's not part of an emoticon
    sentence = "I want to go home ["
    res = FeaturesEnd.unlikely_last_token_penalty(sentence)
    if res < 0:
        print 'pass: right bracket'
    else:
        print 'failed: right bracket'

    # test
    # sentence = "Was there anything else I could help with?"
    # ratio = FeaturesBeginning.first_token_likelihood(sentence)
    # if ratio == 20*(float(857)/float(17878-857)):
    #     print 'pass: was'
    # else:
    #     print 'failed: was'

if __name__ == "__main__":
    main()