
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        min_len = float('inf')
        window_sum = 0
        n = len(nums)

        for high in range(n):
            window_sum += nums[high]

            while window_sum >= target:
                min_len = min(min_len, high - low + 1)
                window_sum -= nums[low]
                low += 1

        return 0 if min_len == float('inf') else min_len

        
