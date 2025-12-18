# for num in range(1,101):
#     if(num % 3 == 0 and num % 5 == 0):
#         print("fizzbuzz",end =" ")
#     elif(num % 3 == 0):
#         print("fizz",end=" ")
#     elif(num % 5 == 0):
#         print("buzz",end=" ")
#     else:
#         print(num,end=" ")
          
#         # leetcode solution  
        
# # for num in range(1,101):
# num = int(input("Enter number : "))
# if(num % 3 == 0 and num % 5 == 0):
#         print("fizzbuzz")
# elif(num % 3 == 0):
#         print("fizz")
# elif(num % 5 == 0):
#         print("buzz")
# else:
#         print(num)

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
            