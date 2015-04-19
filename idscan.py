'''
IMSA Universal Check System Proof of Concept
'''
import time
import csv
while True:
 #get id #
    ID = raw_input(
        """Please scan your id:
        >>""")
 #Strip id # into six digit string
    ID = ID[5:11]
 #convert .txt file to dict(s)
 #List and Dictionary comprehension tools to generate list of lists of the data
 #in student_room.txt and then Dictionary comprehension
 #to convert it to a nested dictionary for a callback later.
    with open('student_room.txt') as fd:
        ALL_ENTRIES = [i.split() for i in fd]
        D = {entry[0]: {'NAME': entry[1:3], 'hall': entry[3]} for entry in ALL_ENTRIES}
 #get NAME
    NAME = tuple(D.get(ID, {}).get('NAME'))
 #get hall
    HALL = D.get(ID, {}).get('hall')
 #print hall[0] check first character of hall
    ACTUAL_HALL = int(HALL[0]) + 1500
    TIME = time.asctime(time.localtime(time.time()))
 #TIME module to get the TIME and strip it to day and local TIME
 #Create empty dictionaries to store the id #
    STUDENTS = dict((k, {}) for k in ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
 #function to write dictionary to .csv file
 #will not be needed if this is a web application
 #unless it will be used for local storage
    def write_to_csv(arg):
        '''Function to write to csv'''
        write = csv.DictWriter(fa, arg.keys())
        write.writeheader()
        write.writerow(arg)
 #Add data to dictionary and organize based on hall
    if ACTUAL_HALL == 1501:
        STUDENTS['a'][NAME] = TIME
        with open('1501.csv', 'ab') as fa:
            write_to_csv(['a'])
    if ACTUAL_HALL == 1502:
        STUDENTS['b'][NAME] = TIME
        with open('1502.csv', 'ab') as fa:
            write_to_csv(STUDENTS['b'])
    if ACTUAL_HALL == 1503:
        STUDENTS['c'][NAME] = TIME
        with open('1503.csv', 'ab') as fa:
            write_to_csv(STUDENTS['c'])
    if ACTUAL_HALL == 1504:
        STUDENTS['d'][NAME] = TIME
        with open('1504.csv', 'ab') as fa:
            write_to_csv(STUDENTS['d'])
    if ACTUAL_HALL == 1505:
        STUDENTS['e'][NAME] = TIME
        with open('1505.csv', 'ab') as fa:
            write_to_csv(STUDENTS['e'])
    if ACTUAL_HALL == 1506:
        STUDENTS['f'][NAME] = TIME
        with open('1506.csv', 'ab') as fa:
            write_to_csv(STUDENTS['f'])
    if ACTUAL_HALL == 1507:
        STUDENTS['g'][NAME] = TIME
        with open('1507.csv', 'ab') as fa:
            write_to_csv(STUDENTS['g'])


