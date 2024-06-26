'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.
'''
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n>=k+maxPts:
            return 1

        dp=[1.0]+[0.0]*n
        maxPts_sum=1.0
        for i in range(1,n+1):
            dp[i]=maxPts_sum/maxPts
            if i<k:
                maxPts_sum+=dp[i]

            if i-maxPts>=0:
                maxPts_sum-=dp[i-maxPts]


        return sum(dp[k:])                
