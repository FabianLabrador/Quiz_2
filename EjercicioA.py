def programa(valor)->int:
    if valor%2 ==0 and valor>0:
        N="EVEN POSITIVE"
    elif valor%2 ==0 and valor<0:
        N="EVEN NEGATIVE"
    elif valor%2 !=0 and valor>0:
        N="ODD POSITIVE"
    elif valor%2 !=0 and valor<0:
        N="ODD NEGATIVE"
    elif valor==0:
     N="NULL"
    return N

prueba=int(input("Ingrese casos de prueba"))

for i in range(prueba):
    valor=int(input("Ingrese datos"))
    N=programa(valor)
    print(f"{N}")


