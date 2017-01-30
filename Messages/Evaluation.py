END_THRESHOLD = 2.3
BEGINNING_THRESHOLD = 4

def is_correct_first_in_group(element, is_beginning):
    if element[3] == '-1':
        return -1
    else:
        if (is_beginning):
            if int(element[5]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[5]) == 0:
                return 1
            else:
                return 0

def is_correct_middle_in_group(element, is_middle):
    if element[3] == '-1':
        return -1
    else:
        if (is_middle):
            if int(element[6]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[6]) == 0:
                return 1
            else:
                return 0

def is_correct_last_in_group(element, is_end):
    if element[3] == '-1':
        return -1
    else:
        if (is_end):
            if int(element[7]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[7]) == 0:
                return 1
            else:
                return 0

def is_correct_standalone(element, is_standalone):
    if element[3] == '-1':
        return -1
    else:
        if (is_standalone):
            if int(element[8]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[8]) == 0:
                return 1
            else:
                return 0


def determine_element_position(segment_key, element_scores_entry):

    is_beginning = False
    is_middle = False
    is_end = False
    is_standalone = False

    beginning_score = element_scores_entry[0]
    middle_score = element_scores_entry[1]
    end_score = element_scores_entry[2]

    if (max(beginning_score, middle_score, end_score) == beginning_score):
        is_beginning = True
        if end_score >= END_THRESHOLD:
            is_end = True
    if (max(beginning_score, middle_score, end_score) == end_score):
        is_end = True
        if beginning_score >= BEGINNING_THRESHOLD:
            is_beginning = True
    if (max(beginning_score, middle_score, end_score) == middle_score):
        if not is_beginning and not is_end:
            is_middle = True
    if(is_beginning and is_end):
        is_standalone = True

    return [is_beginning, is_middle, is_end, is_standalone]


def compare_with_tagging(element, position_results):
    isCorrectFirstInGroup = is_correct_first_in_group(element, position_results[0])
    isCorrectMiddleInGroup = is_correct_middle_in_group(element, position_results[1])
    isCorrectLastInGroup = is_correct_last_in_group(element, position_results[2])
    isCorrectStandalone = is_correct_standalone(element, position_results[3])

    success_metrics = [isCorrectFirstInGroup, \
                       isCorrectMiddleInGroup, \
                       isCorrectLastInGroup, \
                       isCorrectStandalone]

    return success_metrics