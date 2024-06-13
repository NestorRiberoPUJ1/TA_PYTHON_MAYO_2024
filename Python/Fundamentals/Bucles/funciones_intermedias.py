
""" Actualizar valores en diccionarios y listas"""
matriz = [[10, 15, 20], [3, 7, 14]]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6
# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"
# En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431

print("------------------------------------")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for elemento in lista:
        print(f"Nombre - {elemento['nombre']}, País - {elemento['pais']}")


iterarDiccionario(cantantes)