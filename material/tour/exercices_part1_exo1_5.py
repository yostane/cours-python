n = int(input("Saisir un entier : "))

print("pair" if n % 2 == 0 else "impair")

somme_n = 0
for i in range(n + 1):
    somme_n += i

print("Somme des", n, "premiers entiers", somme_n)
