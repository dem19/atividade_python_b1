p_sim=0

p1 = input("Telefonou para a vítima?")

if p1 == "sim":
    p_sim=p_sim + 1

p2 = input("Esteve no local do crime?")
if p2 == "sim":
    p_sim=p_sim + 1

p3 = input("Mora perto da vítima?")
if p3 == "sim":
    p_sim=p_sim + 1

p4 = input("Devia para a vítima?")
if p4 == "sim":
    p_sim=p_sim + 1

p5 = input("Já trabalhou com a vítima?")
if p5 == "sim":
    p_sim=p_sim + 1

if p_sim<= 1:
    print("Inocente")

if p_sim==2:
    print("Suspeito")

if p_sim==3 or p_sim==4:
    print("cumprice")

if p_sim==5:
    print("Assassino")
