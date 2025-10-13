import random

galvas_skaits = 0
metieni = 0

print("Mest monētu līdz būs 3 reizes pēc kārtas galva")

while galvas_skaits < 100:
    metiens = random.choice(["G", "S"])
    print("Izkrīt:", metiens)
    metieni += 1

    if metiens == "G":
        galvas_skaits += 1
    else:
        galvas_skaits = 0

print("Tas izdevās pēc", metieni, "metieniem.")