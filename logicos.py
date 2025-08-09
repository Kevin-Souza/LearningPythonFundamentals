print("Seja Bem Vindo !")
age = int(input("Digite sua idade para continuar: "))
validacao = (age >= 0) and (age <= 10)

if(validacao):
    print("Sua Idade está entre 0 a 10 anos")
else:
    print("Sua idade não está entre 0 a 10 anos")