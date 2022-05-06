print("---------------------------")
print("------------prestamo-------")
print("---------------------------")


 #input
B= int(input("ingrese su numero de deudas: "))
C= int(input("ingrese sus ingresos mensuales: "))

 #processing
if B==0 and C>945200:
     print("Puede sacar  el prestamo")
else:
    if B>0 and C<945200:
       print("no puede sacar el prestamo")
