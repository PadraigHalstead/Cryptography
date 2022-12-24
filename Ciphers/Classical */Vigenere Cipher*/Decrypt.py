import string
# Decryption Process
# P_i = (C_i - K_i mod m) mod 26

k = 'deceptivedeceptivedeceptive'
c = 'zicvtwqngrzgvtwavzhcqyglmgj'

def decrypt(k,c):
    a = list('abcdefghijklmnopqrstuvwxyz')
    p = None
    c = list(c)
    k = list(k)
    for i in range (0, len(c)):
        p_index = None
        p_index = a.index(c[i])-a.index(k[i])
        if(p_index < 0):
                p_index = p_index + 26
        print(a[p_index], end='')

decrypt(k,c)