class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        baza = strs[0]
        for i in range(len(baza)):
            for strok in strs[1:]:
                if (i==len(strok) or baza[i]!=strok[i]):
                    return baza[0:i]
        return baza   
