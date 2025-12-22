"""
Day 8 – DSA with Python
Topic: Introduction to Recursion

--------------------------------------------------
1. Introduction to Recursion
--------------------------------------------------
Definition:
Recursion is a programming technique in which a function calls itself
to solve a problem by breaking it into smaller subproblems.

Key Components:
- Base Case: Condition to stop recursion (prevents infinite calls(base case vo hota h jaha pe aake fuction ruk jata h bnd ho jata h))

# example of recursion
def printNum(i , n):
    i = 1
    n=10
    # Base Case
    if i > n:
        return
    print(i)
    # Recursive Case
    printNum(i + 1, n) here we call the fuction printNum itself with updated value of i (increment by 1)

- Recursive Case: Function calling itself

Note:
Without a base case, recursion can lead to infinite calls.
"""
#factorial of a number using recursion
def factorial(n):
    # Base Case
    if n==0:
        return 1
    # Recursive Case
    return n*factorial(n-1)
print(factorial(5))  # Output: 120

# NOW IT WORKS?
"""
WHEN WE CALL FACTORIAL(5)
IT CHECKS IF N==0 (BASE CASE) IT IS FALSE SO IT GOES TO RECURSIVE CASE
IT RETURNS 5*FACTORIAL(4)
NOW IT CALLS FACTORIAL(4)
IT CHECKS IF N==0 (BASE CASE) IT IS FALSE SO IT GOES TO RECURSIVE CASE
IT RETURNS 4*FACTORIAL(3)
AND SO ON UNTIL IT REACHES FACTORIAL(0)
WHEN IT REACHES FACTORIAL(0)
IT CHECKS IF N==0 (BASE CASE) IT IS TRUE SO IT RETURNS 1

(FINAL IT BECOMES LIKE THIS 5*4*3*2*1*1 = 120)

"""
"""
--------------------------------------------------
2. Loops vs Recursion
--------------------------------------------------
Loops:
- Use iteration
- Faster in most cases
- Uses constant memory
- Easier to understand for beginners

Recursion:
- Function calls itself
- Uses stack memory
- Cleaner solution for some problems
- Useful in tree, graph, and divide & conquer problems

Conclusion:
Loops are generally preferred for simple tasks,
Recursion is preferred for problems with repetitive structure.
loop is always better than recursion in terms of time and space complexity.
"""
# normal if the fun fuction is called 5 times it will print 5 4 3 2 1
def fun(n):
    if n==0:
        return 
    print(n)
    fun (n-1)
fun(5)

# but if we want to print 1 2 3 4 5 we can do this by changing the order of print and function call 
# it is n example of recursive stack

def fun(n):
    if n==0:
        return 
    fun (n-1)
    print(n)
fun(5)

# now how it works 
# when we call fun(5)
# it checks if n==0 (base case) it is false so it goes to recursive case
# it calls fun(4)
# it checks if n==0 (base case) it is false so it goes to recursive case
# it calls fun(3)
# it checks if n==0 (base case) it is false so it goes to recursive case
# it calls fun(2)
# it checks if n==0 (base case) it is false so it goes to recursive case
# it calls fun(1)
# it checks if n==0 (base case) it is false so it goes to recursive case
# it calls fun(0)
# it checks if n==0 (base case) it is true so it returns
# all the calls are popped out to the recursive stack and now it prints the values of n from 1 to 5

"""
--------------------------------------------------
5. Recursive Tree
--------------------------------------------------
Definition:
Recursive Tree is a visual representation of how recursive calls
branch and execute.

Key Points:
- Each node represents a function call
- Shows call flow clearly
- Helps in analyzing time complexity

Used in:
- Fibonacci
- Tree traversals
- Divide and Conquer algorithms
"""
# example of recursive tree (fibonacci series)
def fibonacci(n):
    # Base Case
    if n <=1:
        return n
    # Recursive Case
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(8)) # Output: 21

# now how it works
# when we call fibonacci(8)
# it checks if n<=1 (base case) it is false so it goes to recursive case
# it calls fibonacci(7) and fibonacci(6)
# and so on until it reaches fibonacci(1) and fibonacci(0)
# when it reaches fibonacci(1) and fibonacci(0)
# it checks if n<=1 (base case) it is true so it returns n  
# all the calls are popped out to the recursive stack and now it adds the values of n from fibonacci(0) to fibonacci(8)
