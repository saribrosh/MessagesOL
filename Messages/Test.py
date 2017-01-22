from __future__ import division
import FeaturesBeginning
import FeaturesEnd
import FeaturesMiddle
import csv

def is_correct_first_in_group(element, beginning_score):
    if element[4] == '-1':
        return -1
    else:
        if (beginning_score > 4):
            if int(element[6]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[6]) == 0:
                return 1
            else:
                return 0

def is_correct_middle_in_group(element, middle_score):
    if element[4] == '-1':
        return -1
    else:
        if (middle_score > 5):
            if int(element[7]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[7]) == 0:
                return 1
            else:
                return 0

def is_correct_last_in_group(element, end_score):
    if element[4] == '-1':
        return -1
    else:
        if (end_score > 2.3):
            if int(element[8]) == 1:
                return 1
            else:
                return 0
        else:
            if int(element[8]) == 0:
                return 1
            else:
                return 0

def FeatureCalculation(set):
    number_of_segments = 0
    groups_dict = {}
    with open(set, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = (csvfile.readline()).split(',')
        current_group = []
        current_group_index = -1
        for line in reader:
            if int(line[0]) == current_group_index:
                current_group.append(line)
            else:
                groups_dict[current_group_index] = current_group
                current_group_index = int(current_group_index)+1
                current_group = [line]
            number_of_segments +=1
        groups_dict[current_group_index] = current_group
    groups_dict.pop(-1, None)

    # for key, value in groups_dict.iteritems():
    #     print key, value

    header = header + ['Beginning Score'] + ['Beginning Correct'] + \
             ['Middle Score'] + ['Middle Correct'] + \
             ['End Score'] + ['End Correct']
    output_rows = []
    substract_from_total_count = 0
    correct_beginning_segments = 0
    correct_middle_segments = 0
    correct_end_segments = 0

    for group_id, group in groups_dict.iteritems():
        for element in group:
            text = element[2]
            beginning_score = \
                FeaturesBeginning.capitalization(text) + \
                FeaturesBeginning.first_token_likelihood(text) + \
                FeaturesBeginning.full_word_indication(text) + \
                FeaturesBeginning.common_first_word(text)
            isCorrectFirstInGroup = is_correct_first_in_group(element, beginning_score)
            if (isCorrectFirstInGroup == -1):
                substract_from_total_count += 1
            if (isCorrectFirstInGroup == 1):
                correct_beginning_segments += 1

            middle_score = FeaturesMiddle.cut_from_both_sides(text)
            isCorrectMiddleInGroup = is_correct_middle_in_group(element, middle_score)
            if (isCorrectMiddleInGroup == 1):
                correct_middle_segments += 1

            end_score = \
                FeaturesEnd.EOSPunctuation(text) + \
                FeaturesEnd.full_word_indication(text) + \
                FeaturesEnd.last_token_likelihood(text) + \
                FeaturesEnd.unlikely_last_token_penalty(text)
            isCorrectLastInGroup = is_correct_last_in_group(element, end_score)
            if (isCorrectLastInGroup == 1):
                correct_end_segments += 1

            output_row = element + [beginning_score] + [isCorrectFirstInGroup] + \
                         [middle_score] + [isCorrectMiddleInGroup] + \
                         [end_score] + [isCorrectLastInGroup]
            output_rows.append(output_row)


    with open('results_file_.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in output_rows:
            writer.writerow(row)
        print 'number_of_segments: ', number_of_segments
        print 'substract_from_total_count: ', substract_from_total_count
        total_valid_sentences = number_of_segments-substract_from_total_count
        print "correct_beginning_segments: ", correct_beginning_segments
        print "total_valid_sentences: ", total_valid_sentences
        beginning_precision = correct_beginning_segments/total_valid_sentences
        print 'beginning_precision: ', beginning_precision
        middle_precision = correct_middle_segments/float(total_valid_sentences)
        end_precision = correct_end_segments/float(total_valid_sentences)
        writer.writerow(['total valid sentences: ' + str(total_valid_sentences)])
        print ('total valid sentences: ', total_valid_sentences)

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

