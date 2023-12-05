
print(" ")
print("Bienveido al SacaCuentas3000")
print(" ")
print("Este programa evaluara los salarios individuales y dira cuánto tine que aportar cada uno para el gasto total.")

ingreso1=int(input("Ingrese el salario 1: "))
ingreso2=int(input("Ingrese el salario 2: "))
gasto=int(input("Ingrese el gasto total: "))


totalIngresos=ingreso1+ingreso2

if (totalIngresos<gasto):
    print("Los ingresos acumulados no alcanzan a cubrir los gastos.")
else:
    porcentaje1=ingreso1*100/totalIngresos
    porcentaje2=ingreso2*100/totalIngresos
    
    aporte1=gasto*porcentaje1/100
    aporte2=gasto*porcentaje2/100

    print("Procesando...")
    print("...")
    print("...")
    print("...")


    print("La persona con ingresos de "+str(ingreso1)+" debe aportar un "+str(porcentaje1)+" del total. Equivale a: "+str(aporte1))
    print("La persona con ingresos de "+str(ingreso2)+" debe aportar un "+str(porcentaje2)+" del total. Equivale a: "+str(aporte2))