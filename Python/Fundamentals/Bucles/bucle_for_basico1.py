

""" Básico: imprime todos los números enteros del 0 al 100. """
for iterador in range(0, 101):
    print(iterador)
print("------------------------------------")
"""Múltiplos de 2: imprime todos los números múltiplos de 2 entre 2 y 500"""
for iterador in range(0, 501):
    if iterador % 2 == 0:
        print(iterador)
for iterador in range(0, 501, 2):
    print(iterador)

print("------------------------------------")
"""Contando Vanilla Ice: imprime los números enteros del 1 al 100. 
Si es divisible por 5 imprime “ice ice” en vez del número. 
Si es divisible por 10, imprime “baby”"""

for iterador in range(1, 101):
    if iterador %10 ==0:
        print("baby")
    elif iterador %5 ==0:
        print("ice ice")
    else:
        print(iterador)

print("------------------------------------")
"""Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante)."""
suma = 0
for iterador in range(0, 500001):
    if iterador % 2 == 0:
        suma += iterador
print("Sum:", suma)

suma = 0
for iterador in range(0, 500001, 2):
    suma += iterador
print("Sum:", suma)

print("------------------------------------")
"""Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3."""
for iterador in range(2024,2,-3):
    print(iterador)

print("------------------------------------")

"""Contador dinámico: establece tres variables: numInicial, numFinal y multiplo.
Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.
Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas)."""
numInicial=3
numFinal=10
multiplo=5
for iterador in range(numInicial,numFinal+1):
    if iterador % multiplo == 0:
        print(iterador)

print("------------------------------------")
