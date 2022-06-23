from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, x):
    # Write your code here.
    k=sorted(arr)
    l=[]
    for i in range(len(k)):
        for j in range(i+1,len(k)):
            s=k[i]+k[j]
            if(s==x):
                l.append((k[i],k[j]))
            if(s>x):
                break
    return l
 
