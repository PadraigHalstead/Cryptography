import gmpy2

c1 = input('Enter c1: ')
c2 = input('Enter c2: ')
n = input('Enter n: ')

# convert the inputs to integers
c1 = int(c1)
c2 = int(c2)
n = int(n)

# calculate gcd
gcd = gmpy2.gcd(c1, c2)

# calculate the private key
d = gmpy2.invert(gcd, n)

# print the private key
print('RSA private key is: ', d)