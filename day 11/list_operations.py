"""
LISTS IN PYTHON
- List is an ordered, mutable collection.
- Allows duplicate elements.
- Elements can be of different data types.

WHY WE USE LISTS:
- To store multiple values in a single variable.
- Easy to update, insert, delete elements.
"""
# Why array is not used in Python?

"""
Why Array is not used in Python?

- Python is a high-level language focused on simplicity.
- Lists provide dynamic size and support multiple data types.
- Traditional arrays store only same-type elements and have fixed size.
- Python uses lists as a more flexible replacement for arrays.
- For performance and numerical operations, Python provides array module and NumPy.
"""
# Creating a List

name=["Alice", "Bob", "Charlie", "David",112,13.5,True]
print(name)
print(type(name))#Checking the type of 'name' variable
print(name[4])#Accessing element at index 4


# it is orderedso will provide the output in the same order as we have provided
# it is mutable so we can change, add or remove elements
# it allows duplicate elements
# it can store different data types

"""
Indexing in Python:

- Indexing is used to access elements by position.
- Python uses 0-based indexing.
- Positive indexing starts from left (0,1,2...)
- Negative indexing starts from right (-1,-2...)
- Works on list, tuple, string.
- Set and dictionary do not support indexing.
"""
print(name[0])  # Accessing first element using positive indexing
print(name[-1]) # Accessing last element using negative indexing
print(len(name)) # Getting the length of the list
name[1]="Eve" # Modifying element at index 1 as list is mutable
print(name) # Printing modified list

# operations on list:

"""
1. len()
print(len(name))
2.negative indexing
print(name[-2])# Accessing second last element ,it works from right side to left
3.append()
name.append("Eve")# it adds an element at the end of the list
4. extend()
name.extend(["Frank", "Grace"])# it adds multiple elements at the end of the list
5.insert()
name.insert(2,"zoe")#it adds an element at a specific index 
6. remove()
name.remove("David")# it removes the specified element from the list
7. pop()
name.pop()# it removes the last element from the list
8. clear()
name.clear()# it removes all elements from the list 
 
"""
# 1. operation len()
list_1= [1,23,45,9]
print(len(list_1))

# 2. negative indexing
print(list_1[-3])

# 3. append()
list_1.append("anshika") # assigning the element at the end  
print(list_1)

list_1.extend([1,2,5,3,7])# each element of this list will store in the list_1 when we use extend
print(list_1)

list_1.append([1,3,5])
print(list_1)

# 4.extend()
list_1.extend([12,25,36]) 
print(list_1)


# 5.insert()
list_1.insert(2,"manshi") # it will gonna insert manshi in any specific index which is 2
print(list_1)


# 6.remove()
list_1.remove("anshika") # it will gonna remove any specific element of the list 
print(list_1)


# 7.pop()
list_1.pop(2)# by default it removes the last element if no index is given ,but any index is given it will remove the element of that index 
print(list_1)
  

# 8.clear()
list_2=[1,2,3,4,5]
list_2.clear()
print(list_2)


""" all these operation of list are possible , because list is mutable  """



 
 