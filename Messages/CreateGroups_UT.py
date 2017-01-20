import DataProcessing

def main():
    inputs = [
                # 1: consecutive records were sent at the same time but not from the same number
                [['', '', '1', '8/20/2015 23:31', '13', 'text_a', '29', 0],
                 ['', '', '2', '8/20/2015 23:32', '13', 'text_b', '71', 1],
                 ['', '', '3', '8/20/2015 23:33', '13', 'text_c', '26', 2]],

                # 2: consecutive records were sent from the same number but not at the same time
                [['', '', '1', '8/20/2015 23:30', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:40', '13', 'text_b', '71', 1],
                 ['', '', '1', '8/20/2015 23:50', '13', 'text_c', '26', 2]],

                # 3: two valid consecutive records
                [['', '', '1', '8/20/2015 23:30', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:31', '13', 'text_b', '71', 1]],

                # 4: multiple valid consecutive records
                [['', '', '1', '8/20/2015 23:31', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:31', '13', 'text_b', '29', 1],
                 ['', '', '1', '8/20/2015 23:32', '13', 'text_c', '71', 2]],

                # 5: multiple consecutive records and multiple single records
                [['', '', '1', '8/20/2015 23:31', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:31', '13', 'text_b', '29', 1],
                 ['', '', '1', '8/20/2015 23:32', '13', 'text_c', '71', 2],
                 ['', '', '2', '8/20/2015 23:31', '13', 'text_d', '29', 3],
                 ['', '', '3', '8/20/2015 23:32', '13', 'text_e', '71', 4],
                 ['', '', '4', '8/20/2015 23:33', '13', 'text_f', '26', 5],
                 ['', '', '4', '8/20/2015 23:34', '13', 'text_g', '26', 6]]
    ]

    expected_outputs = [
                # 1: consecutive records were sent at the same time but not from the same number
                [[['', '', '1', '8/20/2015 23:31', '13', 'text_a', '29', 0]],
                 [['', '', '2', '8/20/2015 23:32', '13', 'text_b', '71', 1]],
                 [['', '', '3', '8/20/2015 23:33', '13', 'text_c', '26', 2]]],

                # 2: consecutive records were sent from the same number but not at the same time
                [[['', '', '1', '8/20/2015 23:30', '13', 'text_a', '29', 0]],
                 [['', '', '1', '8/20/2015 23:40', '13', 'text_b', '71', 1]],
                 [['', '', '1', '8/20/2015 23:50', '13', 'text_c', '26', 2]]],

                # 3: two valid consecutive records
                [[['', '', '1', '8/20/2015 23:30', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:31', '13', 'text_b', '71', 1]]],

                # 4: multiple valid consecutive records
                [[['', '', '1', '8/20/2015 23:31', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:31', '13', 'text_b', '29', 1],
                 ['', '', '1', '8/20/2015 23:32', '13', 'text_c', '71', 2]]],

                # 5: multiple consecutive records and multiple single records
                [[['', '', '1', '8/20/2015 23:31', '13', 'text_a', '29', 0],
                 ['', '', '1', '8/20/2015 23:31', '13', 'text_b', '29', 1],
                 ['', '', '1', '8/20/2015 23:32', '13', 'text_c', '71', 2]],
                 [['', '', '2', '8/20/2015 23:31', '13', 'text_d', '29', 3]],
                 [['', '', '3', '8/20/2015 23:32', '13', 'text_e', '71', 4]],
                 [['', '', '4', '8/20/2015 23:33', '13', 'text_f', '26', 5],
                 ['', '', '4', '8/20/2015 23:34', '13', 'text_g', '26', 6]]]
    ]

    for i in range(0,len(inputs)):
        for j in range(0,len(expected_outputs)):
            if (i==j):
                if DataProcessing.group_by_time_and_device(inputs[i]) == expected_outputs[j]:
                    print i+1, ': pass'
                else:
                    print i+1, ': failed'
                    break

if __name__ == "__main__":
    main()