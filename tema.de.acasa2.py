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

def multipli_comuni(x,y,z):
    c_m_m_m=[]
    if x>y:
        multiplu=x
    elif y>x:
        multiplu=y
    else:
        multiplu=x
    while len(c_m_m_m)<3:
        if ((multiplu%x==0)and(multiplu%y==0)):
            c_m_m_m.append(multiplu)
            multiplu=multiplu+1
        else:
            multiplu=multiplu+1
    return print('primii 3 multipli comuni sunt: ',c_m_m_m)

def triunghi(x,y,z):
    #import math#
    if (x+y>z) and (x+z>y) and (y+z>x):
        sperimetru=(x+y+z)/2
        aria=round(math.sqrt(sperimetru*(sperimetru-a)*(sperimetru-b)*(sperimetru-c)),2)
        perimetru=x+y+z
        return print('laturile pot fi ale unui triunghi,aria acestuia fiind: ',aria,"', iar perimetrul: ",perimetru)
    else:
        return print('laturile date nu pot forma un triunghi')

def ecuatie(x,y,z):
    #import math
    delta=((y**2)-(4*(x*z)))
    if delta>0:
        rad_delta=math.sqrt(int(delta))
        x1=round((-y-rad_delta)/(2*x),2)
        x2=round((-y+rad_delta)/(2*x),2)
        return print("solutiile ecuatiei sunt: ",x1,"si",x2)
    elif delta==0:
        rad_delta=math.sqrt(int(delta))
        x1=x2=round((-y)/(4*x),2)
        return print("solutiile sunt egale si valoarea lor este: ",x1)
    elif delta<0:
        return print("ecuatia nu are solutii reale dar poate avea solutii in multimea numerelor complexe!!!")
