import TwitterResourceCleaning

def main():

    # case 1: tweet is not cut
    # expectation: no CUTMARK marker is added to returned tweet
    tweet = 'how am i gonna watch eu lcs in 6 hours :( help i need more sleep'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'how am i gonna watch eu lcs in 6 hours :( help i need more sleep'
    if (result == expected):
        print 'case 1: pass - full tweet'
    else:
        print 'case 1: failed - full tweet'
        print result

    # case 2: tweet ends with a full word followed by  ' ...', tweet is of maximum length
    # expectation: tweet is returned as is, ellipsis from the end is removed and replaced by '<cut>' marker
    tweet = 'The #SNP are the #TartanTories who put Thatcher in no.10 for 18yrs out of revenge for the 40% rule bla bla bla bla bla bla bla bla bla b ...'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'The #SNP are the #TartanTories who put Thatcher in no.10 for 18yrs out of revenge for the 40% rule bla bla bla bla bla bla bla bla bla b CUTMARK'
    if (result == expected):
        print 'case 2: pass - maximum length, ends with ellipsis'
    else:
        print 'case 2: failed - maximum length, ends with ellipsis'
        print result

    # case 3: tweet ends with a full word followed by  ' ...', tweet is not of maximum length
    # expectation: tweet is returned as is, including ellipsis, no '<cut>' marker is added
    tweet = 'Meanwhile, back in the real world ...'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'Meanwhile, back in the real world ...'
    if (result == expected):
        print 'case 3: pass - not maximum length, ends with ellipsis'
    else:
        print 'case 3: failed - not maximum length, ends with ellipsis'
        print result

    # case 4: tweet ends with ' ...', tweet is of maximum length, contains ellipsis in middle too
    # expectation: tweet is returned as is, last ellipsis replaced by '<cut>', middle ellipsis not replaced or removed
    tweet = 'Meanwhile, back in the real world ... be apologise for coalition says Lib Dem big leader Nick Clegg has defended his decision to go into ...'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'Meanwhile, back in the real world ... be apologise for coalition says Lib Dem big leader Nick Clegg has defended his decision to go into CUTMARK'
    if (result == expected):
        print 'case 4: pass - maximum length, elipsis in middle and end'
    else:
        print 'case 4: failed - maximum length, elipsis in middle and end'
        print result

    # case 5: tweet ends with a cut word followed by '...'
    # expectation: both last ellipsis and cut word are removed and replaced by '<cut>' marker
    tweet = 'VIDEO: UKIP would accept the EU vote result URLGEN UKIP leader Nigel Farage says a referendum resulting in a vote to stay i...'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'VIDEO: UKIP would accept the EU vote result URLGEN UKIP leader Nigel Farage says a referendum resulting in a vote to stay CUTMARK'
    if (result == expected):
        print 'case 5: pass - last token is not a full word'
    else:
        print 'case 5: failed - last token is not a full word'
        print result

    # case 6: tweet ends with a regular URL and no ellipsis
    # expectation: tweet is returned as is
    tweet = 'The #SNP are the #TartanTories who put Thatcher in no.10 for 18yrs out of revenge for the 40% rule bla bla bla bla bl URLGEN'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'The #SNP are the #TartanTories who put Thatcher in no.10 for 18yrs out of revenge for the 40% rule bla bla bla bla bl URLGEN'
    if (result == expected):
        print 'case 6: pass - max length, ends with URL, no ellipsis'
    else:
        print 'case 6: failed - max length, ends with URL, no ellipsis'
        print result

    # case 7: tweet ends with an ellipsis followed by a URL
    # expectation: ellipsis is removed, URL is removed, 'CUTMARK' marker is added to end of tweet
    tweet = 'VIDEO: I will never apologise for coalition says Lib Dem big leader Nick Clegg has defended his decision to go into ... URLGEN'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'VIDEO: I will never apologise for coalition says Lib Dem big leader Nick Clegg has defended his decision to go into CUTMARK'
    if (result == expected):
        print 'case 7: pass - maximum length with URL, cut'
    else:
        print 'case 7: failed - maximum length with URL, cut'
        print result

    # case 8: tweet ends with ' ...', is not of maximum length, but contains a URL that brings is to max length
    # expextation: ellipsis is replaced by 'CUTMARK' marker
    tweet = 'URLGEN Russell Brand #RussellBrand The breathtaking hypocrisy of Russell Brand, Ed Miliband, and Labour s front  UPDATE ...'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'URLGEN Russell Brand #RussellBrand The breathtaking hypocrisy of Russell Brand, Ed Miliband, and Labour s front  UPDATE CUTMARK'
    if (result == expected):
        print 'case 8: pass - full tweet, ends with ellipsis'
    else:
        print 'case 8: failed - full tweet, ends with ellipsis'
        print result

    # case 9: tweet ends with ' ...', is not of maximum length, but contains several URLs that bring is to max length
    # expextation: ellipsis and URLs are replaced by 'CUTMARK' marker
    tweet = 'The reason why I\'m always, always overweight... sigeg habhab :( masud pa kaha kos akong un... URLGEN URLGEN'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'The reason why I\'m always, always overweight... sigeg habhab :( masud pa kaha kos akong CUTMARK'
    if (result == expected):
        print 'case 9: pass - several URLs in cut tweet'
    else:
        print 'case 9: failed - several URLs in cut tweet'
        print result


if __name__ == "__main__":
    main()