import math

# Find gcd(a,b) Have a as bigger number
a = 1
b = 1

q = 0 # Number of times b divides into a 
r = None # Remainder of b/a
answer = 0 # Output
prev_rem = 0 

if(a or b == 1):
        r = 1
while math.trunc(a%b) != 0:
    
    q = math.trunc(a/b)
    r = a%b
    a = b
    b = r
print("GCD(",a,b,") =",r)
