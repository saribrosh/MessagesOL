from __future__ import division
import FeaturesBeginningSegmentLevel
import FeaturesEndSegmentLevel
import FeaturesMiddleSegmentLevel
import csv
import collections

STANDALONE_BEGINNING = 10
STANDALONE_END = 10
END_THRESHOLD = 2.3
BEGINNING_THRESHOLD = 4

def is_correct_first_in_group(element, is_beginning):
    print element
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

def FeatureCalculation(set):
    number_of_segments = 0
    groups_dict = {}
    with open(set, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = (csvfile.readline()).split(',')
        previous_group_index = -1
        current_group = []
        for line in reader:
            current_group_index = line[0]
            if current_group_index == previous_group_index:
                current_group.append(line[1:])
            else:
                if previous_group_index == -1:
                    current_group.append(line[1:])
                else:
                    groups_dict[previous_group_index] = current_group
                    current_group = [line[1:]]
                previous_group_index = current_group_index
            number_of_segments += 1
        groups_dict[previous_group_index] = current_group

    groups_dict = collections.OrderedDict(sorted(groups_dict.items()))

    # for key, value in groups_dict.iteritems():
    #     print key, value

    header = header[1:] + ['Beginning Score'] + ['Beginning Correct'] + \
                        ['Middle Score'] + ['Middle Correct'] + \
                        ['End Score'] + ['End Correct']
    output_rows = []
    subtract_from_total_count = 0
    correct_beginning_segments = 0
    correct_middle_segments = 0
    correct_end_segments = 0

    for group_id, group in groups_dict.iteritems():
        # segment level features
        for element in group:
            text = element[1]
            text = text.decode("utf-8")
            text = text.encode("ascii","ignore")
            if not text:
                beginning_score = STANDALONE_BEGINNING
                middle_score = 0
                end_score = STANDALONE_END
            else:
                if (element[4] == -1):
                    subtract_from_total_count += 1

                beginning_score = \
                    FeaturesBeginningSegmentLevel.capitalization(text) + \
                    FeaturesBeginningSegmentLevel.first_token_likelihood(text) + \
                    FeaturesBeginningSegmentLevel.full_word_indication(text) + \
                    FeaturesBeginningSegmentLevel.common_first_word(text) + \
                    FeaturesBeginningSegmentLevel.serial_number(text)

                middle_score = \
                    FeaturesMiddleSegmentLevel.cut_from_both_sides(text) + \
                    FeaturesMiddleSegmentLevel.serial_number(text)

                end_score = \
                    FeaturesEndSegmentLevel.EOSPunctuation(text) + \
                    FeaturesEndSegmentLevel.full_word_indication(text) + \
                    FeaturesEndSegmentLevel.last_token_likelihood(text) + \
                    FeaturesEndSegmentLevel.unlikely_last_token_penalty(text) + \
                    FeaturesEndSegmentLevel.serial_number(text)

                is_beginning = False
                is_middle = False
                is_end = False

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

                isCorrectFirstInGroup = is_correct_first_in_group(element, is_beginning)
                if (isCorrectFirstInGroup == 1):
                    correct_beginning_segments += 1

                isCorrectMiddleInGroup = is_correct_middle_in_group(element, is_middle)
                if (isCorrectMiddleInGroup == 1):
                    correct_middle_segments += 1

                isCorrectLastInGroup = is_correct_last_in_group(element, is_end)
                if (isCorrectLastInGroup == 1):
                    correct_end_segments += 1            

            output_row = element + [beginning_score] + [isCorrectFirstInGroup] + \
                         [middle_score] + [isCorrectMiddleInGroup] + \
                         [end_score] + [isCorrectLastInGroup]
            output_rows.append(output_row)

    with open('mini_dev_results_file_2.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in output_rows:
            writer.writerow(row)
        total_valid_sentences = number_of_segments-subtract_from_total_count
        beginning_precision = correct_beginning_segments/total_valid_sentences
        middle_precision = correct_middle_segments/float(total_valid_sentences)
        end_precision = correct_end_segments/float(total_valid_sentences)
        writer.writerow(['total valid sentences: ' + str(total_valid_sentences)])

        writer.writerow(['correct beginning segments: ' + str(correct_beginning_segments)])
        print ('correct beginning segments: ', correct_beginning_segments)
        writer.writerow(['beginning precision: ' + str(beginning_precision)])
        print ('beginning precision: ', beginning_precision)

        writer.writerow(['correct middle segments: ' + str(correct_middle_segments)])
        print ('correct middle segments: ', correct_middle_segments)
        writer.writerow(['middle precision: ' + str(middle_precision)])
        print ('middle precision: ', middle_precision)

        writer.writerow(['correct end segments: ' + str(correct_end_segments)])
        print ('correct end segments: ', correct_end_segments)
        writer.writerow(['end precision: ' + str(end_precision)])
        print ('end precision: ', end_precision)

