import csv
import nltk
from nltk.util import ngrams
from collections import Counter
import re

def ngram_frequencies(resource):

    markers_list = ['BEGINMARK', 'ENDMARK', 'CUTMARK']

    with open(resource, 'r') as f:
        read_data = f.read()

        tokens = nltk.word_tokenize(read_data)
        for i in range(0,len(tokens)):
            if tokens[i] not in markers_list:
                tokens[i] = (tokens[i]).lower()

        print tokens

        unigrams = list(ngrams(tokens, 1))
        unigram_counts = (Counter(unigrams))
        with open('unigram_count.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in unigram_counts.items():
                writer.writerow([key[0], value])

        bigrams = list(ngrams(tokens, 2))
        bigram_counts = (Counter(bigrams))
        with open('bigram_count.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in bigram_counts.items():
                if key[0] != 'ENDMARK':
                    writer.writerow([key, value])

        trigrams = list(ngrams(tokens, 3))
        trigram_counts = (Counter(trigrams))
        with open('trigram_count.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in trigram_counts.items():
                if key[0] != 'ENDMARK' and \
                    key[1] != 'ENDMARK' and \
                    key[1] != 'BEGINMARK' and \
                    key[2] != 'BEGINMARK':
                    writer.writerow([key, value])

def calculate_token_frequency_by_position():
    first_tokens_case_insensitive_dict = {}
    middle_tokens_case_insensitive_dict = {}
    last_tokens_case_insensitive_dict = {}

    with open('trigram_count.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for entry in reader:
            trigram = (entry[0])[1:-1]
            trigram = re.sub('^[\'\"]', '', trigram)
            trigram = re.sub('[\'\"]$', '', trigram)
            trigram = re.sub(' [\'\"]', ' ', trigram)
            trigram = re.sub('[\'\"]\, ', ', ', trigram)

            trigram = trigram.split(', ')

            if trigram[0] == 'BEGINMARK' and trigram[2] != 'ENDMARK':
                first_token = trigram[1].lower()
                if first_token in first_tokens_case_insensitive_dict.keys():
                    val = int(first_tokens_case_insensitive_dict[first_token])
                    first_tokens_case_insensitive_dict[first_token] = val+int(entry[1])
                else:
                    first_tokens_case_insensitive_dict[first_token] = entry[1]

            if trigram[2] == 'ENDMARK' and trigram[1] != 'CUTMARK':
                last_token = trigram[1].lower()
                if last_token in last_tokens_case_insensitive_dict.keys():
                    val = int(last_tokens_case_insensitive_dict[last_token])
                    last_tokens_case_insensitive_dict[last_token] = val+int(entry[1])
                else:
                    last_tokens_case_insensitive_dict[last_token] = entry[1]

            if trigram[0] != 'BEGINMARK' and trigram[2] != 'ENDMARK' and trigram[2] != 'CUTMARK':
                middle_token = trigram[1].lower()
                if middle_token in middle_tokens_case_insensitive_dict.keys():
                    val = int(middle_tokens_case_insensitive_dict[middle_token])
                    middle_tokens_case_insensitive_dict[middle_token] = val+int(entry[1])
                else:
                    middle_tokens_case_insensitive_dict[middle_token] = entry[1]


        with open('first_tokens_dict.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in first_tokens_case_insensitive_dict.items():
                writer.writerow([key, value])

        with open('middle_tokens_dict.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in middle_tokens_case_insensitive_dict.items():
                writer.writerow([key, value])

        with open('last_tokens_dict.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in last_tokens_case_insensitive_dict.items():
                writer.writerow([key, value])