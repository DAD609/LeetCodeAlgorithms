class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = -sys.maxsize - 1

        for i in range(0, len(accounts)):
            tmp = 0
            for j in range(0, len(accounts[i])):
                tmp +=  accounts[i][j]
            if (max_value<tmp):
                max_value=tmp    

        return max_value
