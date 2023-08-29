num=1
lista=[]
while(num!=0):
    num=int(input("Digite um número: "))
    lista.append(num)

for i in range(len(lista)-2, -1, -1):
    print(lista[i])
