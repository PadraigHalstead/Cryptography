a = 3 # Key 1
b = 11 # Key 2
n = 26 # Alphabet size
ciphertext = 'gxssb' # Ciphertext

def decrypt(a,b,n,ciphertext):
    alphabet = None
    p = 0
    p1 = 0
    g = 0
    #Need python 3.8+ for this function
    ainverse = pow(a, -1, n)
    plaintext = ''
    if(n == 26):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif(n == 45):
        alphabet = 'abdefghijklmnopqrstuvwxyz!£$%^&*()0123456789'
    elif(n == 122):
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    alphabet = list(alphabet)
    ciphertext = list(ciphertext)
    for i in range (0, len(ciphertext)):
       
        g = alphabet.index(ciphertext[i])
        p = ainverse * b % n
        p1 = (ainverse * g) - p
        p1 = p1 % n
        
        if(p1 < 0):
            p1 += n
       
        plaintext = plaintext + alphabet[p1]
    print(plaintext)

decrypt(a,b,n,ciphertext)