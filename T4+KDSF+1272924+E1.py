'''
PENSAMIENTO COMPUTACIONAL - SECCIÓN 12
07/02/2024
Keneth David Salguero Felipe
Objetivo: Resolver movimiento rectilinio uniforme

Entrada: Vo, a, t, vf
Procesos Principales:  sumar, multiplicar y despejar
Salida: resultados del despeje
'''
print("Movimiento rectilineo uniforme")
vo = int(input("Ingrese la velocidad inicial (solo números)"))
t = int(input("Ingrese el tiempo (solo números)"))
a = int(input("Ingrese la aceleración (solo números)"))
vf = vo + (a * t)
print("La velocidad final es {}".format(vf))
