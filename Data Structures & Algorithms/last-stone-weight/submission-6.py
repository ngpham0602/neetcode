class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            new_list = sorted(stones)
            if new_list[-1] == new_list[-2]:
                new_list = new_list[:-2]
                stones = new_list
            elif new_list[-2] < new_list[-1]:
                y = new_list.pop()
                x = new_list.pop()
                new_list.append(y - x)
                stones = new_list
        if len(stones) < 1:
            return 0
        else:
            return stones[0]