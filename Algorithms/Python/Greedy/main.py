from solve import *


sistema_euro = [1, 2, 5, 10, 20, 50, 100, 200]
cambio_a_devolver = 287
cambio_2 = 561

resultado = greedy(sistema_euro, cambio_a_devolver)
print(f"Cambio para {cambio_a_devolver}: {resultado}")
print(f"Total de monedas usadas: {len(resultado)}")

resultado = greedy(sistema_euro, cambio_2)
print(f"Cambio para {cambio_2}: {resultado}")
print(f"Total de monedas usadas: {len(resultado)}")

