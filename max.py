class Solution(object):
    def longestSubarray(self, nums):
        

        max_val = max(nums)  # Step 1: Find the maximum value in the array
        longest = 0
        current = 0

        for num in nums:
            if num == max_val:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest