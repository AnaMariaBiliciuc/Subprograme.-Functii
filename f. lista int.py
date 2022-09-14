def creare_lista() : 
    n= int(input("Nr de elemente: "))
    lista_locala=[]
    for i in range(n) :
        elem=int(input("Elementul"+str(i)+ "este: "))
        if type(elem)==int() :
            lista_locala.append(elem)
        else: 
            print("Introduceti un alt numar: ")
    return lista_locala
lista1= creare_lista()
print(lista1)

