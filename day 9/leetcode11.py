#gcd or hcf
# GCD using Euclidean Algorithm
# gcd(a, b) = gcd(b, a % b)
# We keep reducing the problem size until remainder becomes 0.
# When b becomes 0, a is the GCD.

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(56,98))
#now how it works
#gcd(56,98)
#gcd(98,56) 
#gcd(56,42)
#gcd(42,14)
#gcd(14,0)
#14

#LCM least common multiple

# we know that the product of two numbers is equal to the product of their GCD and LCM.
# i.e., a * b = GCD(a, b) * LCM(a, b)
#So, we can find LCM using the formula:
#if we want to find the LCM 
#we can do LCM(a, b) = (a * b) / GCD(a, b)
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
print(gcd(15,50))
print(lcm(15,50))