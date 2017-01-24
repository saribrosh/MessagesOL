import FeaturesMiddleSegmentLevel

def main():

    # cut from both sides
    sentence = "nt to go hom"
    is_cut_ind = FeaturesMiddleSegmentLevel.is_correct_middle_in_group(sentence)
    if is_cut_ind > 0:
        print 'pass: cut'
    else:
        print 'failed: cut'

    # cut from one side
    sentence = "want to go hom"
    is_cut_ind = FeaturesMiddleSegmentLevel.is_correct_middle_in_group(sentence)
    if is_cut_ind == 0:
        print 'pass: not cut'
    else:
        print 'failed: not cut'

    # not cut
    sentence = "want to go home"
    is_cut_ind = FeaturesMiddleSegmentLevel.is_correct_middle_in_group(sentence)
    if is_cut_ind == 0:
        print 'pass: not cut'
    else:
        print 'failed: not cut'

if __name__ == "__main__":
    main()