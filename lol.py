import math
#1 a
suma = 0
for x in range(2, 101, 2):
    suma += x
print(suma)
#b
suma_kwadratow = 0
for x in range(1, 101):
    suma_kwadratow += x**2
print(suma_kwadratow)
#c
suma_poteg = 0
for x in range(1, 64):
    suma_poteg += 2**x
print(suma_poteg)
#d
a = int(input("Liczbe calkowita a:"))
b = int(input("Liczba calkowita b:"))
sumanieparzystych = 0
for x in range(a, b + 1):
    if x%2 != 0:
        sumanieparzystych += x
    elif a > b:
        print("0")
print(sumanieparzystych)
#2 a
c = int(input("Liczba rzeczywista:"))
sumaliczb = 0
for x in range(1, c + 1):
    d = float(input("liczba do dodania:"))
    sumaliczb += d
print(sumaliczb)
#b
m = int(input("Liczby rzeczywiste:"))
sumamnozenia = 1
for x in range(1, m + 1):
    n = float(input("Liczby do mnozenia:"))
    sumamnozenia *= n
print(sumamnozenia)
#c
l = int(input("Liczby rzeczywiste:"))
dodawanie = 0
for x in range(1, l + 1):
    k = abs(float(input("Liczba rzeczywista:")))
    dodawanie += k
print(dodawanie)
#d
p = int(input("Liczby:"))
sumapierwiastkow = 0
for x in range(1, p + 1):
    o = abs(float(input("pierw")))
    sumapierwiastkow += math.sqrt(o)
print(sumapierwiastkow)
#f
i = int(input("Liczby2"))
kwadraty = 0
for x in range(1, i + 1):
    u =float(input("liczba"))
    kwadraty += u**2
print(kwadraty)
#e
y = int(input("Liczba3"))
mnozenie = 1
for x in range(1, y + 1):
    t = abs(float(input("Liczbaok:")))
    mnozenie *= t
print(mnozenie)
