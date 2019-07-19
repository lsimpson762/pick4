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
    print('Day column 1 = ',l1)
    print('Day column 2 = ',l2)
    print('Day column 3 = ',l3)
    print('Day column 4 = ',l4)
    print (' ')
    print('Eve column 1 = ',l5)
    print('Eve column 2 = ',l6)
    print('Eve column 3 = ',l7)
    print('Eve column 4 = ',l8)
    print (' ')
    print ('Day highest column 1 = ', max(l1),' index = ', l1.index(max(l1)))
    print ('Day highest column 2 = ', max(l2),' index = ', l2.index(max(l2)))
    print ('Day highest column 3 = ', max(l3),' index = ', l3.index(max(l3)))
    print ('Day highest column 4 = ', max(l4),' index = ', l4.index(max(l4)))
    print (' ')
    print ('Day lowest column 1 = ', min(l1),' index = ', l1.index(min(l1)))
    print ('Day lowest column 2 = ', min(l2),' index = ', l2.index(min(l2)))
    print ('Day lowest column 3 = ', min(l3),' index = ', l3.index(min(l3)))
    print ('Day lowest column 4 = ', min(l4),' index = ', l4.index(min(l4)))
    print (' ')
    print ('Eve highest column 1 = ', max(l5),' index = ', l5.index(max(l5)))
    print ('Eve highest column 2 = ', max(l6),' index = ', l6.index(max(l6)))
    print ('Eve highest column 3 = ', max(l7),' index = ', l7.index(max(l7)))
    print ('Eve highest column 4 = ', max(l8),' index = ', l8.index(max(l8)))
    print (' ')
    print ('Eve lowest column 1 = ', min(l5),' index = ', l5.index(min(l5)))
    print ('Eve lowest column 2 = ', min(l6),' index = ', l6.index(min(l6)))
    print ('Eve lowest column 3 = ', min(l7),' index = ', l7.index(min(l7)))
    print ('Eve lowest column 4 = ', min(l8),' index = ', l8.index(min(l8)))
    return

# read the file and fill the distribution lists
def process_file(c1d,c1e,c2d,c2e,c3d,c3e,c4d,c4e):
    with open('NCELPick4.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rowknt = 0
        dayknt = 0
        eveknt = 0
        for row in readCSV:
#            print(row)
#            print(row[0],row[1],row[2],row[3],row[4],row[5])
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
# print_data(col1d,col1e,col2d,col2e,col3d,col3e,col4d,col4e)
process_file(col1d,col1e,col2d,col2e,col3d,col3e,col4d,col4e)
print ('--------')
print_data(col1d,col2d,col3d,col4d,col1e,col2e,col3e,col4e)
