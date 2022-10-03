#numero = float(input("Ingrese un número: "))
#var1 = numero
#if type(numero) == str:
#    print("No Ingresó un número válido..")
#else:
#    print("Es un número válido..")
hAlarma = int(input("Ingrese hora de alarma(0 horas a 23 horas): " ))
mAlarma = int(input("Ingrese hora de alarma(00 minutos a  59 minutos): " ))
while (hAlarma<0) or (hAlarma>24):
    print("Error en ingreso de hora de alarma")
    print("Ingrese formato de hora entre 0 y 23 horas, número entero")
    hAlarma = int(input("Ingrese hora entre 0 y 23: "))
    
print("listo")
print(hAlarma)

while (hAlarma<0) or (hAlarma>60):
    print("Error en ingreso de minutos de alarma")
    print("Ingrese formato de hora entre 00 y 59 minutos, número entero")
    hAlarma = int(input("Ingrese hora entre 0 y 23: "))
print("listo")
print(mAlarma)

for horas in range(24):
    for minutos in range(59):
        print("Son las {}:{}".format(horas,minutos))
        if (horas==hAlarma) and (minutos==mAlarma):
            print("Suena la alarma!!!!!")
           
        
    

        

        