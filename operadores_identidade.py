a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True, pois b aponta para o mesmo objeto que a
print(a is c)      # False, pois c é um objeto diferente com o mesmo conteúdo

print(a is not c)  # True, pois a e c não são o mesmo objeto