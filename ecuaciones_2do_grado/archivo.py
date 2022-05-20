print("-----------------------------------------")
print("------ ECUACIONES DE SEGUNDO GRADO ------")
print("-----------------------------------------")

#input
A=float(input("Ingrese el valor de a: "))
B=float(input("Ingrese el valor de b: "))
C=float(input("Ingrese el valor de c: "))

#processing
disc=B**2-4*A*C
if disc<0:
    print("La ecuación no se puede resolver.(Dos raíces complejas)")
else:
    raiz=disc**0.5

    if disc>0:
        x1=(-B+raiz)/2*A
        x2=(-B-raiz)/2*A
        print("La solución es de dos raíces reales diferentes." + "x1= " + str(x1) + "x2= " + str(x2))
    else:
          x1=-B/2*A   
          print ("La solución es de dos raíces reales iguales, tiene una única solución: " + str(x1))