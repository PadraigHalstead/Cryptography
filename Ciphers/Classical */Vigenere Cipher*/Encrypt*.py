import string
# Encryption Process
# C_i = (P_i + k_i mod m) mod 26
# C - Ciphertext
# P - Plaintext
# K - Key
p = 'LOEUIKZWTZVPSXCRB'
k = 'SHAFISHAFISHAFISH'
p = p.lower()
k = k.lower()

def encrypt(p,k):
    a = list('abcdefghijklmnopqrstuvwxyz') 
    character = None
    p = list(p)
    k = list(k)
    for i in range (0, len(p)):
        c_index = None
        c_index = a.index(p[i])+a.index(k[i])
        if(c_index > 25):
            c_index = c_index % 26
        print(a[c_index], end='')



encrypt(p,k)