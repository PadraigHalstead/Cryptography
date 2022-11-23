import math

# Find gcd(a,b) Have a as bigger number
a = 1701
b = 3768

q = 0 # Number of times b divides into a 
r = 0 # Remainder of b/a
answer = 0 # Output
prev_rem = 0 

while math.trunc(a%b) != 0:
    q = math.trunc(a/b)
    r = a%b
    a = b
    b = r

print(r)