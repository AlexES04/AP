import heapq

# Clase para representar un nodo en el árbol de decisiones
class Nodo:
    def __init__(self, nivel, beneficio, peso, cota):
        self.nivel = nivel         # Índice del objeto actual
        self.beneficio = beneficio # Beneficio acumulado
        self.peso = peso           # Peso acumulado
        self.cota = cota           # Beneficio máximo potencial desde este nodo
        
    # Método mágico para que la cola de prioridad sepa cómo ordenar los nodos.
    # Usamos '<' invertido para simular un Max-Heap (ordenar de mayor a menor cota)
    def __lt__(self, otro):
        return self.cota > otro.cota 

def branch_and_bound_mochila(capacidad_max, pesos, valores):
    """
    Resuelve el problema de la mochila 0/1 usando Ramificación y Poda (Best-First).
    """
    n = len(pesos)
    
    # Función interna para calcular la Cota Superior (Bound)
    def calcular_cota(nivel, peso_actual, beneficio_actual):
        if peso_actual >= capacidad_max:
            return 0
        
        cota_beneficio = beneficio_actual
        peso_total = peso_actual
        j = nivel + 1
        
        # Llenamos la mochila con los objetos restantes mientras quepan
        while j < n and peso_total + pesos[j] <= capacidad_max:
            peso_total += pesos[j]
            cota_beneficio += valores[j]
            j += 1
            
        # Si queda espacio, tomamos una fracción del siguiente objeto (Mochila Fraccional)
        if j < n:
            espacio_restante = capacidad_max - peso_total
            cota_beneficio += valores[j] * (espacio_restante / pesos[j])
            
        return cota_beneficio

    # Cola de prioridad para explorar primero las ramas más prometedoras
    cola = []
    
    # Nodo raíz (nivel -1, antes de evaluar el primer objeto)
    nodo_raiz = Nodo(-1, 0, 0, 0)
    nodo_raiz.cota = calcular_cota(-1, 0, 0)
    heapq.heappush(cola, nodo_raiz)
    
    max_beneficio = 0
    
    while cola:
        # Extraemos el nodo con la mejor cota
        nodo_actual = heapq.heappop(cola)
        
        # PODA: Si la cota de este nodo no supera el mejor beneficio real que 
        # ya tenemos, ignoramos esta rama por completo.
        if nodo_actual.cota <= max_beneficio:
            continue
            
        nivel_sig = nodo_actual.nivel + 1
        if nivel_sig == n:
            continue
            
        # RAMIFICACIÓN 1: Incluimos el objeto siguiente
        peso_con = nodo_actual.peso + pesos[nivel_sig]
        beneficio_con = nodo_actual.beneficio + valores[nivel_sig]
        
        if peso_con <= capacidad_max and beneficio_con > max_beneficio:
            max_beneficio = beneficio_con
            
        cota_con = calcular_cota(nivel_sig, peso_con, beneficio_con)
        if cota_con > max_beneficio:
            heapq.heappush(cola, Nodo(nivel_sig, beneficio_con, peso_con, cota_con))
            
        # RAMIFICACIÓN 2: Excluimos el objeto siguiente
        cota_sin = calcular_cota(nivel_sig, nodo_actual.peso, nodo_actual.beneficio)
        if cota_sin > max_beneficio:
            heapq.heappush(cola, Nodo(nivel_sig, nodo_actual.beneficio, nodo_actual.peso, cota_sin))
            
    return max_beneficio

# --- Prueba del algoritmo ---
valores_ejemplo = [40, 50, 100, 95, 30]
pesos_ejemplo   = [2, 3.14, 1.98, 5, 3]
capacidad       = 10

mejor_resultado = branch_and_bound_mochila(capacidad, pesos_ejemplo, valores_ejemplo)
print(f"El beneficio máximo posible es: {mejor_resultado}")