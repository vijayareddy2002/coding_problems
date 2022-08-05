'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].'''
#----question----
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)==0 or len(intervals)==1):
                return intervals
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for interval in intervals[1:]:
            if(interval[0]<=res[-1][1]):
                res[-1][1]=max(interval[1],res[-1][1])
            else:
                res.append(interval)
        return res
