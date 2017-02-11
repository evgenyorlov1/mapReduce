import os
import csv

import operator

directory = 'chunks'
outputfile = 'output.csv'


def reduce():
    l = list()
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'rb') as file:
            intrm = csv.reader(file, delimiter=',')
            # os.remove(os.path.join(directory, filename))
            for key in intrm:
                l.append(key)
    output = reducelist(l)
    with open(outputfile, 'wb') as file:
        for row in output:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(row)


def reducelist(l):
    output = list()
    otp = list()
    for i in xrange(len(l)):
        temp = l[i]
        for j in xrange(i, len(l)):
            if l[i][1] == l[j][1]:
                temp[0] = int(temp[0]) + int(l[j][0])
                l[j][0] = 0
        output.append(temp)
    [otp.append(row) for row in output if row[0] != 0]
    otp = sorted(otp, reverse=True)
    return otp
