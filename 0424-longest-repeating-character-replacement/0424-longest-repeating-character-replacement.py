class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        max_len=0
        freq={}
        for high in range (len(s)):
            char=s[high]
            freq[char]=freq.get(char,0)+1

            max_freq=max(freq.values())

            while (high-low+1)-max_freq>k:
                freq[s[low]]-=1
                low+=1

                max_freq=max(freq.values())
            max_len=max(max_len,high-low+1)
        return max_len



        