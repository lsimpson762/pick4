# p4.py
#
# Python 3 program to calculate NCEL Pick 4 number distribution
#

import csv

# initialize column lists
# one for each column day and evening draws
#
col1d = [0 for i in range(10)]
col1e = [0 for i in range(10)]
col2d = [0 for i in range(10)]
col2e = [0 for i in range(10)]
col3d = [0 for i in range(10)]
col3e = [0 for i in range(10)]
col4d = [0 for i in range(10)]
col4e = [0 for i in range(10)]

def print_data(l1,l2,l3,l4,l5,l6,l7,l8):
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    return

# read the file and fill the distribution lists
def process_file(c1d,c1e,c2d,c2e,c3d,c3e,c4d,c4e):
    with open('NCELPick4.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowknt = 0
        dayknt = 0
        eveknt = 0
        for row in readCSV:
            print(row)
            print(row[0],row[1],row[2],row[3],row[4],row[5])
            if row[1] == 'D':
                dayknt += 1
                c1d[int(row[2])] += 1
                c2d[int(row[3])] += 1
                c3d[int(row[4])] += 1
                c4d[int(row[5])] += 1
            if row[1] == 'E':
                eveknt += 1
                c1e[int(row[2])] += 1
                c2e[int(row[3])] += 1
                c3e[int(row[4])] += 1
                c4e[int(row[5])] += 1
            rowknt += 1
        print ('Number of rows= ', rowknt)
        print ('Number of day drawings= ', dayknt)
        print ('Number of eve drawings= ', eveknt)
    return

#
# main program
#
print_data(col1d,col1e,col2d,col2e,col3d,col3e,col4d,col4e)
process_file(col1d,col1e,col2d,col2e,col3d,col3e,col4d,col4e)
print ('--------')
print_data(col1d,col1e,col2d,col2e,col3d,col3e,col4d,col4e)
