# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:55:52 2024

@author: srodriguez
"""



from Crypto.PublicKey import RSA

# Generar un nuevo par de claves RSA con una longitud de 2048 bits
key = RSA.generate(2048)

# Obtener la clave privada en formato PEM
private_key = key.export_key()

# Obtener la clave pública en formato PEM
public_key = key.publickey().export_key()

# Imprimir las claves generadas
print("Clave privada RSA:")
print(private_key.decode('utf-8'))

print("\nClave pública RSA:")
print(public_key.decode('utf-8'))
