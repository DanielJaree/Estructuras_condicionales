peso=int(input("Digite su peso: "))
altura=float(input("Digite su altura: "))

imc=peso/altura**2

if imc<16:
    print("ingrese el hospital")
elif imc>=16 and imc<=17:
    print("infrapeso")
elif imc>17:
    print("Bajo peso")
elif imc>=17 and imc<=25:
    print("peso normal saludable")