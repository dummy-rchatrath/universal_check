'''
IMSA Universal Check Program by Rakesh Chatrath
'''
import csv
import time
def universal_check():
    '''Function to get info and store to doc'''
    with open('student_room.txt') as rooms:
        all_entries = [i.split() for i in rooms]
        dic = {entry[0]: {'name': entry[1:3], 'hall': entry[3]} for entry in all_entries}
    name = tuple(dic.get(ID, {}).get('name'))
    hall = dic.get(ID, {}).get('hall')
    actual_hall = int(hall[0]) + 1500
    hall_csv = ['1501.csv', '1502.csv', '1503.csv', '1504.csv', '1505.csv', '1506.csv', '1507.csv']
    students = dict((k, {}) for k in hall_csv)
    date = time.asctime(time.localtime(time.time()))
    for i in hall_csv:
        if str(actual_hall) == i[:4]:
            students[i][name] = date
            with open(i, 'ab') as record:
                write = csv.DictWriter(record, students[i].keys())
                write.writeheader()
                write.writerow(students[i])
if __name__ == "__main__":
    while True:
        ID = raw_input(
            """Please scan your ID
            >>""")[5:11]
        universal_check()







