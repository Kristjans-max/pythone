krasa = input("Ievadi krāsu: ")

match krasa:
    case "zaļa":
        print("Ejam uz priekšu!")
    case "sarkana":
        print("Apstājies!")
    case "dzeltena":
        print("Uzgaidi!")
    case _:
        print("Neatpazīstama krāsa!")