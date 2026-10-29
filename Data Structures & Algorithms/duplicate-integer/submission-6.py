

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicFreq = set()
        for i in nums: 
            if i not in dicFreq: 
                dicFreq.add(i)
            else: 
                return True
        return False