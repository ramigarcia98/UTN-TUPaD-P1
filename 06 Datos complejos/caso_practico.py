# Lista de alumnos (cada alumno es una tupla con nombre y DNI)
alumnos = [
    ("Ana Pérez", 12345678),
    ("Luis Gómez", 23456789),
    ("Ana Pérez", 12345678),  # Intentamos cargar duplicado
    ("Martín Ruiz", 34567890)
]

# Usamos un set para eliminar duplicados (basado en tuplas)
alumnos_unicos = list(set(alumnos))

# Diccionario para guardar calificaciones por DNI
calificaciones = {
    12345678: {"Matemática": 8, "Lengua": 7},
    23456789: {"Matemática": 6, "Historia": 9},
    34567890: {"Lengua": 8, "Historia": 8}
}

# Set para identificar todas las materias dictadas
materias_totales = set()

for notas in calificaciones.values():
    materias_totales.update(notas.keys())

# Mostrar resultados
print("Listado de alumnos:")
for nombre, dni in alumnos_unicos:
    print(f"- {nombre} (DNI: {dni})")

print("\nMaterias dictadas en el curso:")
for materia in materias_totales:
    print(f"- {materia}")

print("\nCalificaciones:")
for dni, notas in calificaciones.items():
    nombre = next((n for n, d in alumnos_unicos if d == dni), "Desconocido")
    print(f"{nombre} ({dni}):")
    for materia, nota in notas.items():
        print(f"  {materia}: {nota}")