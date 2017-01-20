import re

def generalize_URLs(input):
    pattern = 'http[^\s]+\.\.\.'
    t = re.sub(pattern, 'URLGEN...', input)
    if (t<> input):
        return t

    pattern = 'http[^\s]+'
    t = re.sub(pattern, 'URLGEN', input)
    if (t<> input):
        return t

    return input

def white_space_replacements(input):
    input = re.sub('\n', ' ', input)
    input = re.sub('\s+', ' ', input)
    input = re.sub('^\s', '', input)
    return input