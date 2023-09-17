# crear un programa que dados una lista de alumnos y sus notas separados por
# comas y | guarde en un archivo de texto el promedio de las notas de cada
# estudiante

alumnos = [
    "Juan,98,87,89,90",
    "Jose,90,43,20,40",
    "Pedro,70,80,89,90",
    "Carlos,90,78,77,56"
]

# Función para calcular el promedio de las notas de un estudiante


def calculo_de_promedio(calificacion):
    return sum(calificacion) / len(calificacion)


# calcular el promedio e ingresar los estudiantes
promedios = {}
for alumno in alumnos:
    datos = alumno.split(',')
    nombre = datos[0]
    calificacion = list(map(int, datos[1:]))
    promedio = calculo_de_promedio(calificacion)
    promedios[nombre] = promedio

# Guardar en archivos de texto
with open("promedios.txt", "w") as archivo:
    for nombre, promedio in promedios.items():
        archivo.write(f"{nombre}={promedio:.2f}\n")

print("Los promedios se han guardado en el archivo 'promedios.txt'")
