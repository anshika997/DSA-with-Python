"""
Day 3: FizzBuzz Problem (LeetCode)

Problem:
Print numbers from 1 to n with:
- "Fizz" for multiples of 3
- "Buzz" for multiples of 5
- "FizzBuzz" for multiples of both

Approach:
- Iterate from 1 to n
- Use modulo operator to check divisibility
- Store results in a list

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
class Solution:
    def FizzBuzz(self,n:int)->List[str]:          
        ans=[]        
        for i in range(1,n+1):
            if i%3==0 and i %5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:   
                ans.append(str(i))
        return ans
obj= Solution()
n=int(input("Enter number : "))
print(obj.FizzBuzz(n))
            