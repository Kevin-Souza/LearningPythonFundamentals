import math
'''
1 - Dado a nota das provas P1,P2 e P3, calcular a média (aritmética) das notas do aluno

2 - Escreva um código que calcule a hipotenusa de um
triângulo retângulo, cujos catetos são a = 4 e b = 3.

3 - Solicite ao usuário o valor do salário atual (numérico com
decimais), em seguida, solicite o percentual de aumento
(numérico com decimais) e imprima o valor do salário
atualizado 

4 - Crie um programa e declare uma constante PI (use 4 casas após a vírgula). Dados o
raio e a altura, calcular e apresentar o valor do volume de uma lata de óleo, utilizando
a fórmula: volume = PI * r 2 * altura
'''

def mediaAritmetica():
    return round(((p1+p2+p3)/3),2)

print('Qual atividade você quer executar')
print('\n','1 - Média Aritmética','\n','2 - Escreva um código que calcule a hipotenusa de um triângulo retângulo','\n','3 - Imprima o valor do salário atualizado')
option = input("")

if(option == "1"):
    p1 = float(input('Nota da Prova1: '))
    p2 = float(input('Nota da Prova2: '))
    p3 = float(input('Nota da Prova3: '))
    print(f'Sua média é: {mediaAritmetica()}')
elif(option == "2"):
    a = 4
    b = 3
    hipo = math.hypot(a,b)
    print(f'A sua Hipotenusa: {hipo}')
elif(option == "3"):
    money = float(input("Informe o seu salário: "))
    percent = float(input("Informe o percentual do aumento: "))
    newValue = round((money+((percent/100) * money)),2)
    print(f'Salário atualizado para: R${newValue}')
elif(option == "4"):
    pi = 3.1415
    raio = float(input("Insira o valor do Raio: "))
    alt = float(input("Insira o valor da altura: "))
    result = (pi*(raio ** 2)*alt)
    print(f'o volume da lata é: {result}')

