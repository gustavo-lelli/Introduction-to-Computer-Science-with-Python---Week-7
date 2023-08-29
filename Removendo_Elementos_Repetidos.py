def remove_repetidos(lista):
    i=0
    recuo=0
    while(i<len(lista)-1):
        j=i+1
        while(j<len(lista)):
            print("i =", i, "j =", j)
            if(lista[i]==lista[j]):
                del lista[j]
                recuo+=1
                j-=1
            print("lista[i] =", lista[i], "lista[j] =", lista[j], end="\n\n")
            j+=1
        i+=1

    return sorted(lista)
