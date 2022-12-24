import string
k = 13
p = 'usetheshiftcipherandchargehimagrand'

def encrypt(k,p):
    a = 'abcdefghijklmnopqrstuvwxyz'
    a = list(a)
    p = list(p)
    p_index = None
    for i in range (0, len(p)):
        p_index = None
        p_index = k + a.index(p[i])
        if(p_index > 25):
                p_index = p_index % 26
        print(a[p_index], end='')

encrypt(k, p)