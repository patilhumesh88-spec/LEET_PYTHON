class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[-1]*n
        st=[]
        for i in range (2*n):
            while st and nums[st[-1]]<nums[i%n]:
                res[st.pop()]=nums[i%n]
            if i<n:
                st.append(i)
        return res    