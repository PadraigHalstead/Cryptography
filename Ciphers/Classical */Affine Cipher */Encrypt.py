a = 3 # Key 1
b = 11 # Key 2
n = 26 # Alphabet size
plaintext = 'hello' # Plaintext

def encrypt(a,b,n,plaintext):
    alphabet = None
    ciphertext = ''
    p = None
    if(n == 26):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif(n == 45):
        alphabet = 'abdefghijklmnopqrstuvwxyz!£$%^&*()0123456789'
    elif(n == 122):
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    alphabet = list(alphabet)
    plaintext = list(plaintext)
    for i in range (0, len(plaintext)):
        p = alphabet.index(plaintext[i])
        p = a*p + b
        p = p % n
        ciphertext = ciphertext + alphabet[p]
    print(ciphertext)

encrypt(a,b,n,plaintext)