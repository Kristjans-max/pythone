import math

print("matemātikas kalkulators")
print("Izvēlies darbību")
print("+")
print("-")
print("/")
print("sqrt")

izvele = int(input("Tava izvēle:"))

if izvele == 1:
    a = float(input("Ievadi pirmo skaitli: "))
    b = float(input("Ievadi otro skaitli"))
    print("Rezultāts:", a + b)

elif izvele == 2:
    a = float(input("Ievadi pirmo skaitli: "))
    b = float(input("Ievadi otro skaitli"))
    print("Rezultāts:", a - b)

elif izvele == 3:
    a = float(input("Ievadi pirmo skaitli: "))
    b = float(input("Ievadi otro skaitli"))
    print("Rezultāts:", a / b)

elif izvele == 4:
    a = float(input("Ievadi pirmo skaitli: "))
    if a >= 0:
     print("Rezultāts:", math.sqrt(a))
    else:
        print("xxx")

elif izvele == 5:
    a = float(input("Ievadi leņķi grādos: "))
    print("Rezultāts:", math.sin(math.radians(a)))

else:
     print("nederīga izvēle!")