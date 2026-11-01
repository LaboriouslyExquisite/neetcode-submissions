class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. Make a dict for each word in the list
            for(strs){

            }

        2. Make a [output]

        2. Check each dictized word with every other dictized word.
            1. make a list[similiar words]
            2. If wordIDict == wordJDict:
                2. Add word to [similar]
                3. go to next word
                4. at the end of the for append [similiar] words to [Output]
        3. end whenever at end push that list to [Output]

        4. return output

        '''

        # dictList = []
        # for i in strs:
        #     strDict = {} 
        #     for j in i:
        #         if j not in strDict:
        #             strDict[j] = 1
        #         else: 
        #             strDict[j] = strDict[j] + 1
        #     dictList.append(strDict)
        #     print(strDict)

        # output = []
        # visited = set()
        # for i in range(0, len(strs)): 
        #     if strs[i] not in visited:
        #         similiar = []
        #         similiar.append(strs[i])
        #     else: 
        #         continue
        #     for j in range(i + 1, len(dictList)):
        #         if dictList[i] == dictList[j] and (strs[j] not in visited):                   
        #             similiar.append(strs[j])
        #             visited.add(strs[j])
        #             print("similiar", similiar)
                
        #     output.append(similiar)
        # print("output", output)
        # return output
        wordDict = {}
        for i in strs:
            sortedWord = str(sorted(i))
            if sortedWord not in wordDict:
                wordDict[sortedWord] = [i]
            else:
                wordDict[sortedWord].append(i) 
        output = []
        for i in wordDict: 
            output.append(wordDict[i])
        return output

            


            
            
            
            
            
            