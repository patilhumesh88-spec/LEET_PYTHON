class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_best=nums[0]
        max_best=nums[0]
        res=nums[0]
        for i in range (1,len(nums)):
            v1=nums[i]
            v2=min_best*nums[i]
            v3=max_best*nums[i]

            min_best=min(v1,v2,v3)
            max_best=max(v1,v2,v3)
            res=max(res,max_best)
        return res

        