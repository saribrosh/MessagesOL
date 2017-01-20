import datetime

MAX_TIME_DIFFERENCE_ALLOWED_WITHIN_GROUP = 2

def sent_at_the_same_time(message1, message2):
    time_format = "%m/%d/%Y %H:%M"
    current_date_time = datetime.datetime.strptime(message2[3], time_format)
    previous_date_time = datetime.datetime.strptime(message1[3], time_format)

    delta = current_date_time - previous_date_time
    days = delta.days
    seconds = delta.total_seconds()
    minutes = (seconds % 3600) // 60

    return (days == 0) and (minutes <= MAX_TIME_DIFFERENCE_ALLOWED_WITHIN_GROUP)
