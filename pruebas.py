#codicional if

#cajero automatico
saldo=2000
print("1.-ingreso de dinero")
print("2.-retirar dinero")
print("3.-mostrar dinero")
print("4.-salir")
opcion=int(input("ingrese opcion solicitada: "))
if opcion <=4 and opcion >0:
    if opcion == 1:
        ingreso=float(input("cuanto dinero desea depositar: "))
        saldo += ingreso
        print(f"su saldo actual es: ${saldo:.0f}")
    elif opcion == 2:
        retiro=int(input("que cantidad desea retirar: "))
        if retiro <= saldo and retiro > 0:
            saldo -= retiro
            print(f"su saldo actual es: ${saldo:.0f}")
        else : print(f"cantidad erronea su saldo actual es: ${saldo:.0f}")
    elif opcion == 3:
        print(f"su saldo actual es: ${saldo:.0f}")
    elif opcion == 4:
        print("ok adios")
else: print("su opcion esta equivocada")