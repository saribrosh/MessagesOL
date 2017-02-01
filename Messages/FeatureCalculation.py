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
    output_rows = []
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

    for group_id, group in groups_dict.iteritems():

        # segment level features
        for element in group:
            key = element[0]
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

                seg_beginning_score = FeaturesBeginningSegmentLevel.calculate_segment_level_beginning_score(key, text)
                seg_middle_score = FeaturesMiddleSegmentLevel.calculate_segment_level_middle_score(key, text)
                seg_end_score = FeaturesEndSegmentLevel.calculate_segment_level_end_score(key, text)
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
            segment_scores = [total_beginning_score, total_middle_score, total_end_score, total_standalone_score]
            segment_scores_dict[element[0]] = segment_scores

        # veto feature: serial number
        for element in group:
            key = element[0]
            if key in FeaturesBeginningSegmentLevel.beginning_serial:
                (segment_scores_dict[key])[1] = 0
                (segment_scores_dict[key])[2] = 0
                (segment_scores_dict[key])[3] = 0
            if key in FeaturesMiddleSegmentLevel.middle_serial:
                (segment_scores_dict[key])[0] = 0
                (segment_scores_dict[key])[2] = 0
                (segment_scores_dict[key])[3] = 0
            if key in FeaturesEndSegmentLevel.end_serial:
                (segment_scores_dict[key])[0] = 0
                (segment_scores_dict[key])[1] = 0
                (segment_scores_dict[key])[3] = 0

        # position result calculation
            segment_position_scores = segment_scores_dict.get(key)
            position_results = Evaluation.determine_element_position(key, segment_position_scores)
            element_position_results[key] = position_results
            element_success_info = Evaluation.compare_with_tagging(element, position_results)
            element_success_info_dict[key] = element_success_info

            output_row = [group_id] + \
                         element + \
                         segment_scores_dict[key] + \
                         element_position_results[key] + \
                         element_success_info_dict[key]
            output_rows.append(output_row)

    # reporting metrics
    header = header[:] + ['Beginning Score'] + ['Middle Score'] + ['End Score'] + ['Standalone Score'] + \
                         ['Result Beginning'] + ['Result Middle'] + ['Result End'] + ['Result Standalone'] + \
                         ['Beginning Correct'] + ['Middle Correct'] + ['End Correct'] + ['Standalone Correct']

    total_valid_sentences = number_of_segments-subtract_from_total_count
    correct_beginning_segments = 0
    correct_middle_segments = 0
    correct_end_segments = 0
    correct_standalone_segments = 0

    for key, value in element_success_info_dict.iteritems():
        if value[0] == 1:
            correct_beginning_segments += 1
        if value[1] == 1:
            correct_middle_segments += 1
        if value[2] == 1:
            correct_end_segments += 1
        if value[3] == 1:
            correct_standalone_segments += 1

    print correct_beginning_segments
    print correct_middle_segments
    print correct_end_segments
    print correct_standalone_segments

    beginning_precision = correct_beginning_segments/float(total_valid_sentences)
    middle_precision = correct_middle_segments/float(total_valid_sentences)
    end_precision = correct_end_segments/float(total_valid_sentences)
    standalone_precision = correct_standalone_segments/float(total_valid_sentences)

    print beginning_precision
    print middle_precision
    print end_precision
    print standalone_precision

    with open('results_mini_dev_2.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in output_rows:
            writer.writerow(row)

        writer.writerow(['correct beginning segments: ' + str(correct_beginning_segments)])
        writer.writerow(['beginning precision: ' + str(beginning_precision)])
        writer.writerow(['correct middle segments: ' + str(correct_middle_segments)])
        writer.writerow(['middle precision: ' + str(middle_precision)])
        writer.writerow(['correct end segments: ' + str(correct_end_segments)])
        writer.writerow(['end precision: ' + str(end_precision)])
        writer.writerow(['correct standalone segments: ' + str(correct_standalone_segments)])
        writer.writerow(['standalone precision: ' + str(standalone_precision)])

    return output_rows