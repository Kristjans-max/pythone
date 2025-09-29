vecums = int(input("Ievadi vecumu: "))

if vecums < 13:
    print("Bērns")
elif vecums < 18:
    print("Pusaudzis")
elif vecums < 21:
    print("Legāli pieaugušais")
elif vecums < 65:
    print("Pieaugušais")
else:
    print("Seniors")