menor=0
maior=0
for i in range(1,6):
    n=int(input("digite um número:"))

    if i == 1:
        menor=n
        maior=n
    elif n>maior:
        maior=n
    elif n<menor:
        menor=n

print("maior numero: ",maior)
print("menor numero: ",menor)
