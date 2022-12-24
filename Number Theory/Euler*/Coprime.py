# "Two numbers are said to be relatively prime (Co-prime) 
# if they have no prime factors in common and their only common factor is 1."

# If GCD(a,b) = 1, 'a' and 'b' are relatively prime numbers.

import math

# Find gcd(a,b) Have a as bigger number
a = 727
b = 683

t = a
s = b
q = 0 # Number of times b divides into a 
r = 0 # Remainder of b/a
answer = 0 # Output
prev_rem = 0 

while math.trunc(a%b) != 0:
    q = math.trunc(a/b)
    r = a%b
    a = b
    b = r


if r == 1:
    print(t,s, "are relatively prime.")
else:
    print(t,s, "are not relatively prime.")

