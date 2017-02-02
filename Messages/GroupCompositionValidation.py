def validate_group(dict_with_results):

    invalid_groups_dict = {}

    for group_id, group in dict_with_results.iteritems():
        count_beginning = 0
        count_end = 0
        for segment in group:
            if segment[13]:
                count_beginning += 1
            if segment[15]:
                count_end += 1
        if count_beginning != count_end:
            invalid_groups_dict[group_id] = group

    return invalid_groups_dict