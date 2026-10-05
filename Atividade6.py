import random

# a) número inteiro aleatório entre 1 e 100
numero = random.randint(1, 100)
print(f"Número sorteado entre 1 e 100: {numero}")

# b) escolher um filme aleatoriamente com choice
filmes = ["Interestelar", "Matrix", "O Poderoso Chefão", "Parasita", "Vingadores: Ultimato"]
filme_escolhido = random.choice(filmes)
print(f"Filme escolhido: {filme_escolhido}")

# c) embaralhar a lista com shuffle
random.shuffle(filmes)
print(f"Lista embaralhada: {filmes}")