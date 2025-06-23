# Cada nodo se representa como: [valor, [lista de hijos]]

# Crear nietos
nietos_hijo1 = [["Gabriel", []], ["Jose", []], ["Ana", []]]
nietos_hijo2 = [["Pedro", []], ["Silvia", []]] 
nietos_hijo3 = [["Oscar", []], ["Manuel", []], ["Carlos", []]]

# Crear hijos con sus respectivos nietos
hijo1 = ["Nora", nietos_hijo1]
hijo2 = ["Sonia", nietos_hijo2]
hijo3 = ["Hugo", nietos_hijo3]

# Crear el nodo padre con los hijos
arbol = ["Salvador", [hijo1, hijo2, hijo3]]

# Función para imprimir el árbol
def imprimir_arbol(nodo, nivel=0):
    print("  " * nivel + "- " + nodo[0]) # viñetas
    for hijo in nodo[1]:
        imprimir_arbol(hijo, nivel + 1) #recursividad

# Función para obtener el grado de un nodo por nombre
def grado_nodo(nodo, nombre):
    if nodo[0] == nombre:
        return len(nodo[1])
    for hijo in nodo[1]:
        grado = grado_nodo(hijo, nombre)
        if grado is not None:
            return grado
    return None  # Si no se encuentra el nodo

# Función para obtener el grado del árbol (máximo grado entre todos los nodos)
def grado_arbol(nodo):
    grados = [len(nodo[1])]
    for hijo in nodo[1]:
        grados.append(grado_arbol(hijo))
    return max(grados)

# Imprimir el árbol
print("Árbol:")
imprimir_arbol(arbol)

# Consultar el grado de un nodo específico
nombre_nodo = "Sonia"
grado = grado_nodo(arbol, nombre_nodo)
if grado is not None:
    print(f"\nGrado del nodo '{nombre_nodo}': {grado}")
else:
    print(f"\nNodo '{nombre_nodo}' no encontrado.")

# Consultar el grado del árbol
print(f"Grado del árbol: {grado_arbol(arbol)}")
