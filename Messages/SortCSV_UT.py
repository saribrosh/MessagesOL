import DataProcessing

def main():
    input_files = ['tests\ordinary_file.csv',
                   'tests\duplicate_lines.csv',
                   'tests\one_column_is_identical_in_some_entries.csv',
                   'tests\several_columns_are_identical_in_some_entries.csv',
                   'tests\single_entry_file.csv']

    expected_outputs = [
                        [['', '', 'SMS-+14047404524', '4/18/2016 23:56', '', 'c', ''],
                         ['', '', 'SMS-+17572354834', '4/18/2016 15:47', '', 'b', ''],
                         ['', '', 'SMS-+19099933404', '4/22/2016 22:14', '', 'a', '']],

                        [['', '', 'SMS-+14047404524', '4/18/2016 23:56', '', 'c', ''],
                         ['', '', 'SMS-+14047404524', '4/18/2016 23:56', '', 'c', ''],
                         ['', '', 'SMS-+17572354834', '4/18/2016 15:47', '', 'b', ''],
                         ['', '', 'SMS-+19099933404', '4/22/2016 22:14', '', 'a', ''],
                         ['', '', 'SMS-+19099933404', '4/22/2016 22:14', '', 'a', ''],
                         ['', '', 'SMS-+19099933404', '4/22/2016 22:14', '', 'a', ''],
                         ['', '', 'SMS-+19099933404', '4/22/2016 22:14', '', 'a', '']],

                        [['', ' ', 'SMS-+14047404524', '4/18/2016 23:58', '', 'c', ''],
                         ['', ' ', 'SMS-+14047404665', '4/18/2016 23:58', '', 'b', ''],
                         ['', ' ', 'SMS-+17572354834', '4/18/2016 15:47', '', 'a', '']],

                        [['', ' ', 'SMS-+14047404665', '4/18/2016 23:52', '', 'b', ''],
                         ['', ' ', 'SMS-+14047404665', '4/18/2016 23:58', '', 'b', ''],
                         ['', ' ', 'SMS-+17572354834', '4/18/2016 15:47', '', 'a', '']],

                        [['TBD Liquids', ' ', 'SMS-+14047404665', '4/18/2016 23:58', '13', 'Yes sorry', '9']]
    ]

    for i in range(0,len(input_files)):
        for j in range(0,len(expected_outputs)):
            if (i==j):
                if DataProcessing.sort_data(input_files[i]) == expected_outputs[j]:
                    print input_files[i], ': pass'
                else:
                    print input_files[i], ': failed'
                    break

if __name__ == "__main__":
    main()