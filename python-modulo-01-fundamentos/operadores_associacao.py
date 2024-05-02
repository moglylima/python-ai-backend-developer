curso = "Curso de Python"
frutas = ["Maçã", "Banana", "Laranja"]
saques = [1000, 800, 500]

print("Python" in curso) # True
print("python" in curso) # False
print("banana" in frutas) # False
print("Banana" in frutas) # True

print(1000 in saques) # True
print(2000 in saques) # False
print(500 not in saques) # False
print(300 not in saques) # True



