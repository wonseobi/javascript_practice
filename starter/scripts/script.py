# Sistema de evaluación de calificaciones

# Solicitar la cantidad de estudiantes
num_estudiantes = int(input("Ingrese el número de estudiantes: "))

# Lista para almacenar las calificaciones
calificaciones = []

# Captura y validación de calificaciones
for i in range(num_estudiantes):
    while True:
        calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
        if 0 <= calificacion <= 100:
            calificaciones.append(calificacion)
            break
        else:
            print("Calificación inválida. Debe estar entre 0 y 100.")

# Cálculo de resultados
aprobados = 0
reprobados = 0

for cal in calificaciones:
    if cal >= 60:
        aprobados += 1
    else:
        reprobados += 1

promedio = sum(calificaciones) / num_estudiantes
calificacion_maxima = max(calificaciones)
calificacion_minima = min(calificaciones)

# Mostrar resultados
print("\nResultados finales:")
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
print("Promedio del grupo:", promedio)
print("Calificación más alta:", calificacion_maxima)
print("Calificación más baja:", calificacion_minima)
