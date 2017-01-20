import csv
import operator
import CalculateSendingTime
from itertools import ifilterfalse


def sort_data(raw_data):
    # sort data by 'device id', 'Sent At' and message
    with open(raw_data, 'rb') as infile:
        csvreader = csv.reader(infile, delimiter=',')
        header = next(csvreader, None)
        sorted_data = sorted(csvreader, key=operator.itemgetter(2,3,5))
    return sorted_data

def assign_ID_to_entries(data):
    # give each entry a unique ID
    current_ID = 0
    for entry in data:
        entry.append(current_ID)
        current_ID += 1
    return data

def remove_duplicates(data):
    duplicate_IDs = []
    for i in range(1,len(data)):
        if ((data[i])[2] == (data[i-1])[2]) and \
                ((data[i])[5] == (data[i-1])[5]) and \
                ((CalculateSendingTime.sent_at_the_same_time(data[i-1], data[i]))):
            dup_ID = (data[i])[7]
            duplicate_IDs.append(dup_ID)

    return list(ifilterfalse(lambda x: (x[7] in duplicate_IDs), data))

def check_relevant_codes(current_record, previous_record):
    valid_codes = ['8', '13']
    result = (current_record[4] in valid_codes) and \
             (previous_record[4] == current_record[4])
    return result

def group_by_time_and_device(data):
    # if consecutive messages were a)sent from the same device id, and b) sent at the same time:
    # give them a group ID and add to a dictionary in which the ID is the key and the value is the list of entries
    # else, add to a list of single segments
    list_of_groups = []
    current_group = [data[0]]
    for i in range(1, len(data)):
        current_record = data[i]
        previous_record = data[i-1]
        same_device = (current_record[2] == previous_record[2])
        same_time = CalculateSendingTime.sent_at_the_same_time(previous_record,current_record)
        same_legal_code = check_relevant_codes(current_record, previous_record)
        if (same_time and same_device and same_legal_code):
            current_group.append(current_record)
        else:
            list_of_groups.append(current_group)
            current_group = [data[i]]
    if i == len(data)-1:
        list_of_groups.append(current_group)
    return list_of_groups

def sort_list_of_groups(list_of_groups):
    group_key = 0
    multiple_segments_potential_groups_dict = {}
    single_segments_list = []
    for list in list_of_groups:
        if len(list) == 1:
            single_segments_list.append(list[0])
        else:
            multiple_segments_potential_groups_dict[group_key] = list
            group_key += 1
    return multiple_segments_potential_groups_dict, single_segments_list

def separate_data_to_multiples_and_singles(raw_data):
    sorted_data = sort_data(raw_data)
    sorted_data_with_entry_IDs = assign_ID_to_entries(sorted_data)
    data_no_dups = remove_duplicates(sorted_data_with_entry_IDs)
    list_of_groups= group_by_time_and_device(data_no_dups)
    multiple_segments_potential_groups_dict, single_segments_list = sort_list_of_groups(list_of_groups)
    return multiple_segments_potential_groups_dict, single_segments_list

def create_dev_and_test_set(multiple_segment_message_groups_dict):
    groups = len(multiple_segment_message_groups_dict)
    test_size = int(0.2*groups)
    test_dict = dict(multiple_segment_message_groups_dict.items()[0:test_size])
    dev_dict = dict(multiple_segment_message_groups_dict.items()[test_size+1:])

    with open('dev_set.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            header = ['Group ID', 'Segment ID', 'Text', 'Length', 'Tagging']
            writer.writerow(header)
            for key, value in dev_dict.items():
                number_of_segments_in_group = len(value)
                for i in range(0, number_of_segments_in_group):
                    group_ID = key
                    segment_ID = (value[i])[7]
                    segment_text = (value[i])[5]
                    segment_length = (value[i])[6]
                    row = [group_ID, segment_ID, segment_text, segment_length]
                    writer.writerow(row)

    with open('test_set.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            header = ['Group ID', 'Segment ID', 'Text', 'Length', 'Tagging']
            writer.writerow(header)
            for key, value in test_dict.items():
                number_of_segments_in_group = len(value)
                for i in range(0, number_of_segments_in_group):
                    group_ID = key
                    segment_ID = (value[i])[7]
                    segment_text = (value[i])[5]
                    segment_length = (value[i])[6]
                    row = [group_ID, segment_ID, segment_text, segment_length]
                    writer.writerow(row)

    return test_dict, dev_dict


