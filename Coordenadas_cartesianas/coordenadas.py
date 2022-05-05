X = int(input("Favor ingresar coordenada en X: "))
Y = int(input("Favor ingresar coordenada en Y: "))
if((X > 0) and (Y  > 0)):
    print("punto en el primer cuadrante")

elif((X > 0) and (Y < 0)):
    print("Punto en el segundo cuadrante")

elif((X < 0) and (Y < 0)):
    print("Punto en el tercer cuadrante")

elif((X < 0) and (Y > 0)):
    print("Punto en el cuarto cuadrante")

else:
    print("Punto en el origen")