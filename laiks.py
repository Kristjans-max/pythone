import time

tagad = time.localtime()
stunda = tagad.tm_hour

print("Šodien ir::", time.strftime("%Y-%m-%d"))
print("Laiks: ", time.strftime("%H:%M:%S"))

if stunda <= 12:
    print("Labrīt")
elif stunda <= 18:
    print ("Labdien!")
else:
    print("Labvakar!")