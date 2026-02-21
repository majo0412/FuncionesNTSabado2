




def crear_lista_estudiantes(cantidadEstudiantes):
    estudiantes=[]
    for i in range(cantidadEstudiantes):
        estudiante={}
        estudiante["nombre"]=input("Ingrese el nombre del estudiante: ")
        estudiante["id"]=int(input("Ingrese la id del estudiante: "))   
        estudiante["semestre"]=int(input("Ingrese el semestre del estudiante: "))
        estudiante["promedio"]=float(input("Ingrese el promedio del estudiante: "))
        estudiante["esBecado"]=input("¿El estudiante es becado? (s/n): ")
        estudiante["documento"]=input("Ingrese el documento del estudiante: ")
        estudiante["correo"]=input("Ingrese el correo del estudiante: ")
        estudiante["telefono"]=input("Ingrese el teléfono del estudiante: ")
        estudiantes.append(estudiante)
    return estudiantes
#invocar la lista de estudiantes
crear_lista_estudiantes(5)