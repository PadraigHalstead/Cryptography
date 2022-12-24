c = 'baxhhyeeafvarrzfvihp'
p = 'makethepassmarkfifty'

def getKey(p,c):
    a = 'abcdefghijklmnopqrstuvwxyz'
    k = 0
    key = ''
    c = list(c)
    p = list(p)
   
    for i in range (0, len(p)):
        k = (a.index(c[i]) - a.index(p[i])) % 26
        key = key + a[k]
    print(key) 

getKey(p,c)