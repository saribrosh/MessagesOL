import FeaturesEnd

def main():

    # case 1: (3/3) ...
    # expectation: true
    text = '(3/3) I don\'t know'
    result = FeaturesEnd.serial_number(text)
    if (result > 0):
        print 'case 1: pass - pattern (x/x)'
    else:
        print 'case 1: failed - pattern (x/x)'

    # case 2: x/x---OL ...
    # expectation: true
    text = '4/4---OL---Hi my nameie doris'
    result = FeaturesEnd.serial_number(text)
    if (result > 0):
        print 'case 2: pass - pattern x/x---OLy'
    else:
        print 'case 2: failed - pattern x/y---OL'

    # case 3: some text (3/3) ...
    # expectation: false
    text = 'this is page (3/3) I think'
    result = FeaturesEnd.serial_number(text)
    if (result == 0):
        print 'case 3: pass - pattern (x/x) in middle of text'
    else:
        print 'case 3: failed - pattern (x/x) in middle of text'

    # case 4: (x/y)..., | x<y
    # expectation: false
    text = '(1/5) some text'
    result = FeaturesEnd.serial_number(text)
    if (result == 0):
        print 'case 4: pass - pattern serial number is not last'
    else:
        print 'case 4: failed - pattern serial number is not last'

    # test
    text = '(1/4) A manager did not come ask me anything about my son! You\'re right, you didn\'t hear from me because I was so mad that the owner did not have the decency to'
    result = FeaturesEnd.serial_number(text)
    if (result == 0):
        print 'test: pass'
    else:
        print 'test: failed'

if __name__ == "__main__":
    main()