import math
t =int(input())
for i in range(t): 
    numeros=[0,1,2,3,4,5,6,7,8,9]
    Remembers= int(input())
    texto = input()
    lista =texto.split()
    lista = [int(each) for each in lista]
    for each in lista: 
        if each in numeros: 
            numeros.remove(each)
    #print(f"lista inicial {numeros} \nlista texto {lista}")
    #Posible = int((math.factorial(4)/(math.factorial(4-(10-Remembers))*math.factorial(10-Remembers))))
    #print(Posible)
    Posible = math.comb(4,10-Remembers)
    print(Posible)
    #print(len(numeros))2
