"""
Tuple in Python:

- A tuple is an ordered collection of elements.
- Tuples are immutable (cannot be changed after creation).
- Defined using round brackets ().
- Can store different data types.
- size fixed
"""
"""
Tuple supports:
- Positive indexing
- Negative indexing
"""
t=(1,2,3,4,5,6,7,8,9,10,"anshika",98.4,True)
print(t)

# Operations possible in tuple

# 1- len()
# 2- negative indexing 

# Functions of tuple 

# 1- slicing 
# 2- count()
# 3- index()

# Example of operations and functions

print(len(t))
print(t[0])
print(t[-2])
print(t[2:8])
print(t[12:0:-1])
print(t[::-1])
print(t.count(2))

tuple1=(1,2,3,4,5)
tuple2=tuple1
print(tuple1,id(tuple1))
print(tuple2,id(tuple2))
# as append is not used in tuple so changes occur in it  
list1= list(tuple1)# we can convert a tuple to a list or vise versa
print(list1)
