'''
Uma escola possui um sistema de Notas de 0 a 100. O aluno pode ainda faltar apenas 25% do curso. Crie um programa que leia a Nota de Prova de um aluno, a Nota de Trabalho, a Carga horária do curso e a quantidade de Horas de Faltas. A nota final do aluno é formada pela somatória da Nota de Prova que tem um peso de 80% e, a Nota de Trabalho que tem um Peso de 20%. 

Verifique se o aluno foi Aprovado ou Reprovado e exiba uma mensagem. O aluno só passa se possuir uma carga horária mínima de presença (75%) e sua Nota final seja maior ou igual a 50 pontos. 

E por fim, classifique o aluno pela Nota Final conforme a tabela abaixo e exiba sua classificação:

Nota Final <= 100 (Aluno Excelente)
Nota Final <= 75 (Aluno Ótimo)
Nota Final <= 50 (Aluno Bom)
Nota Final <= 25 (Aluno Regular)
'''



print("=======================================")
print("Sistema de média escolar")
print("=======================================")
print("Preencha as informações a seguir")
prov = float(input("Insira a nota de prova: "))
trab = float(input("Insira a nota de trabalho: "))
print("=======================================")
cargaH = float(input("Insira a carga horária do curso: "))
horaF = int(input("Insira as horas de falta do aluno: "))

calcNumerador = ((prov*0.8)+(trab*0.2))
calcDenominador = (0.8) + (0.2)
nota = (calcNumerador/calcDenominador)

pres = ((cargaH - horaF)/cargaH)*100

print("=======================================")

if(pres >= 75) and (nota >= 50):
    print("Aluno Aprovado !")
    print(f"Presença: {pres}%\nNota: {nota}")
else:
    print("Aluno Reprovado !")
    print(f"Presença: {pres}%\nNota: {nota}")


if(nota > 75 and nota <= 100):
    print("Aluno Exelente !")
elif(nota > 50 and nota <= 75):
    print("Aluno Ótimo !")
elif(nota > 25 and nota <= 50):
    print("Aluno Bom !")
else:
    print("Aluno Regular !")

