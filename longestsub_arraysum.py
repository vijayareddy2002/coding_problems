'''Write an efficient program to find the sum of the contiguous subarray within a one-dimensional array of numbers that has the largest sum. '''
#a = [-2, -3, 4, -1, -2, 1, 5, -3]#
a=[1,2,3,-2,5]#
a=[-1,-2,-3,-4]
max1=a[0]# or max(arr)
sum2=0
for i in range(0,len(a)):
    sum2=a[i]
    for j in range(i+1,len(a)):
        sum2=sum2+a[j]
        if(max1<sum2):
            max1=sum2
print(max1)
#tried above 
#solution -kadnes algorith
def maxSubArraySum(self,arr,N):
        ans=arr[0]
        currSum=arr[0]
        for i in range(1,N):
            currSum=max(arr[i],currSum+arr[i])
            ans=max(ans,currSum)
        return ans
