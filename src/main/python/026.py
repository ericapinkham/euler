
import math
import fractions
import time

##Euler 26
##
# Find the value of d  1000 for which 1/d contains the
# longest recurring cycle in its decimal fraction part.

before=time.clock()

def longdiv(n):
    #computes the number of steps required to achieve remainder 1
    remainder=10
    prevremainders=[0]
    lengthofcycle=0
    while remainder not in prevremainders[:len(prevremainders)-1]:
        if n<remainder:
            m=1
            while m*n<=remainder:
                m+=1
            m-=1
            remainder-=m*n
            prevremainders.append(remainder)
        else:
            remainder*=10
    lengthofcycle=len(prevremainders)-prevremainders.index(remainder)-1
    return lengthofcycle

n=10
longestcycle=0
while n<1000:
    n+=1
    cycle=longdiv(n)
    if cycle>longestcycle:
        longestcycle=cycle
        d=n

print("1/",d, "gave the longest cycle of length ", longestcycle, " and took ", time.clock()-before, "seconds")
    


