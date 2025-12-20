"""
Day 6: Subtract the Sum and Product of Digits of an Integer

Problem:
Given an integer n, find the difference between the product of its digits
and the sum of its digits.

Approach:
- Store the number in a temporary variable to avoid losing the original value
- Extract each digit using modulo (% 10)
- Add the digit to the sum
- Multiply the digit with the product
- Remove the last digit using integer division (// 10)
- Return product - sum

Important Note:
- Product is initialized with 1 because multiplying by 0 would make the
  entire product 0.

Time Complexity: O(d)
Space Complexity: O(1)
(where d is the number of digits in the number)
"""
class Solution:
    def sub_productAndSum(self,n:int)->int:
        temp = n
        product=1
        addition=0
        while temp>0:
            r=temp%10
            temp//=10
            addition+=r
            product*=r
        return product - addition 
sol=Solution()
print(sol.sub_productAndSum(234))