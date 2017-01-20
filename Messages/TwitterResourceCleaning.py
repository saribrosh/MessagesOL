import re

def discover_length(tweet):
    urls = tweet.count('URLGEN')
    original_length = len(tweet)+17*urls
    return original_length

def cut_tweet_indication(tweet):
    if len(tweet) > 3:
        last_3 = tweet[-3:]
    else:
        return False
    if len(tweet) > 10:
        last_10 = tweet[-10:]
    if last_3 == '...':
        return True
    if last_10 == '... URLGEN':
        return True
    return False


def mark_cut_content(tweet):
    tweet_length = discover_length(tweet)
    if tweet_length < 137:
        return tweet
    cut_ending_pattern = re.compile('\.\.\.((\sURLGEN)+?)?$')
    cut_ending = re.search(cut_ending_pattern, tweet)
    if cut_ending is None:
        return tweet
    else:
        cut_ind_index = cut_ending.start()
        if tweet[cut_ind_index-1] == ' ':
            tweet = tweet[:cut_ind_index-1] + ' CUTMARK'
        else:
            tweet = tweet[:cut_ind_index-1]
            char_before_cut_token_index = tweet.rfind(' ')
            tweet = tweet[:char_before_cut_token_index] + ' CUTMARK'
    return tweet

def remove_retweet_data(tweet):
    retweet_pattern = re.compile('(RT\s)?\"?[@#][^\s]+\s(([@#][^\s]+\s)+)?')
    if re.match(retweet_pattern, tweet):
        last_char_of_RT_data = re.search(retweet_pattern, tweet).end()
        tweet = tweet[last_char_of_RT_data:]
    return tweet

def remove_tags_from_ending(tweet):
    end_tags_pattern = re.compile('\s(((([#@][^\s]+)|(URLGEN))\s)+?)?(([#@][^\s]+)|(URLGEN))$')
    if re.search(end_tags_pattern, tweet):
        # print 'yes'
        first_char_of_RT_data = re.search(end_tags_pattern, tweet).start()
        tweet = tweet[:first_char_of_RT_data]
    return tweet

def calculate_string_differences(tweet1, tweet2):
    if len(tweet1) <> len(tweet2):
        return False
    else:
        zipped = zip(tweet1, tweet2)
        differences = 0
        for i,j in zipped:
            if i <> j:
                differences += 1
    if differences < 3:
        return True
    else:
        return False