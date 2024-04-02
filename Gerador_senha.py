import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

comprimento = int(input("Digite o comprimento da senha desejada: "))

senha = " "
for i in range(comprimento):
    senha += random.choice(caracteres)

print("A senha gerada é:", senha)