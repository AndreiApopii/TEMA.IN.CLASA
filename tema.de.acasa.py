a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

def divizori_comuni(x,y,z):
    x1=[]
    y1=[]
    z1=[]
    for i in range(1,x+1):
        if (x%i==0):
            x1.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            y1.append(j)
    for l in range (1,z+1):
        if (z%l==0):
            z1.append(l)
    m=set(x1).intersection(y1)
    n=set(m).intersection(z1)
    br=list(n)
    return print('toti divizorii comuni sunt: ',br)
