for num in range(1,101):
    if(num % 3 == 0 and num % 5 == 0):
        print("fizzbuzz",end =" ")
    elif(num % 3 == 0):
        print("fizz",end=" ")
    elif(num % 5 == 0):
        print("buzz",end=" ")
    else:
        print(num,end=" ")
          
        # leetcode solution  
        
# for num in range(1,101):
num = int(input("Enter number : "))
if(num % 3 == 0 and num % 5 == 0):
        print("fizzbuzz")
elif(num % 3 == 0):
        print("fizz")
elif(num % 5 == 0):
        print("buzz")
else:
        print(num)
        
        
        