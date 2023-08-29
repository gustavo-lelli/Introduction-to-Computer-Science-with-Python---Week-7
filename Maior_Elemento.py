def maior_elemento(lista):
    maior=lista[0]
    for i in range(1, len(lista)):
        if(i>maior):
            maior=lista[i]

    return maior
