class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        first make a dictionary where the key's are the index of the array and the value is value of that index for O(1) lookup table 

        dict{key = value at that index, value = index}
        
        Second thing once we have the lookup table we need to take target - nums[i] = [value we want]. 

        Then we search what index {key} corresponds to what value {num[j]} and we make a tuple with (num[i], num[j])
        '''

        numDic = {}
        for i in range(0, len(nums)): 
            "store {nums[i], i} 3:0"
            # if nums[i] not in numDic
            #     numsJDic[nums[i]] = i
            if (target - nums[i] in numDic):
                return [numDic[target - nums[i]], i]
            numDic[nums[i]] = i


            


        