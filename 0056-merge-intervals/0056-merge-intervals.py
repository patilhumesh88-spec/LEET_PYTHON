class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals :
            return []
        intervals.sort(key=lambda x: x[0])
        res=[]
        start1=intervals[0][0]
        end1=intervals[0][1]
        for i in range (1,len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]
            if end1>=start2:
                end1=max(end1,end2)
                continue
            res.append([start1,end1])
            start1=start2
            end1=end2
        res.append([start1,end1])
        return res