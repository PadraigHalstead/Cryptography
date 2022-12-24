import math
# A and N should be relatively prime to eachother

a = 10 # Any positive integer
n = 11 # Any number
CoprimeCounter = 0

# Denoted as Φ(n)
# Φ(n) = Number of positive integers less than 'n' that are relatively prime to n

#First find Φ(n)
def GCD(i, n):
    r = 0
    
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


# Check if a^Φ(n) = 1 (mod n)
verify = 1 % n

print(1 % 15) 

a = pow(a,CoprimeCounter)
a = a % n

if( a == verify):
    print("Holds true")
else:
    print("Does NOT hold true")