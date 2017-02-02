import DataProcessing
import ResourceGeneration
import LinguisticResources
import FeatureCalculation
import GroupCompositionValidation

def main():
    # data processing
    # multiple_segment_message_groups_dict, single_segments_list = DataProcessing.separate_data_to_multiples_and_singles('data-updated.csv')
    # test_dict, dev_dict = DataProcessing.create_dev_and_test_set(multiple_segment_message_groups_dict)

    # resource generation by source
    # OwnerListens_resource = ResourceGeneration.create_owner_listens_resource(single_segments_list)
    # nps_chat_resource = ResourceGeneration.create_nps_chat_resource()
    # twitter_resource = ResourceGeneration.create_twitter_resource()
    # resource = OwnerListens_resource + nps_chat_resource + twitter_resource

    # create csv resource from all different data sources
    # ResourceGeneration.create_resource_csv(resource)
    # create LM - bigram and trigram frequencies
    # LinguisticResources.ngram_frequencies('resource.txt')
    # create frequency count for first, middle and last tokens
    # LinguisticResources.calculate_token_frequency_by_position()

    # feature calculation

    # evaluation
    dict_with_results = FeatureCalculation.FeatureCalculation('mini_dev_set.csv')
    invalid_groups_dict = GroupCompositionValidation.validate_group(dict_with_results)

    for key, value in invalid_groups_dict.iteritems():
        print key, value

if __name__ == "__main__":
    main()
