 def groupAnagrams():
        str = ["eat","tea","tan","ate","nat","bat"]
        endlist = []
         if (sorted(strs[0])==sorted(strs[1])):
             endlist.append(strs[0])
             endlist.append(strs[1])
         else: endlist.append(strs[0]) 
         for i in range(1,len(strs)):
             for j in range(i+1,len(strs)):  
                 stri = sorted(strs[i])
                 strj = sorted(strs[j])
                 if (stri==strj):
                     endlist.append(stri)
                     endlist.append(strj)
                 else: endlist.append(stri)   
         print(endlist)         
         return endlist     
