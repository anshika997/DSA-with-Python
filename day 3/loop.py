# day 3 
# we use loops to repeat actions multiple times
# for loops are used to iterate over a sequence (like a list, tuple, or string)
# while loops are used to repeat an action as long as a condition is true

# Example of a while loop

i = 0 
while i <5:
    # print(i)
    print(i,end=" ")  # print i on the same line with a space
    i += 1  # increment i by 1  
    
# Example of a for loop

list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i,end=" ")
    # print i on the same line with a space
    
for i in range(1 , 21):# print numbers from 1 to 20
    print(i , end ="_")
print()

for i in range (1,50,2):
    print(i , end =" ")
    # print odd numbers from 1 to 49
print()

for i in range (50,0,-1):
    print(i , end =" ")
    # print numbers from 50 to 1
print()