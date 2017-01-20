import CalculateSendingTime

def main():

    input_positive = [
         # max difference
            [
                ['','','', '5/3/2016 5:38','','',''],
                ['','','', '5/3/2016 5:40','','','']
            ],
        # same time
            [
                ['','','', '5/3/2016 5:38','','',''],
                ['','','', '5/3/2016 5:38','','','']
            ],
        # legal difference around midnight
            [
                ['','','', '5/3/2016 23:59','','',''],
                ['','','', '5/4/2016 00:01','','','']
            ],
        # legal difference at midnight
            [
                ['','','', '5/3/2016 23:59','','',''],
                ['','','', '5/4/2016 00:00','','','']
            ]]

    input_negative = [
           # more than max difference
            [
                ['','','', '5/3/2016 5:38','','',''],
                ['','','', '5/3/2016 5:41','','','']
            ],
            # same time, consecutive months
            [
                ['','','', '5/3/2016 5:38','','',''],
                ['','','', '6/3/2016 5:38','','','']
            ],
            # same time, consecutive days
            [
                ['','','', '5/3/2016 5:38','','',''],
                ['','','', '5/4/2016 5:38','','','']
            ],
            # illegal difference around midnight
            [
                ['','','', '5/3/2016 00:01','','',''],
                ['','','', '5/4/2016 23:59','','','']
            ]]

    for i in range(0,len(input_positive)):
        result = CalculateSendingTime.sent_at_the_same_time((input_positive[i])[0], ((input_positive[i])[1]))
        if result:
            print 'test ', i+1, 'positive: pass'
        else:
             print 'test ', i+1, 'positive: failed'

    for i in range(0,len(input_negative)):
        result = CalculateSendingTime.sent_at_the_same_time((input_negative[i])[0], ((input_negative[i])[1]))
        if result:
            print 'test ', i+1, 'negative: failed'
        else:
             print 'test ', i+1, 'negative: pass'


if __name__ == "__main__":
    main()