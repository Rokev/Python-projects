#Un programa que sume los números ingresados por el usuario y cuando la suma sea superior a 100 deje de pedir números y muestre el total.

n=int(input('Digite un numero: '))
while n>0 and n<=99:
    n=n+int(input('Digite un numero: '))
print(n)

