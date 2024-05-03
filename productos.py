# Importo las librerias que vo a utilizar
import pandas as pd
import matplotlib.pyplot as plt

# Creo el array de objetos en donde almaceno mi productos con los precios y la cantidad disponible
productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]


# Defino una funcion llamada "stock" para realizar los calculos necesarios sobre los productos
def stock(productos):
    # Creo un bucle for para iterar sobre cada producto
    for producto in productos:
        # Multiplico el precio de cada producto con su cantidad disponible para hallar el valor total de 
        # inventario de cada producto y lo imprimo por la terminal
        valor_inventario_por_producto = producto['precio'] * producto['cantidad_disponible']
        print(f'El valor total del inventario para el producto {producto['nombre']} es: ', valor_inventario_por_producto)

    # Sumo los totales obtenidos de los inventarios por producto para sacar el total de inventario de todos 
    # los produtos y lo imprimo por la terminal
    valor_total_inventario = sum(producto['precio'] * producto['cantidad_disponible'] for producto in productos)
    print('El valor total del inventario es de: ', valor_total_inventario)

    # Simulo 3 ventas creando un array de tuplas
    ventas = [("Vestido", 2), ("Pulsera", 5), ("Bolso", 7)]

    # Creo dos bucles for para iterar sobre cada tupla y sobre los productos para poder restar la cantidad del
    # producto vendido
    for venta in ventas:
        for producto in productos:
            if producto["nombre"] == venta[0]:
                producto["cantidad_disponible"] -= venta[1]

    # Imprimo la cantidad disponible de cada producto luego de la simulacion de ventas
    print("La cantidad restante disponible de cada producto despues de las ventas es: ")
    for producto in productos:
        print(f"{producto['nombre']}: {producto['cantidad_disponible']}")

    # Creo un DataFrame con dos columnas, una para el nombre de los productos y otra para la cantidad disponible
    dataFrame = pd.DataFrame(productos, columns=["nombre", "cantidad_disponible"])
    print(dataFrame)

    # Retorno el DataFrame para su posterior uso
    return dataFrame

# Defino una funcion para mostrar el grafico
def grafico(productos):
    # LLamo al DataFrame que retorno en la funcion anterior
    dataFrame = stock(productos)

    # Obtengo el nombre y la cantidad disponible de los productos
    nombre = dataFrame['nombre']
    cantidad_disponible = dataFrame['cantidad_disponible']

    # Crear grafico
    plt.figure(figsize=(10,6))
    plt.plot(nombre, cantidad_disponible)

    # Dar un titulo e indicar el nombre de x e y al grafico
    plt.title('Cantidad disponible de productos')
    plt.xlabel('nombre')
    plt.ylabel('cantidad_disponible')

    # Mostrar el grafico
    plt.grid(True)
    plt.show()

grafico(productos)