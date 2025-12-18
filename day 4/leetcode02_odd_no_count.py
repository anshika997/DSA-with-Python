"""
Day 4: Count Odd Numbers in a Range

Logic:
- The number of odd integers from 0 to n is given by (n + 1) // 2
- To find odd numbers between low and high (inclusive):
    1. Count odd numbers from 0 to high
    2. Count odd numbers from 0 to low - 1
    3. Subtract the two results

Formula Used:
    odd_count = (high + 1) // 2 - (low // 2)

This avoids looping and works efficiently even for very large numbers.

Time Complexity: O(1)  -> Constant time, no iteration
Space Complexity: O(1) -> No extra space used
"""
class solution:
    def countOdds(self,low:int,high:int)->int:
        return(high + 1)//2 - (low//2) 
sol = solution() # Creating an instance of the solution class
print(sol.countOdds(3,67)) # Example usage