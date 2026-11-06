class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        
        noDEL=arr[0]
        DEL=arr[0]
        res=arr[0]
        for i in range (1,len(arr)):
            PREVnoDEL=noDEL
            noDEL=max(arr[i],noDEL+arr[i])
            DEL=max(PREVnoDEL,DEL+arr[i])
            res=max(noDEL,DEL,res)
        return res 