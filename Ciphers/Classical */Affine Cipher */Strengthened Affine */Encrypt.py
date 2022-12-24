from math import trunc

a = 159 # Key 1
b = 580 # Key 2
n = 26 # Alphabet size
plaintext = 'no' # Plaintext

def encrypt(a,b,n,plaintext):
    alphabet = None
    ciphertext = ''
    p = 0
    if(n == 26):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif(n == 45):
        alphabet = 'abdefghijklmnopqrstuvwxyz!£$%^&*()0123456789'
    elif(n == 122):
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    alphabet = list(alphabet)
    plaintext = list(plaintext)
   
    x = alphabet.index(plaintext[0])
    y = alphabet.index(plaintext[1])
    p = x*n + y
    n2 = n*n
    p = (a*p+b) % n2 
    x = trunc(p / n) 
    y = trunc(p % n)
    ciphertext = ciphertext + alphabet[x]
    ciphertext = ciphertext + alphabet[y]
    print(ciphertext)

encrypt(a,b,n,plaintext)