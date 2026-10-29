def dicChecker(dic: dict, s: str) -> dict:
    for i in s: 
        if i not in dic:
            dic[i] = 1
        else: 
            dic[i] = dic[i] + 1
    return dic

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        xDic = {}
        yDic = {}
        xDicChecked = dicChecker(xDic, s)
        yDicChecked = dicChecker(yDic, t)
        
        if xDicChecked == yDicChecked:
            return True
        else:
            return False
