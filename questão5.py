print ("CALCULADORA PYTHON")
print("A – Adição")
print("S – Subtração")
print("D – Divisão")
print("M – Multiplicação")

operação = input("Digite uma Operação:")
num1 = int(input("Digite um Numero:"))
num2 = int(input("Digite um Numero:"))

if operação == "A":
    print(num1+num2)
if operação == "a":
    print(num1+num2)

if operação == "S":
    print(num1-num2)
if operação == "s":
    print(num1 - num2)

if operação == "D":
    if num2 ==0:
        print("erro")
    if num2 !=0:
        print(num1 / num2)
if operação == "d":
        if num2 == 0:
            print("erro")
        if num2 != 0:
            print(num1 / num2)

if operação == "M":
    print(num1*num2)
if operação == "m":
    print(num1*num2)
