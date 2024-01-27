#Informar en pantalla el promedio de cinco números.

number1= float(input("ingrese el primer numero: "))
number2=float(input("ingrese el segundo numero: "))
number3=float(input("ingrese el tercer numero: "))
number4=float(input("ingrese el cuartonumero: "))
number5=float(input("ingrese el quinto numero: "))

suma= number1+number2+number3+number4+number5
promedio= suma/5

print(f"el promedio de los numeros {number1}, {number2}, {number3}, {number4} y {number5} es ", + promedio)

