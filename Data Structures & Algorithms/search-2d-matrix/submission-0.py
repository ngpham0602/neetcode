class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for column in matrix:
            l, r = 0, len(column) - 1
            while l <= r:
                mid = (l + r) // 2
                if target > column[mid]:
                    l = mid + 1
                elif target < column[mid]:
                    r = mid - 1
                else:
                    return True
            continue
        return False