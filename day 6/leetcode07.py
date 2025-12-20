"""
Day 6: Kids With the Greatest Number of Candies

Problem:
Given an array representing candies each kid has and an integer extraCandies,
determine for each kid whether giving them all extraCandies makes them have
the greatest number of candies among all kids.

Approach:
- First find the maximum candies any kid currently has
- For each kid, add extraCandies to their candies
- If the total is greater than or equal to the maximum, mark True
- Otherwise, mark False
- Store results in a boolean list

Time Complexity: O(n)
- Finding the maximum takes O(n)
- Checking each kid takes O(n)

Space Complexity: O(n)
- Extra space is used for the result array
"""


from typing import List
class Solution :
    def greatestNumberCandy(self,candies:int,extraCandies:int)->List[bool]:
        result =[]
        max_candies=max(candies)
        for candy in candies:
            if candy+extraCandies>=max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
sol=Solution()
print(sol.greatestNumberCandy([2,3,5,1,3],3))