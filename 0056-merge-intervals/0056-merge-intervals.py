class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged=[]
        intervals.sort(key=lambda x: x[0])
        start=intervals[0]

        for inter in intervals[1:]:
            if inter[0]<= start[1]:
                start[1]=max(start[1],inter[1])
            else:
                merged.append(start)
                start=inter
        merged.append(start)

        return merged
