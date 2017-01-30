from __future__ import division
import FeaturesBeginningSegmentLevel
import FeaturesMiddleSegmentLevel
import FeaturesEndSegmentLevel
import FeaturesEndGroupLevel
import Evaluation
import csv
import collections

STANDALONE_BEGINNING = 10
STANDALONE_END = 10


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

    segment_scores_dict = {}
    element_position_results = {}
    element_success_info_dict = {}
    subtract_from_total_count = 0
    correct_beginning_segments = 0
    correct_middle_segments = 0
    correct_end_segments = 0
    correct_standalone_segments = 0

    for group_id, group in groups_dict.iteritems():

        # segment level features
        for element in group:
            text = element[1]
            text = text.decode("utf-8")
            text = text.encode("ascii","ignore")
            if not text:
                seg_beginning_score = STANDALONE_BEGINNING
                seg_middle_score = 0
                seg_end_score = STANDALONE_END
                seg_standalone_score = float((seg_beginning_score+seg_end_score)/2)
            else:
                if (element[4] == -1):
                    subtract_from_total_count += 1

                seg_beginning_score = FeaturesBeginningSegmentLevel.calculate_segment_level_beginning_score(text)
                seg_middle_score = FeaturesMiddleSegmentLevel.calculate_segment_level_middle_score(text)
                seg_end_score = FeaturesEndSegmentLevel.calculate_segment_level_end_score(text)
                seg_standalone_score = float((seg_beginning_score+seg_end_score)/2)

            segment_scores_dict[element[0]] = [seg_beginning_score, seg_middle_score, seg_end_score, seg_standalone_score]

        # group level features
        # group_beginning_scores = []
        # group_middle_scores = []
        group_end_scores = FeaturesEndGroupLevel.calculate_group_level_end_score(group)
        # group_standalone_scores = []

        for i in range(0,len(group)):
            element = group[i]
            scores = segment_scores_dict.get(element[0])
            total_beginning_score = scores[0] #+ group_beginning_scores[i]
            total_middle_score = scores[1] #+ group_middle_scores[i]
            total_end_score = scores[2] + group_end_scores[i]
            total_standalone_score = scores[3] #+ group_standalone_scores[i]
            segment_scores_dict[element[0]] = [total_beginning_score, total_middle_score, total_end_score, total_standalone_score]

        # position result calculation
            segment_key = element[0]
            segment_position_scores = segment_scores_dict.get(segment_key)
            position_results = Evaluation.determine_element_position(segment_key, segment_position_scores)
            element_position_results[segment_key] = position_results
            element_success_info = Evaluation.compare_with_tagging(element, position_results)
            element_success_info_dict[segment_key] = element_success_info

    # reporting metrics


    header = header[1:] + ['Beginning Score'] + ['Middle Score'] + ['End Score'] + ['Standalone Score'] + \
                         ['Beginning Correct'] + ['Middle Correct'] + ['End Correct'] + ['Standalone Correct']

    # with open('mini_dev_results_file_2.csv', 'wb') as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow(header)
    #     for row in output_rows:
    #         writer.writerow(row)
    #     total_valid_sentences = number_of_segments-subtract_from_total_count
    #     beginning_precision = correct_beginning_segments/total_valid_sentences
    #     middle_precision = correct_middle_segments/float(total_valid_sentences)
    #     end_precision = correct_end_segments/float(total_valid_sentences)
    #     standalone_precision = correct_standalone_segments/float(total_valid_sentences)
    #     writer.writerow(['total valid sentences: ' + str(total_valid_sentences)])
    #
    #     writer.writerow(['correct beginning segments: ' + str(correct_beginning_segments)])
    #     print ('correct beginning segments: ', correct_beginning_segments)
    #     writer.writerow(['beginning precision: ' + str(beginning_precision)])
    #     print ('beginning precision: ', beginning_precision)
    #
    #     writer.writerow(['correct middle segments: ' + str(correct_middle_segments)])
    #     print ('correct middle segments: ', correct_middle_segments)
    #     writer.writerow(['middle precision: ' + str(middle_precision)])
    #     print ('middle precision: ', middle_precision)
    #
    #     writer.writerow(['correct end segments: ' + str(correct_end_segments)])
    #     print ('correct end segments: ', correct_end_segments)
    #     writer.writerow(['end precision: ' + str(end_precision)])
    #     print ('end precision: ', end_precision)
    #
    #     writer.writerow(['correct standalone segments: ' + str(correct_standalone_segments)])
    #     print ('correct standalone segments: ', correct_standalone_segments)
    #     writer.writerow(['standalone precision: ' + str(standalone_precision)])
    #     print ('standalone precision: ', standalone_precision)