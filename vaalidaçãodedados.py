nome= input("Digite seu nome: ")
sexo= input("Digite seu sexo (M/F): ").upper().strip()
while sexo not in "MF":
    sexo= input("Dados inválidos. Por favor, digite seu sexo (M/F): ").upper().strip()
print(f"Nome: {nome}, Sexo: {sexo}")