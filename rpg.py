print("Seja bem-vindo ao mundo de batalhas!!!")
print("Você está prestes a entrar em uma aventura épica.")
print("Prepare-se para enfrentar desafios e conquistar vitórias!")

#####################definição de variáveis#####################
nivel = 1
experiencia = 0
vida = 100                              
dano_arma = 15
armadura = "Armadura de Obsidiana"
monstro = "Goblin"     
vida_monstro = 100          
forca = 15

#####################interação com o usuário#####################

nome = input("Digite seu nome de guerreiro: ")
arma = input("Escolha sua arma (Espada, Machado, Arco): ")

print(f"Saudações, {nome}! Sua jornada começa agora.")
print(f"Você está no nível {nivel} com {vida} pontos de vida.")
print(f"Sua arma {arma} causa {dano_arma} pontos de dano.")
print(f"Você está vestindo uma {armadura}.")
print(f"Um {monstro} selvagem apareceu!")
print(f"O {monstro} tem {vida_monstro} pontos de vida e {forca} de força.")
print("Prepare-se para a batalha!")

#####################lógica de batalha#####################
while vida > 0 and vida_monstro > 0:
    acao = input("Você quer (A) atacar ou (D) defender? ").upper()
    
    if acao == 'A':
        vida_monstro -= dano_arma
        print(f"Você atacou o {monstro} e causou {dano_arma} pontos de dano.")
        
        if vida_monstro <= 0:
            print(f"Você derrotou o {monstro}!")
            experiencia += 50
            print(f"Você ganhou 50 pontos de experiência. Total de experiência: {experiencia}")
            break
        
        vida -= forca
        print(f"O {monstro} contra-atacou e causou {forca} pontos de dano. Sua vida agora é {vida}.")
        
    elif acao == 'D':
        vida -= forca // 2
        print(f"Você se defendeu! O {monstro} causou apenas {forca // 2} pontos de dano. Sua vida agora é {vida}.")
        
    else:
        print("Ação inválida! Tente novamente.")
    
    if vida <= 0:
        print("Você foi derrotado! Fim de jogo.")
        break