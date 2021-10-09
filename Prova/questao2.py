import numpy as np

# a. Crie dois NumPy Arrays 1-D com 4 nomes de marcas de smartphones cada;
array1 = np.array(["Nokia LG", "Apple", "Samsung", "Motorola"])
array2 = np.array(["Nokia LG", "Apple", "Samsung", "Motorola"])
print(array1)
print(array2)

# b. Em seguida, concatene-os em um só Array e ordene seus elementos;
array3 = np.concatenate((array1, array2))
array3 = np.sort(array3)
print(array3)

# c. Transforme o Array final em um Array 2-D com mais linhas do que colunas;
array4 = np.reshape(array3, (4, 2))
print(array4)

# d. Por fim, apresente quais os índices das linhas desta matriz que possuem todos os nomes contendo a letra “a” no meio deles.
res = np.char.find(array4, 'a') > 0
print(res)