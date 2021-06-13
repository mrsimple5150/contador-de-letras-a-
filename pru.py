w = input("Ingresa una palabra con 'dos' letras 'a': ")
w = w.lower()
z = w.count("a")

if z == 2:
    print("Lo lograste a la primera")

while z <= 1 or z >= 3:
    
    print("incorrecto")
    w = input("intenta otra vez: ")
    z = w.count("a")
    if z == 2:
        print("lo lograste despues de varios intentos")

print("fin")




