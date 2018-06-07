l1 = int(input("Digite um lado"))
l2 = int(input("Digite um lado"))
l3 = int(input("Digite um lado"))

if l1 + l2 > l3 and l1+l3>l2 and l2+l3>l1:
    print("É um Triângulo")
    if l1 == l2== l3 ==l1:
        print('Triângulo Equilátero')
    if l1==l3!=l2:
        print('É um Triângulo Isósceles')
    if l2==l1!=l3:
        print('É um Triângulo Isósceles')
    if l3==l2!=l1:
        print('É um Triângulo Isósceles')
    if l1 != l2 != l3 != l1:
        print("Triângulo Escaleno")

else:
    print('não éum triângulo')
