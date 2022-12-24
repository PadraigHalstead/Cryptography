import string
k = 25
c = 'hfrgurfuvsgpvcurenaqpunetruvzntenaq'

def decrypt(k,c):
    a = 'abcdefghijklmnopqrstuvwxyz'
    a = list(a)
    c = list(c)
    c_index = None
    for i in range (0, len(c)):
        c_index = None
        c_index =  a.index(c[i]) - k
        if(c_index < 0):
                c_index = c_index + 26
        print(a[c_index], end='')

decrypt(k, c)