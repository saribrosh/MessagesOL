import FeaturesBeginningSegmentLevel

def main():
    # 1. first token is proper noun: expected score 0
    res = FeaturesBeginningSegmentLevel.capitalization("Michael Jackson likes to eat at McDonalds")
    if res == 0:
        print "pass: 1- proper noun"
    else:
        print "failed: 1 - proper noun"

    # 2. first token is "I" <or other predefined tokens>: expected score 0
    res = FeaturesBeginningSegmentLevel.capitalization("I like to eat at McDonalds")
    if res == 0:
        print "pass: 2 - known capitalized token"
    else:
        print "failed: 2 - known capitalized token"

    # 3. first token is all caps: expected score 0
    res = FeaturesBeginningSegmentLevel.capitalization("NBA players are tall")
    if res == 0:
        print "pass: 3 - all caps"
    else:
        print "failed: 3 - all caps"

    # 4. first token not capitalized: expected score 0
    res = FeaturesBeginningSegmentLevel.capitalization("all players are tall")
    if res == 0:
        print "pass: 4 - lowercase"
    else:
        print "failed: 4 - lowercase"

    # 5. first token capitalized: expected score > 0
    res = FeaturesBeginningSegmentLevel.capitalization("This is correct")
    if res > 0:
        print "pass: 5 - capitalization feature"
    else:
        print "failed: 5 - capitalization feature"

    # 6. test
    # res = FeaturesBeginning.capitalization("Was there anything else I could help with?")
    # if res > 0:
    #     print "pass: 6 - capitalization feature"
    # else:
    #     print "failed: 6 - capitalization feature"

if __name__ == "__main__":
    main()