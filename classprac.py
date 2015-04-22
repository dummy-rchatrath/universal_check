import csv
import time

class univesral_check(getter):
    def __init__(self):
        self.name = getter
    def scan():
        ID = raw_input(
            """Please sacan your ID
            >>""")[5:11]
    def get_val():
        with open('student_room.txt') as fd:
            ALL_ENTRIES = [i.split() for i in fd]
            D = {entry[0]: {'NAME': entry[1:3], 'hall': entry[3]} for entry in ALL_ENTRIES}
        NAME = tuple(D.get(ID, {}).get('NAME'))
        HALL = D.get(ID, {}).get('hall')
        ACTUAL_HALL = int(HALL[0]) + 1500
        TIME = time.asctime(time.localtime(time.time()))
    # def write_to_csv(arg):
    #     '''Function to write to csv'''
    #     write = csv.DictWriter(fa, arg.keys())
    #     write.writeheader()
    #     write.writerow(arg)
check = univesral_check(getter)

