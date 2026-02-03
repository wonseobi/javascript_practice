Inicio

  Escribir "Ingrese el número de estudiantes"
  Leer numero_estudiantes

  Crear lista calificaciones vacía

  Para i ← 1 hasta numero_estudiantes hacer
    Repetir
      Escribir "Ingrese la calificación del estudiante ", i
      Leer calificacion
    Hasta que calificacion sea mayor o igual a 0
    y calificacion sea menor o igual a 100

    Agregar calificacion a la lista calificaciones
  Fin Para

  Inicializar aprobados ← 0
  Inicializar reprobados ← 0

  Para cada calificacion en la lista calificaciones hacer
    Si calificacion ≥ 60 entonces
      aprobados ← aprobados + 1
    Si no
      reprobados ← reprobados + 1
  Fin Para

  Calcular promedio ← suma de calificaciones / numero_estudiantes
  Obtener calificacion_maxima ← valor máximo de la lista
  Obtener calificacion_minima ← valor mínimo de la lista

  Escribir "Estudiantes aprobados:", aprobados
  Escribir "Estudiantes reprobados:", reprobados
  Escribir "Promedio del grupo:", promedio
  Escribir "Calificación más alta:", calificacion_maxima
  Escribir "Calificación más baja:", calificacion_minima

Fin
