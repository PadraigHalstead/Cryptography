p = 7
q = 17
e = 5


def GenKey(p,q,e):
    n = p*q
    on = (p - 1)*(q-1)
    d= pow(e, -1, on)
    print("pubkey:",e,n, "\nprivkey:",d,n )

GenKey(p,q,e)