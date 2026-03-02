# Crear matriz 5x5 (5 estudiantes x 5 materias)
calificaciones = []

# Ingreso de datos por consola
for i in range(5):
    fila = []
    print(f"\nEstudiante {i + 1}")
    for j in range(5):
        nota = float(input(f"Ingrese la calificación de la materia {j + 1}: "))
        fila.append(nota)
    calificaciones.append(fila)

# Mostrar la matriz organizada
print("\nTabla de calificaciones:")
for i in range(5):
    for j in range(5):
        print(calificaciones[i][j], end="\t")
    print()
    