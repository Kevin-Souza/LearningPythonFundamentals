for n1 in [8,7,17,25,38]:
    print(n1)
    if(n1 > 10):
        break


for n2 in [8,7,17,25,38]:
    print(n2)
else:
    print("terminou")

#range(valor_inicial, valor_final+1, step)
for n3 in range(10):
    print(n3+1)

print("Continue")
for n4 in range(10):
    if(n4 % 2 == 0):
        continue
    print(n4)