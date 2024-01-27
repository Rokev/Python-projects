#Salario de un Trabajador: Se desea obtener el salario neto de un trabajador conociendo el número de horas trabajadas, el salario hora y la tasa de impuestos que se le debe deducir.

numero_horas=int(input("ingrese el numero de horas trabajadas: "))
salario_hora=int(input("ingrese el salario que gana por hora: " ))
tasa_impuesto=int(input("ingrese la tasa de impuestos: " ))

pago_bruto=numero_horas*salario_hora
total_impuestos=(tasa_impuesto*pago_bruto)/100
pago_neto=pago_bruto-total_impuestos

print("el pago bruto es: ", pago_bruto)
print("el pago total de impuestos es: ", total_impuestos)
print("el pago neto es: ", pago_neto)



