import math
def findMajorityElement(arr, n):
    for i in range(0,len(arr)):
        if(arr.count(arr[i])==math.floor(n/2)):
            return arr[i]
    return -1
print(findMajorityElement([2 ,3, 9, 2, 2],4))
