class solution:
    def countDigits(self,nums:int)->int:
        temp = nums
        count =0
        while temp>0:
            lastDigit=temp%10#it will shows the last digit of the number
            if nums%lastDigit==0:
                count+=1
            temp//=10
        return count
sol = solution()
print(sol.countDigits(121))

"""
Day 5: Digit-Based Problems (LeetCode Practice)

Problems Solved:
1) Count Digits That Divide a Number

--------------------------------------------------
Problem 1: Count Digits That Divide a Number
--------------------------------------------------
Logic:
- Store the original number since the input number will be modified
- Extract each digit using modulo (% 10)
- Check if the original number is divisible by the digit
- Increase count if divisible
- Remove the last digit using integer division (// 10)

Key Point:
- The number does not contain digit 0, so division is safe

Time Complexity: O(d)
Space Complexity: O(1)
(where d is the number of digits)
"""