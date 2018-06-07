n1 = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
n3 = int(input("Digite um numero"))

if n1 < n2 < n3:
    print("Ordem Crescente", n1,n2,n3)
if n1 < n3 < n2:
    print("Ordem Crescente", n1, n3, n2)
if n2 < n1 < n3:
    print("Ordem Crescente", n2,n1,n3)
if n2 < n3 < n1:
    print("Ordem Crescente", n2,n3,n1)
if n3 < n1 < n2:
    print("Ordem Crescente", n3,n1,n2)
if n3 < n2 < n1:
    print("Ordem Crescente", n3,n2,n1)

if n1 > n2 > n3:
    print("Ordem Decrescente", n1,n2,n3)
if n1 > n3 > n2:
    print("Ordem Decrescente", n1, n3, n2)
if n2 > n1 > n3:
    print("Ordem Decrescente", n2,n1,n3)
if n2 > n3 > n1:
    print("Ordem Decrescente", n2,n3,n1)
if n3 > n1 > n2:
    print("Ordem Decrescente", n3,n1,n2)
if n3 > n2 > n1:
    print("Ordem Decrescente", n3,n2,n1)
