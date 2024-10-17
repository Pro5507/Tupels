def palen(r):
    a= len(r)-1
    s= 0
    while s<a:
        if r[s]!=r[a]:
            return False
        s= s+1
        a= a-1
    return True
r= (1, 2, 3, 4, 2, 1)
if palen(r):
    print("The tupel is flip flop")
else:
    print("The tupel is not flip flop")