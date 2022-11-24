# Denoted as Φ(n)
# Φ(n) = Number of positive integers less than 'n' that are relatively prime to n
import math

n = 1
CoprimeCounter = 0

# Euclidean Algorithm
def GCD(i, n):
    r = None
    if(i == 1):
        r = 1
    while math.trunc(n%i) != 0:
        q = math.trunc(n/i)
        r = n%i
        n = i
        i = r
    return r


for i in range(1, n):
    if(GCD(i, n)) == 1:
        CoprimeCounter += 1
    else:
        continue


print("Φ(",n,") =",CoprimeCounter)