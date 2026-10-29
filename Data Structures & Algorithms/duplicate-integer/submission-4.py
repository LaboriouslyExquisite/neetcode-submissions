

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicFreq = {}
        for i in nums: 
            if i not in dicFreq: 
                dicFreq[i] = 1
            else: 
                return True
        return False