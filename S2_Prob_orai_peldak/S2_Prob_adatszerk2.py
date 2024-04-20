#faktoriális vagy euklidészi algoritmus
def fakt(n):
    f=1
    if n==0:
        return(1)
    else:
        for i in range(n):   
            f*=(i+1)
        return(f)
    
print(fakt(8))

#Euklidész lelgnagyobb közös osztó

def euk(a,b):
    while a!=b:
        if b>a:
            a,b=b,a
        a= a-b
    return a

print(euk(184,12))

