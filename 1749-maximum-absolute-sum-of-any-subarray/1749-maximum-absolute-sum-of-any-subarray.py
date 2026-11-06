class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxsofar=0
        minsofar=0
        currmin=0
        currmax=0
        for num in nums:
            currmax=max(currmax+num,num)
            maxsofar=max(currmax,maxsofar)
            currmin=min(currmin+num,num) 
            minsofar=min(currmin,minsofar)
        return max(maxsofar,abs(minsofar))       