"""
String Key Points:
- Immutable
- Supports indexing & slicing
- Many built-in functions
- Used heavily in LeetCode problems
"""

# most common operations and functions string

# Operations

#1 len()
#2 negative indexing 
#3 upper()
#4 lower()
#5 capitalize()
#6 strip()
#7 split()

# functions

# 1.replace()
# 2.slicing
# 3.count()
# 4.startswith()
# 5.endswith()
# 6.find()
# 7.index()

name = "anshika singh"
name += " bisen " # here we add one more string in previous ,we can not modify string but can add like this 
print(name)
print(len(name))
print(name[3])
print(name*3)
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.replace("singh", "Singh"))
print(name.count("i"))
# when want to replace in the same string 
name = name.replace("bisen","BISEN")

s ="hello world"
print(s.startswith("hello"))
print(s.endswith("world"))
print(s[2:5:2])
print(list(s))
print(s.strip())# it will remove the extra spaces from starting and ending only 
#by default () it tale space" " but we can end any thing which we want here 

s1 ="hello my name is anshika"
print(s1.split(" "))
print(s1.split("a"))

list2=["a","n","s","h","i"]
s= "".join(list2)
# we want to joint all elements of any list 
print(list2)

s3="hello anshika \n how are you"

 #we can find the ascii value of any character with ord

print(ord(s))
 


