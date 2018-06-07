
salario=float(input("digite seu salario:"))

if salario<= 280:
    porc=(20/100)*salario
    resultado= salario+porc

    print("seu salario antes do reajuste:R$ ", salario)
    print("percentual aumentado: %", 20)
    print("o valor do aumento é:R$ ", porc)
    print("o seu salario com o reajuste é:R$ ", resultado)

if salario > 280 and salario <=700:
    porc = (15 / 100) * salario
    resultado = salario + porc

    print("seu salario antes do reajuste:R$ ", salario)
    print("percentual aumentado: %", 15)
    print("o valor do aumento é:R$ ", porc)
    print("o seu salario com o reajuste é:R$ ", resultado)

if salario > 700 and salario <= 1500 :
        porc = (10 / 100) * salario
        resultado = salario + porc

        print("seu salario antes do reajuste:R$ ", salario)
        print("percentual aumentado: %", 10)
        print("o valor do aumento é:R$ ", porc)
        print("o seu salario com o reajuste é:R$ ", resultado)

if salario >1500:
    porc = (5 / 100) * salario
    resultado = salario + porc

    print("seu salario antes do reajuste:R$ ", salario)
    print("percentual aumentado: %", 5)
    print("o valor do aumento é:R$ ", porc)
    print("o seu salario com o reajuste é:R$ ", resultado)
