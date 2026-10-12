import json

# 1. Preparacion de los datos
def cargar_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

data_prog = cargar_json("estudiantes_programacion.json")
data_redes = cargar_json("estudiantes_redes.json")

# Construcción de conjuntos utilizando el campo comun id
A = {est["id"] for est in data_prog}  # Estudiantes de Programación
B = {est["id"] for est in data_redes} # Estudiantes de Redes
U = set(range(100, 111))               # Universo: IDs del 100 al 110

print("--- PREPARACIÓN DE DATOS ---")
print(f"Registros archivo 1: {len(data_prog)} | Únicos en A: {len(A)}")
print(f"Registros archivo 2: {len(data_redes)} | Únicos en B: {len(B)}")
print(f"Conjunto A (Programación): {sorted(A)}")
print(f"Conjunto B (Redes): {sorted(B)}")
print(f"Universo U: {sorted(U)}\n")

# TEMA 1: Concepto de conjunto
print("--- TEMA 1 ---")
set_prog = set([101, 102, 101, 103]) 
set_prog_orden = set([103, 101, 102])
print("Set con duplicados:", set_prog)
print("¿Conservan igualdad al cambiar orden?:", set_prog == set_prog_orden)

# TEMA 2: Notación y pertenencia
print("\n--- TEMA 2 ---")
print("101 in A:", 101 in A)
print("106 not in A:", 106 not in A)

# TEMA 3: Extensión y comprensión
print("\n--- TEMA 3 ---")
extensión = {101, 102, 103, 104, 105}
comprensión = {x for x in A if x % 2 == 0} 
print("Extensión:", extensión)
print("Comprensión (IDs pares de A):", comprensión)

# TEMA 4: Conjunto vacío y universo
print("\n--- TEMA 4 ---")
vacio = set()
print("len(vacio):", len(vacio))
print("type(set()):", type(set()), "| type({}):", type({}))

# TEMA 5: Conjuntos numéricos
print("\n--- TEMA 5 ---")
print("IDs en N:", all(isinstance(x, int) and x >= 0 for x in A))
print("Limitación de float en R (0.1 + 0.2):", 0.1 + 0.2)

# TEMA 6: Subconjuntos y subconjuntos propios
print("\n--- TEMA 6 ---")
C = {x for x in A if x <= 103} 
print("C < A (Subconjunto propio):", C < A)
print("A <= A (Subconjunto):", A <= A)
print("A < A (Subconjunto propio de sí mismo):", A < A)

# TEMA 7: Igualdad y conjuntos disjuntos
print("\n--- TEMA 7 ---")
print("A == B:", A == B)
print("A.isdisjoint(B):", A.isdisjoint(B))
X = {101, 102}
Y = {106, 107}
print("X.isdisjoint(Y):", X.isdisjoint(Y))

# TEMA 8: Cardinalidad de conjuntos finitos
print("\n--- TEMA 8 ---")
print("len(A):", len(A))
print("len(B):", len(B))
print("len(A & B):", len(A & B))

# TEMA 9: Creación y modificación de conjuntos
print("\n--- TEMA 9 ---")
A_copia = A.copy()
A_copia.add(109)
print("Tras add(109):", A_copia)
A_copia.discard(109)
print("Tras discard(109):", A_copia)
A_copia.discard(999)
try:
    A_copia.remove(999)
except KeyError:
    print("remove(999) arrojó KeyError correctamente")

# TEMA 10: Elementos hashables y conjuntos inmutables
print("\n--- TEMA 10 ---")
f_a = frozenset(A)
f_b = frozenset(B)
conjunto_de_conjuntos = {f_a, f_b}
print("Conjunto con frozensets:", conjunto_de_conjuntos)

# TEMA 11: Unión
print("\n--- TEMA 11 ---")
print("A | B:", A | B)
print("Igual a A.union(B):", (A | B) == A.union(B))

# TEMA 12: Intersección
print("\n--- TEMA 12 ---")
print("A & B:", A & B)
print("Igual a A.intersection(B):", (A & B) == A.intersection(B))

# TEMA 13: Diferencia
print("\n--- TEMA 13 ---")
print("A - B:", A - B)
print("B - A:", B - A)

# TEMA 14: Diferencia simétrica
print("\n--- TEMA 14 ---")
print("A ^ B:", A ^ B)
print("Equivale a (A - B) | (B - A):", (A ^ B) == ((A - B) | (B - A)))

# TEMA 15: Complemento
print("\n--- TEMA 15 ---")
print("A <= U:", A <= U)
complemento_A = U - A
print("Complemento U - A:", complemento_A)

# TEMA 16: Propiedades de las operaciones
print("\n--- TEMA 16 ---")
C_prop = {x for x in U if x >= 105}
assert (A | B) == (B | A)   
assert ((A | B) | C_prop) == (A | (B | C_prop))  
assert (A & A) == A                      
assert (A & (B | C_prop)) == ((A & B) | (A & C_prop)) 
print("¡Todas las propiedades comprobadas exitosamente con assert!")