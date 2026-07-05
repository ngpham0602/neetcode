class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: 
            return 0
        if len(nums) < 1:
            return 1
        sorted_array = sorted(set(nums))
        max_length = 1
        current_streak = 1
        for i in range(1, len(sorted_array)):
            if sorted_array[i] == sorted_array[i-1] + 1:
                current_streak += 1
            else:
                current_streak = 1
            max_length = max(max_length, current_streak)
        return max_length