import TwitterResourceCleaning

def main():

    # case 1: ends with hashtag
    tweet = 'At one point it looked like Ed Miliband was giving a thumbs up. Turns out he was counting on his hand. #bbcqt'
    result = TwitterResourceCleaning.remove_tags_from_ending(tweet)
    expected = 'At one point it looked like Ed Miliband was giving a thumbs up. Turns out he was counting on his hand.'
    if (result == expected):
        print 'case 1: pass - ends with single hashtag'
    else:
        print 'case 1: failed - ends with single hashtag'
        print result

    # case 2: ends with multiple hashtags and @
    tweet = 'Big thanks to everyone! Couldn\'t have done it without all the support! :) @HIT_LondonCity @BaxterStorey @GBCookBook @Bschefacademy #thanks'
    result = TwitterResourceCleaning.remove_tags_from_ending(tweet)
    expected = 'Big thanks to everyone! Couldn\'t have done it without all the support! :)'
    if (result == expected):
        print 'case 2: pass - multiple tags'
    else:
        print 'case 2: failed - multiple tags'
        print result

    # case 3: ends with URLGEN
    tweet = 'Big up to Ivory from How High standing up to Nick Clegg like that URLGEN'
    result = TwitterResourceCleaning.remove_tags_from_ending(tweet)
    expected = 'Big up to Ivory from How High standing up to Nick Clegg like that'
    if (result == expected):
        print 'case 3: pass - URLGEN'
    else:
        print 'case 3: failed - URLGEN'
        print result

    # case 4: ends with multiple hashtags and URLGEN which is not the last token
    tweet = 'Blog Post &gt; THE HUNGER GAMES: MOCKINGJAY - PART 2 (2015): No More Teasers :-) URLGEN #TheHungerGames URLGEN'
    result = TwitterResourceCleaning.remove_tags_from_ending(tweet)
    expected = 'Blog Post &gt; THE HUNGER GAMES: MOCKINGJAY - PART 2 (2015): No More Teasers :-)'
    if (result == expected):
        print 'case 4: pass - sequence in which the URLGEN is not only the last token'
    else:
        print 'case 4: failed - sequence in which the URLGEN is not only the last token'
        print result

    # case 5: all elements removed
    tweet = '#SNPout #SNP #Labour #LibDems #Conservative #ukip #Greens #GE2015 #Ge15 #Scotland URLGEN'
    result = TwitterResourceCleaning.remove_tags_from_ending(tweet)
    expected = ''
    if (result == expected):
        print 'case 5: pass - all elements removed'
    else:
        print 'case 5: failed - all elements removed'
        print result

    # case 6: multiple hashtags and at signs in middle of tweet
    tweet = 'Big @Nigel_Farage #bossing it again @UKIP #UKIP'
    result = TwitterResourceCleaning.remove_tags_from_ending(tweet)
    expected = 'Big @Nigel_Farage #bossing it again'
    if (result == expected):
        print 'case 6: pass - tags in the middle'
    else:
        print 'case 6: failed - tags in the middle'
        print result



if __name__ == "__main__":
    main()