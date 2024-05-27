'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.
'''
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1
        @cache    
        def dp(a, b):
            if a <= 0 and b > 0:
                return 1.0
            if a <= 0 and b <= 0:
                return 0.5
            if a > 0 and b <= 0:
                return 0.0

            return 0.25 * (dp(a - 100, b) + dp(a - 75, b - 25) + dp(a - 50, b - 50) + dp(a - 25, b - 75))
        
        return dp(n, n)
