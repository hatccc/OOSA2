
from math import sqrt

for y0 in range(1, 9):
    for x0 in range(1, 9):
        for y1 in range(1, 9):
            for x1 in range(1, 9):
                if not (x0==x1 and y0==y1):
                    distance = sqrt( (x0-x1)**2 + (y0-y1)**2)
                    sentence = "Distance between (" + str(x0) + ", " + str(y0) + ") and (" + str(x1) + ", " + str(y1) + ") is " + str(distance)
                    print(sentence)
                    #print(f."Distance between ({x0}, {y0}) and ({x1}, {y1}) is {distance}")


