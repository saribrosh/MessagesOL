import TwitterResourceCleaning

def main():

# RT @stardust193: #AskNigelFarage #AskNigel #UKIP #AskFarage #bbcqt Some people just love big government dictating everything they can &amp; <cut>

    # case 1: starts with RT
    # expectation: no '<cut>' marker is added to returned tweet
    tweet = 'how am i gonna watch eu lcs in 6 hours :( help i need more sleep'
    result = TwitterResourceCleaning.mark_cut_content(tweet)
    expected = 'how am i gonna watch eu lcs in 6 hours :( help i need more sleep'
    if (result == expected):
        print 'case 1: pass - starts with RT'
    else:
        print 'case 1: failed - starts with RT'
        print result

    # case 2: RT and at sign
    tweet = 'RT @1manandhisbeard: Settling down to watch the lizard king himself Nigel Farage dig himself a deeper grave #hypnotoad'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'Settling down to watch the lizard king himself Nigel Farage dig himself a deeper grave #hypnotoad'
    if (result == expected):
        print 'case 2: pass - RT and @'
    else:
        print 'case 2: failed - RT and @'
        print result

    # case 3: RT and multiple hashtags and at signs
    tweet = 'RT @AlanUkip #Nigel_Farage #hi @Nigel did well on the @bbcqt go @UKIP'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'did well on the @bbcqt go @UKIP'
    if (result == expected):
        print 'case 3: pass - RT and multiple @ and #'
    else:
        print 'case 3: failed - RT and multiple @ and #'
        print result

    # case 4: hashtag
    tweet = '#ThankYou! for Debbie &amp; Carol :) Thanks for seeing a record number of patients in the discharge lounge yesterday.  You\'re great!'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'for Debbie &amp; Carol :) Thanks for seeing a record number of patients in the discharge lounge yesterday.  You\'re great!'
    if (result == expected):
        print 'case 4: pass - #'
    else:
        print 'case 4: failed - #'
        print result

    # case 5: at sign
    tweet = '@voidstxlinski theyre so cute :('
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'theyre so cute :('
    if (result == expected):
        print 'case 5: pass - @'
    else:
        print 'case 5: failed - @'
        print result

    # case 6: multiple hashtags and at signs
    tweet = '@xQueenBriee @Invictus47Diddy @Raven3611 #xAnnaCheeriosx @HEELZigglez :D U KNO WHET'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = ':D U KNO WHET'
    if (result == expected):
        print 'case 6: pass - multiple @ and #'
    else:
        print 'case 6: failed - multiple @ and #'
        print result

    # case 7: tweet is only retweet data and hashtags
    tweet = '@zavvi @b9scottuk @gkm86'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = ''
    if (result == expected):
        print 'case 7: pass - only data for removal'
    else:
        print 'case 7: failed - only data for removal'
        print result

    # case 8: RT data available but not in beginning
    tweet = 'AWW&gt;. RT @iandavis28: @idahorner @eileen_means You look like a caring human being so you can\'t be a Tory so yes labour your best option!'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'AWW&gt;. RT @iandavis28: @idahorner @eileen_means You look like a caring human being so you can\'t be a Tory so yes labour your best option!'
    if (result == expected):
        print 'case 8: pass - RT data in the middle'
    else:
        print 'case 8: failed - RT data in the middle'
        print result

    # case 9: with colon after at sign, followed by more at signs
    tweet = 'RT @010501AZ: @labourpress @WingsScotland Then Ed Miliband won\'t be prime minister.'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'Then Ed Miliband won\'t be prime minister.'
    if (result == expected):
        print 'case 9: pass - with colon followed by more @'
    else:
        print 'case 9: failed - with colon followed by more @'
        print result

    tweet = 'RT @mac123_m: Osborne\'s borrowed more in 5yrs than LAB did in 13yrs.The Tory "#LongTermEconomicPlan has FAILED \
    #Ed4PM <cut>'
    result = TwitterResourceCleaning.remove_retweet_data(tweet)
    expected = 'Osborne\'s borrowed more in 5yrs than LAB did in 13yrs.The Tory "#LongTermEconomicPlan has FAILED \
    #Ed4PM <cut>'
    if (result == expected):
        print 'case 10: pass - test'
    else:
        print 'case 10: test'
        print result

if __name__ == "__main__":
    main()