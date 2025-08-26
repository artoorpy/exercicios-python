valor_da_casa = int(input("Qual o valor da casa? "))
salario = int(input("Qual o seu salário? "))
anos = int(input("Em quantos anos você pretende pagar? "))


####logica do financiamento####
prestacao = valor_da_casa / (anos * 12)    
if prestacao > salario * 0.3:
    print("Empréstimo negado! A prestação ultrapassa 30% do seu salário.")     
else:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {prestacao:.2f}")
    print(f"Você pagará o empréstimo em {anos} anos.")