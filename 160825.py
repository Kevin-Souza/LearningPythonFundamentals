print("====================================================")
print("Opções:\n1-Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor\n2-Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias:")
print("====================================================")
print("")
option = int(input("Escolha uma opção: "))

def categoriaIdade(age:int):
    if age >= 5 and age <= 7:
        print("Infantil A")
    elif age >= 8 and age <= 11:
        print("Infantil B")
    elif age >= 12 and age <= 13:
        print("Juvenil A")
    elif age >= 14 and age <= 17:
        print("Juvenil B")
    elif age >= 18 and age <= 80:
        print("Adultos")
    else:
        print("Sem Classificação")

match option:
    case 1:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        if num1 > num2:
            print(f"Maior: {num1} Menor: {num2}")
        elif num1 < num2:
            print(f"Maior: {num2} Menor: {num1}")
        else:
            print("Os numeros sao iguais!")
    case 2:
        idade = int(input("Informe a idade: "))
        categoriaIdade(idade)