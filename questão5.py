print ("CALCULADORA PYTHON")
print("A – Adição")
print("S – Subtração")
print("D – Divisão")
print("M – Multiplicação")

operação = input("Digite uma Operação:")
c1 = int(input("Digite um Numero:"))
c2 = int(input("Digite um Numero:"))

if operação == "A":
    print(c1+c2)
if operação == "a":
    print(c1+c2)

if operação == "S":
    print(c1-c2)
if operação == "s":
    print(c1-c2)

if operação == "D":
    if c2 ==0:
        print("erro")
    if c2 !=0:
        print(c1 / c2)
if operação == "d":
        if c2 == 0:
            print("erro")
        if c2 != 0:
            print(c1 / c2)

if operação == "M":
    print(c1*c2)
if operação == "m":
    print(c1*c2)
