# Read a,b,n

a = 7
b = 17


def compute(a,b):
    n = a*b
    t=1
    amodn = a%n
    while b != 0:
        if(b%2 > 0):
            t=t*amodn
            b = b/2
            a = a*amodn
    print(t)

compute(a,b)
    
