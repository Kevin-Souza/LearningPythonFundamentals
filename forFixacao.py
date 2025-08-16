'''
1 -
Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
• idade média das mulheres
• idade média dos homens
• idade média do grupo

2-
Faça um programa que solicite ao usuário um número que ele
queira treinar a tabuada. Você irá solicitar ao mesmo a resposta
do cálculo do número informado multiplicado por 1, 2 até 10.
A cada resposta você deverá validar e imprimir :”CORRETO” ou
“QUE PENA, VOCÊ ERROU, O VALOR CORRETO É X “, no lugar
de ”X“ coloque o valor correto Ao final imprima “Total de
acertos: y” e “Total de erros z”, onde “y“ deverá ser o total de
acertos e “z“ o total de erros.
'''

print("1- Média de 10 pessoas, 2- Tabuada")
option = int(input("Selecione uma opção: "))


match option:
    case 1:
        array_M = []
        array_F = []
        array_G = []
        med_M = 0
        med_F = 0

        for i in range(2):
            print("================================")
            idade = int(input("Idade: "))
            genero = str(input("Genero (M/F): "))

            if(genero.upper() == "M"):
                array_M.append(idade)
            elif(genero.upper() == "F"):
                array_F.append(idade)
            else:
                i = i-1
                continue

            array_G.append(idade)

        if(len(array_M) > 0):
            med_M = (sum(array_M)/len(array_M))
        if(len(array_F) > 0):
            med_F = (sum(array_F)/len(array_F))

        print("================================")
        print("Média da idade de Homens: ",med_M)
        print("Média da idade de Mulheres: ",med_F)
        print("Média de idade geral: ",(sum(array_G)/len(array_G)))
        print("Participaram da pesquisa:\nHomens: ",len(array_M),"\nMulheres: ",len(array_F),"\nTotal: ",len(array_G))

    case 2:
        listaAcertos = 0
        listaErros = 0
        tabuada = int(input("Digite a tabuada que deseja treinar: "))

        for i in range(11):
            resultado = int(input(f"{tabuada} X {i} = "))
            calc = tabuada * i
            if(calc == resultado):
                listaAcertos += 1
                print("CORRETO")
            else:
                listaErros += 1
                print("QUE PENA, VOCÊ ERROU, O VALOR CORRETO É",calc)
        
        print("Total de acertos:",listaAcertos)
        print("Total de erros:",listaErros)


