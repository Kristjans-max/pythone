import random
pareizi = 0

print("<atemātikas Viktorīna")
for i in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    darbiba = random.choice(["+", "-"])

    if darbiba == "+":
        pareiza_atbilde = a + b
    else:
        pareiza_atbilde = a - b

    atbilde = int(input(f"Cik ir {a} {darbiba} {b}? "))
    if atbilde == pareiza_atbilde:
        print("Pareizi!")
        pareizi += 1
    else:
        print(f"Nepareizi! Pareizā atbilde ir {pareiza_atbilde}.")
    
print(f"Tu atbildēji pareizi uz {pareizi} no 5 jautājumiem")
if pareizi == 5:
    print("Malacis")