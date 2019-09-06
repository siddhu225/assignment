import numpy as np 
import sys
with open('/Users/siddhu/Downloads/football.dat') as file:
    start = 2
    end = 22
    skip = 19
    min_diff_team = None
    count = 0
    min_diff = sys.float_info.max
    for line in file:
        count = count + 1
        array = line.split()
        if count<=end and count>=start and count!=skip:
            forGoals = int(array[6])
            againstGoals = int(array[8])
            diff = abs(forGoals - againstGoals)
            if diff<min_diff:
                min_diff = diff
                min_diff_team = array[1]
    print('Team is ' + min_diff_team)
    print('min difference  is ' + str(min_diff))
