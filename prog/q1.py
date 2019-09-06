import numpy as np 
import sys
with open('/Users/siddhu/Downloads/weather.dat') as file:
    start = 3
    end = 33
    min_spread_day = 1
    count = 0
    min_spread = sys.float_info.max
    for line in file:
        count=count+1
        array = line.split()
        if count<=end and count>=start:
            maxTemp =  float(''.join(array[1].split('*')))
            minTemp =  float(''.join(array[2].split('*')))
            spread = maxTemp-minTemp
            if spread < min_spread:
                min_spread_day = int(array[0])
                min_spread = spread
    print('day is ' + str(min_spread_day))
    print('min spread is ' + str(min_spread))
