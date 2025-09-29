pulkstenis = 21

if pulkstenis > 21:
    print("Laiks iet gulēt.")
if pulkstenis < 21:
    print("Var vel spēlēt datoru!")
if pulkstenis == 21:

    zobi = input("Vai izmazgāji zobus?")
    dusa = input("Vai tu nomazgājies?")

    if(zobi =="Jā"):
        print("Tev jau ir tīri zobi")
    elif(zobi =="Nē"):
        print("Ej mazgāt zobus")
    else:
        print("Atbilde nav valīda")

    if(dusa =="Jā"):
        print("tu jau biji dušā")
    elif(dusa =="Nē"):
        print("Ej nomazgāties")
    else:
        print("Atbilde nav valīda")

    print("Tagad ej gulēt")