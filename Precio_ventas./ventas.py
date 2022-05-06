 #input
preciocosto = float(input("El costo del articulo es: "))

 #processing

if preciocosto<3000:
    ganancia= preciocosto * 0.15
else:
    if preciocosto<=6000:
        ganancia=500
        else:
            ganancia= preciocosto * 0.25

precio_venta=preciocosto+ganancia

 #output

print(str(preciocosto) + " mas la ganancia que es " + str(ganancia) + " da " + str(precio_venta))


        
    