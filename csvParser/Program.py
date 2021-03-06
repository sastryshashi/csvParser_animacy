'''
Author: Sastry, Shashidhar
Date created: February 16, 2019
Last change made: February 17, 2019
Version: Python 3.4.4
'''

import csv
import pprint

pp = pprint.PrettyPrinter(indent=4)

'''
Get_Word_List():
Input: id_number
Output: list of 24 words that were presented to that participant, sorted in ascending order
'''
def Get_Word_List (id_number):
    with open ('sheet.csv') as csv_file:
        word_list = set()
        csv_reader = csv.reader (csv_file, delimiter = ',')
        count = 0
        for row in csv_reader:
            if (row[0] == id_number):
                word_list.add(row[2])
                count += 1
            if (count == 24):
                break
    return list(sorted(word_list))    

#Create a blank scored_data.csv file and add the column headers
with open ('scored_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer (csv_file)
    fields = ['idnumber', 'materials', 'word', 'list1', 'list2', 'list3']
    csv_writer.writerow(fields)

#Create a blank dict.csv file that will contain all unscored data. The delimiter is ; instead of , to make retrieval easier
with open ('unscored.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')

file_prefix = 'animacy encoding beliefs RECALL exp2 '
unfound_ids = set()     #Set of ids that did not have a corresponding file
materials = {1: ['104', '113', '119', '122', '128', '131', '134', '140', '143', '146', '152', '155', '158', '161', '164', '167', '173', '176', '182', '185', '188', '191', '194', '197', '200', '203', '206', '209', '212', '215', '218', '221', '224', '227', '230', '233', '236', '239', '242', '245', '248', '251', '254', '257', '260', '263', '266', '269', '272', '275', '278', '281', '284', '287', '290', '293', '296', '299', '302', '305', '308', '311', '314', '317', '320', '323', '326', '329', '331', '333', '335', '338', '341', '344', '347', '350', '353', '356', '359', '362', '365', '368', '371', '374', '377', '380', '383', '386', '389', '392', '395', '398', '401', '404', '407', '410', '413', '416', '419', '422', '425', '428', '431', '433', '434', '437', '440', '446', '449', '452', '455', '458', '461', '464', '467', '470', '473', '476', '479', '482', '485', '488', '491', '494', '497', '500', '503', '506', '509', '512', '515'],
             2: ['102', '108', '110', '111', '114', '117', '123', '126', '129', '138', '141', '144', '147', '150', '153', '159', '162', '165', '168', '171', '174', '177', '180', '186', '189', '192', '195', '198', '201', '204', '207', '210', '213', '216', '219', '222', '225', '228', '231', '234', '237', '240', '243', '246', '249', '252', '255', '258', '261', '264', '267', '270', '273', '276', '279', '282', '285', '288', '291', '294', '297', '300', '303', '306', '309', '312', '315', '318', '321', '324', '327', '330', '336', '339', '342', '345', '348', '351', '354', '357', '360', '363', '366', '369', '372', '375', '378', '381', '384', '387', '390', '393', '396', '399', '402', '405', '408', '411', '414', '417', '420', '423', '426', '429', '432', '435', '438', '441', '444', '447', '450', '453', '456', '459', '462', '465', '468', '471', '474', '477', '480', '483', '486', '489', '492', '495', '498', '501', '504', '507', '510', '513', '516'],
             3: ['106', '109', '112', '115', '124', '127', '130', '133', '139', '142', '145', '148', '149', '151', '154', '157', '160', '163', '166', '169', '172', '175', '181', '184', '187', '190', '193', '196', '199', '202', '205', '208', '211', '214', '217', '220', '223', '226', '229', '232', '235', '238', '241', '244', '247', '250', '253', '256', '259', '262', '265', '268', '271', '274', '277', '280', '283', '286', '289', '292', '295', '298', '301', '304', '307', '310', '313', '316', '319', '322', '325', '328', '332', '334', '337', '340', '343', '346', '349', '352', '355', '358', '361', '364', '367', '370', '373', '376', '379', '382', '385', '388', '391', '394', '397', '400', '403', '406', '409', '412', '415', '418', '421', '424', '427', '430', '439', '442', '445', '448', '451', '454', '457', '460', '463', '466', '469', '472', '475', '478', '481', '484', '487', '490', '493', '496', '499', '502', '505', '508', '511', '514']}

for material_number, participant_list in materials.items():
    print ("Now searching materials with material number: " + str(material_number)) 
        
    for participant in participant_list:
        word_list = Get_Word_List (participant)
        scores_dict = dict()
        unscored_dict = {'list1': [], 'list2': [], 'list3': []}

        for word in word_list:             #Iterate through the words shown to the participant
            scores_dict [word] = [0, 0, 0] #Start by assuming that a given word was not recalled by the participant in lists 1, 2 or 3.
                                           #If the participant did recall the word, we will later change it to 1.
        try:
            with open('dataFiles/' + file_prefix + participant + '.txt') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = ',')
                for row in csv_reader:
                    item_name = row[1].lower().strip(' ')
                    list_num = row[4]
                    if (item_name in scores_dict.keys()):
                        if (list_num == 'list1'):
                            scores_dict [item_name][0] = 1
                        elif (list_num == 'list2'):
                            scores_dict [item_name][1] = 1
                        elif (list_num == 'list3'):
                            scores_dict [item_name][2] = 1
                    elif (item_name != 'finished' and item_name != 'fork' and item_name != 'spoon' and item_name != 'deer' and item_name != 'goose'):
                        unscored_dict [list_num].append(row[1]) #row[1] is used instead of item_name to preserve case
        except:
            print ('Could not find file with id: ' + participant)
            unfound_ids.add(participant)
            continue
        #Add results of the given participant in scored_data.csv
        with open ('scored_data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer (csv_file)
            for word in word_list:
                fields = [str(participant), material_number, word, scores_dict[word][0], scores_dict[word][1], scores_dict[word][2]]
                csv_writer.writerow(fields)
        #Add results of the given participant in unscored.csv
        with open ('unscored.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            fields = [participant, str(unscored_dict)]
            csv_writer.writerow(fields)

print ('\n' + '*'*75 + '\n\tFINISHED SEARCH\n' + '*'*75)

'''
Appendix code: Get ids for materials
'''
##with open ('sheet.csv') as csv_file:
##    materials1 = set()
##    csv_reader = csv.reader (csv_file, delimiter = ',')
##    first = True
##    for row in csv_reader:
##        if (first):
##            first = False
##            continue
##        elif (row[1] == '3'):
##            materials1.add(row[0])
##    print (sorted(materials1))
##    print (len(materials1))
