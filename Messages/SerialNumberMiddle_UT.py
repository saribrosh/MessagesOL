import FeaturesMiddleSegmentLevel

def main():

    # case 1: (2/3) ...
    # expectation: true
    text = '(2/3) I don\'t know'
    result = FeaturesMiddleSegmentLevel.serial_number(text)
    if (result > 0):
        print 'case 1: pass - pattern (2/x)'
    else:
        print 'case 1: failed - pattern (2/x)'

    # case 2: 2/x---OL ...
    # expectation: true
    text = '4/6---OL---Hi my nameie doris'
    result = FeaturesMiddleSegmentLevel.serial_number(text)
    if (result > 0):
        print 'case 2: pass - pattern x/y---OL | x<y'
    else:
        print 'case 2: failed - pattern x/y---OL | x<y'

    # case 3: some text (2/3) ...
    # expectation: false
    text = 'this is page (2/3) I think'
    result = FeaturesMiddleSegmentLevel.serial_number(text)
    if (result == 0):
        print 'case 3: pass - pattern (2/x) in middle of text'
    else:
        print 'case 3: failed - pattern (2/x) in middle of text'

    # case 4: (x/y)..., | x=1
    # expectation: false
    text = '(1/5) some text'
    result = FeaturesMiddleSegmentLevel.serial_number(text)
    if (result == 0):
        print 'case 4: pass - pattern serial number is 1'
    else:
        print 'case 4: failed - pattern serial number is 1'

    # case 5: last part of a serial number
    # expectation: false
    text = '(5/5) some text'
    result = FeaturesMiddleSegmentLevel.serial_number(text)
    if (result == 0):
        print 'case 5: pass - pattern serial number is the last'
    else:
        print 'case 5: failed - pattern serial number is the last'

if __name__ == "__main__":
    main()