#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    res = list()
    for g in grades:
        if g < 38:
            res.append(g)
        else:
            if g % 5 == 3:
                g += 2
                res.append(g)
            elif g % 5 == 4:
                g += 1
                res.append(g)
            else:
                res.append(g)
    return res


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
