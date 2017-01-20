import DataProcessing

def main():
    inputs = [
                # 1: no duplicates
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6565],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:33', '13', 'ok\nDaryl \nAuto Revelations', '26', 6566]],

                # 2: one duplicate
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6565],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6566],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:33', '13', 'ok\nDaryl \nAuto Revelations', '26', 6567]],

                # 3: multiple duplicates of same entry
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6565],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6566],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6567],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6568],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6569]],

                # 4: multiple different duplicates
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6566],
                 ['', '', 'SMS-+16198893530', '9/5/2014 23:19', '13', 'Took money. No water. Anyone here.', '34', 6567],
                 ['', '', 'SMS-+16198893530', '9/5/2014 23:19', '13', 'Took money. No water. Anyone here.', '34', 6568],
                 ['', '', 'SMS-+16198893530', '9/5/2014 23:19', '13', 'Took money. No water. Anyone here.', '34', 6569],
                 ['', '', 'SMS-+16198893530', '9/5/2014 23:25', '13', 'Raul fixed it.', '14', 6570]],

                # 5: only one entry and it has a duplicate
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565]],

                # 6: duplicates are not at the same time but are within legal time difference
                [['', '', 'SMS-+16198864675', '8/20/2015 23:29', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565]],

                # 7: duplicates are not at the same time and are not within legal time difference
                [['', '', 'SMS-+16198864675', '8/20/2015 23:29', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:37', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565]],

                # 8: not the same device ID
                [['', '', 'SMS-+16198864678', '8/20/2015 23:29', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565]],
    ]

    expected_outputs = [
                # no duplicates
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6565],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:33', '13', 'ok\nDaryl \nAuto Revelations', '26', 6566]],

                # one duplicae - duplicate removed
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6565],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:33', '13', 'ok\nDaryl \nAuto Revelations', '26', 6567]],

                # multiple duplicates of same entry were all removed
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6565]],

                # multiple different duplicates were removed
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:32', '13', 'ok do you know how long till they will be here?\nDaryl \nAuto Revelations', '71', 6566],
                 ['', '', 'SMS-+16198893530', '9/5/2014 23:19', '13', 'Took money. No water. Anyone here.', '34', 6567],
                 ['', '', 'SMS-+16198893530', '9/5/2014 23:25', '13', 'Raul fixed it.', '14', 6570]],

                # one entry remaining
                [['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564]],

                # earlier entry remaining
                [['', '', 'SMS-+16198864675', '8/20/2015 23:29', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564]],

                # different times are not considered duplicates, nothing is removed
                [['', '', 'SMS-+16198864675', '8/20/2015 23:29', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:37', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565]],

                # different device IDs are not considered duplicates, nothing is removed
                [['', '', 'SMS-+16198864678', '8/20/2015 23:29', '13', 'I did\nDaryl \nAuto Revelations', '29', 6564],
                 ['', '', 'SMS-+16198864675', '8/20/2015 23:31', '13', 'I did\nDaryl \nAuto Revelations', '29', 6565]]
    ]

    for i in range(0,len(inputs)):
        for j in range(0,len(expected_outputs)):
            if (i==j):
                if DataProcessing.remove_duplicates(inputs[i]) == expected_outputs[j]:
                    print i+1, ': pass'
                else:
                    print i+1, ': failed'
                    break

if __name__ == "__main__":
    main()