# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:48:45 2024

@author: Santiago Rodriguez

@GitHub: https://github.com/Santii-A/SeguridadInformatica.git
"""
vector_mensaje=[]
mensaje_encriptado = ""
mensaje=input("Por favor, introduce el mensaje a encriptar")
numero = int(input("Por favor, ingresa un número del 0 al 12: "))

# Verificar si el número está en el rango válido
if numero < 0 or numero > 12:
    print("El número ingresado está fuera del rango válido.")
else:
    print("El número ingresado es:", numero)

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

abecedario_numeros = {letra: indice for indice, letra in enumerate(abecedario)}


# Imprimir el vector
# print(abecedario)

# Imprimir el abecedario con sus números correspondientes
#print(abecedario_numeros)


# for letra in mensaje:
#     vector_mensaje.append(letra)
 

for letra in mensaje:
    if letra in abecedario_numeros:
        numero_correspondiente = abecedario_numeros[letra]
        numero_encriptado = (numero_correspondiente + numero) % 27  # 27 letras en el abecedario
        vector_mensaje.append(numero_encriptado)
    else:
        print("La letra", letra, "no está en el abecedario.")


for numero in vector_mensaje:
    for letra, indice in abecedario_numeros.items():
        if indice == numero:
            mensaje_encriptado += letra
            break

print("El mensaje encriptado es:", mensaje_encriptado)