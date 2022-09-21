x=int(input('x='))
y=int(input('y='))
z=int(input('z='))


def cel_mai_mare_div_comun(a,b,c):
    cmmdc=0
    i=min(a,b,c)
    while(i>1):
        if(a%i==0 and b%i==0 and c%i==0):
            cmmdc = i
            break
        i=i-1
    if(i<=1):
        cmmdc = "numerele nu au divizori comuni in afara de 1"
        return print(cmmdc)
    return print("cel mai mare divizor comun a",a,b,"si",c,"este:",cmmdc)

def cel_mai_mic_multiplu_comun(a,b,c):
    i=maxim(a,b,c)
    multiplu=0
    while True:
        if(i%a==0 and i%b==0 and i%c==0):
            multiplu = i
            break
        i=i+1
    return print("cel mai mic multiplu comun a",a,b,"si",c,"este:", multiplu)

def maxim(a,b,c):
    lista =[a,b,c]
    max=0
    for numar in lista:
        if numar>max:
            max = numar
    return max

def min(a,b,c):
    lista = [a,b,c]
    min = a
    for numar in lista:
        if numar<min:
            min = numar
    return min