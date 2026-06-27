class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1

