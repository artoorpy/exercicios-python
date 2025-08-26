import random
numero = random.randint(1, 100)
tentativas = 0
print("Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")
while True:
    palpite = input("Digite seu palpite (ou 'sair' para encerrar): ")
    if palpite.lower() == 'sair':
        print("Obrigado por jogar! Até a próxima.")
        break
    try:
        palpite = int(palpite)
        tentativas += 1
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue
        if palpite < numero:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero} em {tentativas} tentativas.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")