"""
     -- FUNCTIONS OF LIST --
     
1. min()
2. max()
3. count()
4. sort()
5. reverse()
6. copy()
7. index()
8. slicing
    
"""

list = [1,2,3,4,5,6,7,8,9,10,1,1]

# 1. min()
print(min(list))#finds the min. value of list 

# 2. max()
print(max(list))#finds the max. value of list 

# 3. count()
list.count(1)# it will that how many times any specific no. appears in the list

# 4. sort()
list.sort()#sort the list in acending order
print(list)

# 5. reverse()
list.reverse()
print(list)

# 6. copy()
""" 
there are two types of copy deep copy and shallow copy

"""
# this is the deep copy when all references are copied like same list with two different names 

list1=[1,2,3,4,5]
list2=list1 # deep copy 
list2.append(6)
print(list1,id(list1))
print(list2,id(list2))

# shallow copy we only need to copy the values of a list to another list 

list2=list1.copy() # 
list2.append(8)
print(list1,id(list1))
print(list2,id(list2))

# 7. index()
print(list.index(3))

# 8. slicing()
"""
slicing is like the range fuction range prints the elements present in the range
And the slicing in list print the elements which are present in between the given index   

"""
list_1= [11,22,33,44,55,66,77,88,99,100]
print(list_1[2:6])# it will print the elements present at index 2 to 5 [33,44,55,66]
print(list_1[2:8:2])# it will print the elements present at index 2 to 7 with gap of 2
print(list_1[8:1:-2])# it will print the reverse value of list_1 from index 8 to 1 with gap of -2 means start from last 2nd 
print(list_1[:5])#by default it takes 0
print(list_1[6:])#by default it tales n
print(list_1[::-1])#print the reverse of list
print(list_1[:])# print the complete list

