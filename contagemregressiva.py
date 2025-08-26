from time import sleep
a = int(input("Digite o tempo de contagem em segundos: "))
for i in range(a, -1, -1):
    sleep(1)
    print(i)
print("Feliz Ano Novo!")