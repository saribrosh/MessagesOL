import FeaturesBeginningSegmentLevel

def main():

    # real word
    sentence = "I want to go home"
    is_known_first_token = FeaturesBeginningSegmentLevel.full_word_indication(sentence)
    if is_known_first_token:
        print 'pass: I'
    else:
        print 'failed: I'

    # non word
    sentence = "yout want to go home"
    is_known_first_token = FeaturesBeginningSegmentLevel.full_word_indication(sentence)
    if not is_known_first_token:
        print 'pass: yout'
    else:
        print 'failed: yout'


if __name__ == "__main__":
    main()