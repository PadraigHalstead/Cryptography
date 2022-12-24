from math import trunc
a = 159 # Key 1
b = 580 # Key 2
n = 26 # Alphabet size
n2 = n*n
ciphertext = 'qy' # Ciphertext

def decrypt(a,b,n,n2,ciphertext):
    alphabet = None
    p = 0
    p1 = 0
    g = 0
    #Need python 3.8+ for this function
    ainverse = pow(a, -1, n2)
    plaintext = ''
    if(n == 26):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif(n == 45):
        alphabet = 'abdefghijklmnopqrstuvwxyz!£$%^&*()0123456789'
    elif(n == 122):
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    alphabet = list(alphabet)
    ciphertext = list(ciphertext)

    x = alphabet.index(ciphertext[0])
    y = alphabet.index(ciphertext[1])
    p = x*n + y
    print(p)
    ep = (a*p+b) % n2
    print(ep%n)
   # p = (ainverse * ep - ainverse * b) % n2
    #print(p / n2)


    x = p % n 

    #y = trunc(p % 26)
    #plaintext = plaintext + alphabet[x]
    #plaintext = plaintext + alphabet[y]
        
    if(p1 < 0):
        p1 += n
       
    
    print(plaintext)

decrypt(a,b,n,n2,ciphertext)