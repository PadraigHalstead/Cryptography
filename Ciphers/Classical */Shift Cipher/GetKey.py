p = 'usetheshiftcipherandchargehimagrand'
c = 'hfrgurfuvsgpvcurenaqpunetruvzntenaq'

def getKey(p,c):
    k = None
    p = list(p)
    c = list(c)
    a = 'abcdefghijklmnopqrstuvwxyz'
    if(p[0]>c[0]):
        k = a.index(p[0])-a.index(c[0])
    else:
        k = a.index(c[0])-a.index(p[0])
    print('Key =',k)



getKey(p,c)