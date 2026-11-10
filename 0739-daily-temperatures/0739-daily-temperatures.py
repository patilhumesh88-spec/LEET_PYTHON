class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        n=len(t)
        st=[n-1]
        ans=[0]*n

        for i in range (n-2,-1,-1):
            while st and t[st[-1]]<=t[i]:
                st.pop()
            if not st:
                ans[i]=0
            else:
                ans[i]=st[-1]-i
            st.append(i)
        return ans
        