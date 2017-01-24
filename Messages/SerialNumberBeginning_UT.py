import FeaturesBeginningSegmentLevel

def main():

    # case 1: (1/3) ...
    # expectation: true
    text = '(1/3) I don\'t know'
    result = FeaturesBeginningSegmentLevel.serial_number(text)
    if (result > 0):
        print 'case 1: pass - pattern (1/x)'
    else:
        print 'case 1: failed - pattern (1/x)'

    # case 2: 1/2---OL ...
    # expectation: true
    text = '1/2---OL---Hi my nameie doris'
    result = FeaturesBeginningSegmentLevel.serial_number(text)
    if (result > 0):
        print 'case 2: pass - pattern 1/x---OL'
    else:
        print 'case 2: failed - pattern 1/x---OL'

    # case 3: some text (1/3) ...
    # expectation: false
    text = 'this is page (1/3) I think'
    result = FeaturesBeginningSegmentLevel.serial_number(text)
    if (result == 0):
        print 'case 3: pass - pattern (1/x) in middle of text'
    else:
        print 'case 3: failed - pattern (1/x) in middle of text'

    # case 4: (x/y)..., | x !=1
    # expectation: false
    text = '(2/5) some text'
    result = FeaturesBeginningSegmentLevel.serial_number(text)
    if (result == 0):
        print 'case 4: pass - pattern serial number but not 1'
    else:
        print 'case 4: failed - pattern serial number but not 1'

if __name__ == "__main__":
    main()