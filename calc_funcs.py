print("=======================================")
print("Calcula - Selecione uma opção")
print("=======================================")
    

options = "1- Soma -- 2- Subtração -- 3- Multiplicação -- 4- Divisão -- 5- Divisão de Inteiros -- 6- Modulo -- 7-DEMO"
print(options)
option = int(input(""))
num1 = float(input('numero1:'))
num2 = float(input('numero2:'))
result = 0


def Soma(num1F, num2F):
    return num1F + num2F

def Sub(num1F, num2F):
    return num1F - num2F

def Mult(num1F, num2F):
    return num1F * num2F

def Div(num1F, num2F):
    return num1F / num2F

def DivInt(num1F, num2F):
    return int(num1F // num2F)

def Mod(num1F, num2F):
    return num1F % num2F

def Raiz(num1F,num2F):
    return num1F ** (1/num2F)

def selectedOption():
    match(option):
        case(1):
            result = Soma(num1,num2)
            print(result)
        case(2):
            result = Sub(num1,num2)
            print(result)
        case(3):
            result = Mult(num1,num2)
            print(result)
        case(4):
            result = Div(num1,num2)
            print(result)
        case(5):
            result = DivInt(num1,num2)
            print(result)
        case(6):
            result = Mod(num1,num2)
            print(result)
        case(7):
            print('\n',"Soma: ",Soma(num1,num2),'\n',"Subtração: ",Sub(num1,num2),'\n', "Multiplicação: ",Mult(num1,num2),'\n',"Divisão: ",Div(num1,num2),'\n',"Divisão de inteiros:",DivInt(num1,num2),'\n',"Modulo: ",Mod(num1,num2),'\n',"Raiz: ",Raiz(num1,num2))
        case _:
            print("não existe essa opção")

selectedOption()
