"""
Day 7 – DSA with Python
Topic: Time Complexity & Asymptotic Notation

-----------NOTE----------------------------------
THE NO. OF OPERATIONS IS THE KEY TO DETERMINE THE TIME COMPLEXITY 
--------------------------------------------------
1. Time Complexity
--------------------------------------------------
Definition:
Time Complexity is a way to measure how the execution time of an algorithm
changes with respect to the size of the input.

Purpose:
- Helps in analyzing algorithm efficiency
- Used to compare different algorithms
- Independent of machine or programming language
"""
# example 
n=10
for i in range (n) : # the time complexity of this loop is dependence on the value of n (which is the input size) and we know that the time complexity is depends on the input size 
    print(i)# n number of operations are performed here so the time complexity is O(n)
    
"""
--------------------------------------------------
2. Asymptotic Notation
--------------------------------------------------
Definition:
Asymptotic Notation is a mathematical representation used to describe the
time complexity of an algorithm for large input sizes (n → ∞).

Why we use it:
- Ignores constant values
- Focuses on growth rate
- Helps in worst-case analysis
"""

"""
--------------------------------------------------
3. Types of Time Complexity
--------------------------------------------------

a) Best Case (Ω – Omega):
Definition:
Best case represents the minimum time taken by an algorithm under ideal
conditions.

b) Average Case (Θ – Theta):
Definition:
Average case represents the expected time taken by an algorithm for normal
inputs.

c) Worst Case (O – Big O):
Definition:
Worst case represents the maximum time taken by an algorithm in the most
unfavorable conditions.

Note:
In DSA and interviews, we mostly focus on Worst Case complexity.
"""


# example

n=20
x=8
for i in range(n):
    if n>=x:
        print(i)
# Here the time complexity of all cases are :
# Best cases : O(n)
# Average cases : O(n/2)     
# Worst cases : O(n)

#------------------note----------------------------
''' we always consider the worst case because it is max time taken by algorithm to execute with respect to the size of the input '''

"""
--------------------------------------------------
4. Common Time Complexities
--------------------------------------------------

O(1)       → Constant time
O(log n)   → Logarithmic time
O(n)       → Linear time
O(n log n) → Linearithmic time
O(n²)      → Quadratic time
O(2ⁿ)      → Exponential time

Meaning:
As input size increases, the execution time increases according to the
given complexity.
"""

"""
--------------------------------------------------
5. Comparison of Time Complexities
--------------------------------------------------
Order from best to worst performance:

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

Key Point:
Lower time complexity algorithms perform better for large inputs.
"""


"""
--------------------------------------------------
6. Space Complexity
--------------------------------------------------
Definition:
Space Complexity measures the amount of memory used by an algorithm
with respect to the input size.

It includes:
- Input space
- Auxiliary (extra) space
"""

"""
--------------------------------------------------
7. Space Complexity Examples
--------------------------------------------------

O(1) Space Complexity:
- Uses constant memory
- Memory does not grow with input size

Example:
a = 10
b = 20

O(n) Space Complexity:
- Memory grows linearly with input size

Example:
Creating a list of size n

Note:
Recursive functions also use extra stack space.
"""

# example of types of time complexity

# 1. linear time complexity (it is depends on input value )

# time complexity is O(n) for all 

for i in range (n/2):
    print(i,end =" ")
    
for i in range (n+2):
    print(i,end =" ")
    
for i in range (n*2):
    print(i,end =" ")
m=7
for i in range (n-m):
    print(i,end =" ")
    
# 2.contant time complexity (independent of input value)

# independent from any input value

# the time complexity is O(1)

for i in range(10):
    print(i)

for i in range (100):
    print(i)
    
# 3. Quadratic time complexity

# time complexity is O(n^2)

for i in range(n**2):
    print(i)
    
for i in range (n):
    for j in range (n):
        print(i,j)
# here also the time complexity in n^2 because we should take the highest order term only
for i in range (n):
    for j in range (n):
        print(i,j)
for i in range (n):
    print(i)
    
# 4. Logarithmic time complexity

n= 100 
while n>0:
    print(n,end=" ")
    n//=2
    # here the time complexity is O(log n) because the value of n is reducing to half in each iteration (yb bhi iteration me n ka value aadha ho rha h ya multiply ho rha h to time complexity is log n hojata h)
    #k no. of operations are performed here
    #nx2^k=1
    #=> n=2^k
    #=> log n = k
    
# 5.others(n(logn))

for i in range (n):
    n= 100 
    while n>0:
        print(n,end=" ")
        n//=2
# here the time complexity is O(n log n) because the outer loop is O(n) and inner loop is O(log n)