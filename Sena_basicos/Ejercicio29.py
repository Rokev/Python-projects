#Un alumno desea saber cuál será su calificación final en la materia de español, donde sus calificaciones están relacionadas con los siguientes porcentajes:
# 50% Promedio de sus (3) tres calificaciones parciales.
# 30% Examen final.
# 20% Un trabajo final.

nota1=float(input("calificacion parcial 1: "))
nota2=float(input("calificacion parcial 2: "))
nota3=float(input("calificacion parcial 3: "))
nota4=float(input("nota del examen final: " ))
nota5=float(input("nota del trabajo final: " ))

promedio_3_notas=(nota1+nota2+nota3)/3
porcentaje1=promedio_3_notas*50/100
porcentaje2=nota4*30/100
porcentaje3=nota5*20/100

suma_P=porcentaje1+porcentaje2+porcentaje3

print(porcentaje1)
print(porcentaje2)
print(porcentaje3)
print(promedio_3_notas)

print("la nota final del estudiante es: ", suma_P)
