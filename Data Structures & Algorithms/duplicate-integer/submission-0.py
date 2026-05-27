class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for num in nums:
            if num in new:
                return True
            new.append(num)
        return False
        