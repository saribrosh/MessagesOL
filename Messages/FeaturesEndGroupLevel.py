ALL_CAPS_BONUS = 0.5
ALL_OTHERS_ARE_NOT_CAPS = -2
ALL_OTHERS_ARE_CAPS = 2
MIXED_GROUP = -0.5

def group_capitalization(group):

    group_level_cap_end_feature = []

    for item in group:
        group_level_cap_end_feature.append(0)

    start_with_lowercase_or_other = []
    start_with_uppercase = []
    for element in group:
        if (element[1])[0].isupper():
            start_with_uppercase.append(group.index(element))
        else:
            start_with_lowercase_or_other.append(group.index(element))

    # all segments begin with capital: possibly all standalone => small boost for end
    if len(start_with_uppercase) == len(group):
        for i in range(0, len(group)):
            group_level_cap_end_feature[i] = (ALL_CAPS_BONUS)

    # exactly one capital: unlikely end penalty
    if len(start_with_uppercase) == 1:
        cap_element_index = start_with_uppercase[0]
        group_level_cap_end_feature[cap_element_index] = ALL_OTHERS_ARE_NOT_CAPS

    # exactly one non capital: likely end bonus
    if len(start_with_lowercase_or_other) == 1:
        lowercase_element_index = start_with_lowercase_or_other[0]
        group_level_cap_end_feature[lowercase_element_index] = ALL_OTHERS_ARE_CAPS

    # mixed groups: capitalized are less likely to be endings
    if all(v == 0 for v in group_level_cap_end_feature) and \
            (len(start_with_lowercase_or_other) >= 1) and \
            (len(start_with_uppercase) >= 1):
        for item in start_with_uppercase:
            group_level_cap_end_feature[item] = MIXED_GROUP

    return group_level_cap_end_feature

def calculate_group_level_end_score(group):
    scores = group_capitalization(group)
    return scores