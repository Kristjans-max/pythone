skaitlis = int(input("Ievadi skaitli:"))

if skaitlis % 2 == 0 and skaitlis % 3 == 0:
    print("Skaitlis dalas ar 6")
elif skaitlis % 2 == 0:
    print("Skaitlis dalas ar 2")
elif skaitlis % 3 == 0:
    print("Skaitlis dalas ar 3")
else:
    print("Skaitlis ne dalas ar 2 ne ar 3")