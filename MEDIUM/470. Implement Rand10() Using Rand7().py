'''
Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().
rejection sampling
рисуем с помощью rand7 нужную кривую распределения а после скелим вывод на основе необходимого результата
'''


def rand7():
    import random
    return random.randint(1, 7)
class Solution:
    def rand10(self):
       while True:
        
        num = (rand7() - 1) * 7 + rand7()
         
        if num <= 40:
            return (num - 1) % 10 + 1
