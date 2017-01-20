import FeaturesEnd

def main():
    # 1. last token is EOS punctuation: expected score > 0
    res = FeaturesEnd.EOSPunctuation("Michael Jackson likes to eat at McDonalds.")
    if res == 0:
        print "failed: 1 - input ends with full stop"
    else:
        print "pass: 1 - input ends with full stop"

    # 2. last token is an alphabet token: expected score = 0
    res = FeaturesEnd.EOSPunctuation("I like to eat at McDonalds")
    if res == 0:
        print "pass: 2 - input ends with an alphabet token"
    else:
        print "failed: 2 - input ends with an alphabet token"

    # 3. last token is non EOS punctuation: expected score = 0
    res = FeaturesEnd.EOSPunctuation("NBA players are tall,")
    if res == 0:
        print "pass: 3 - input ends with non EOS punctuation"
    else:
        print "failed: 3 - input ends with non EOS punctuation"

    # 4. last token is an emoticon: expected score = 0
    res = FeaturesEnd.EOSPunctuation("NBA players are tall :)")
    if res == 0:
        print "pass: 3 - input ends with emoticon"
    else:
        print "failed: 3 - input ends with emoticon"

    # 5. last token is multi-character EOS punctuation: expected score > 0
    res = FeaturesEnd.EOSPunctuation("Michael Jackson likes to eat at McDonalds?!")
    if res == 0:
        print "failed: 1 - input ends with multi-character EOS punctuation"
    else:
        print "pass: 1 - input ends with multi-character EOS punctuation"

if __name__ == "__main__":
    main()