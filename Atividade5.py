import math

numero = float(input("Digite um número decimal: "))

# a) arredondado para cima
print(f"Arredondado para cima (ceil): {math.ceil(numero)}")

# b) arredondado para baixo
print(f"Arredondado para baixo (floor): {math.floor(numero)}")

# c) elevado ao quadrado, usando pow
print(f"Elevado ao quadrado (pow): {math.pow(numero, 2)}")