class Solution:
    def fib(self, n: int) -> int:
     if n<=2:
       return n
    a = 0
    b = 1
    for i in n: 
         a=b
         b = a+b
         
      return b
