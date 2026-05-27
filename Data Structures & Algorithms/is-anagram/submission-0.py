class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        for ch2 in s:
            count1[ch2] = count1.get(ch2, 0) + 1
        
        for ch1 in t:
            count2[ch1] = count2.get(ch1, 0) + 1

        if count1 == count2:
            return True
        else:
            return False
        