import numpy as np
import json
from datetime import datetime 

def isNum():
    while(True):
        try:
            x = int(input("ingresa una opcion: "))
            break
        except:
            print("Error, se esperaba un numero, reintente")
    return x

def menu():
    print("----------------------------------------")
    print("SERVICIO DE ATENCION MEDICA DE URGENCIAS")
    print("----------------------------------------")
    print("1.- Ingresar Ficha del Paciente")
    print("2.- Buscar ficha por Rut")
    print("3.- Buscar medicamentos por Rut")
    print("4.- Eliminar ficha del paciente")
    print("5.- Listar pacientes atendidos")
    print("6.- Salir")

# Tamaño máximo de pacientes que se pueden manejar
maximoPacientes = 50

# Crear una matriz para almacenar las fichas de pacientes
pac = np.empty((maximoPacientes, 26), dtype='object')

f = 0 # Contador de pacientes ingresados

# Intentar cargar datos existentes desde el archivo JSON
try:
    with open('pacientes.json', 'r') as paciente_json: 
        #se abrira el archivo json en modo lectura "r", 
        data = json.load(paciente_json)  # Cargar datos como una lista de listas
        #Recorrer los datos cargados y colocarlos en la matriz pac
        for i, row in enumerate(data):
            if len(row) == 26:  # Verificar que la fila tenga 24 elementos
                pac[i, :] = row
            else:
                print(f"Error: La fila {i} del archivo JSON tiene {len(row)} elementos en lugar de 24. Se omitirá esta fila.")
        f = len(data)  # Actualizar contador de pacientes ingresados
        print(f"Se han cargado {f} fichas de pacientes existentes.")
except FileNotFoundError:
    print("No se encontró el archivo 'pacientes.json'. Comenzando con lista vacía.")

while(True):
    menu()
    opt = isNum()

    if opt == 1:
        if f < maximoPacientes:  # Verificar que hay espacio para agregar más pacientes

            #con datetime obtenemos la fecha y hora actual
            fechaHora = datetime.now()
            fecha_actual = fechaHora.date()
            hora_actual = fechaHora.time().strftime('%H:%M:%S')

            print(f"Fecha ingreso: {fecha_actual}")
            print(f"Hora ingreso: {hora_actual}")

            #Almacenar la fecha y hora en la matriz pac
            pac[f, 19] = str(fecha_actual)
            pac[f, 20] = str(hora_actual)

            #Ingresar los datos del paciente en la matriz pac
            for i in range(26):
                if i == 0:
                    print("Ingrese nombre del paciente")
                    pac[f, i] = input()
                if i == 1:
                    print("Ingrese apellido del paciente")
                    pac[f, i] = input()
                if i == 2:
                    print("Ingrese rut del paciente")
                    pac[f, i] = input()
                if i == 3:
                    print("Ingrese estado civil del paciente")
                    pac[f, i] = input()
                if i == 4:
                    print("Ingrese domicilio del paciente")
                    pac[f, i] = input()
                if i == 5:
                    print("Ingrese telefono del paciente")
                    pac[f, i] = input()
                if i == 6:
                    print("Ingrese sexo del paciente")
                    pac[f, i] = input()
                if i == 7:
                    print("Ingrese edad del paciente")
                    pac[f, i] = input()
                if i == 8:
                    print("Ingrese nivel de urgencia del paciente")
                    print("Bajo, Medio, Alto.")
                    pac[f, i] = input()
                if i == 9:
                    print("diagnostico")
                    pac[f, i] = input()

                
                if i == 10:
                    print("medicamentos recetados")
                    pac[f, i] = input()
                if i == 11:
                    print("nombre del medico que receto los medicamentos")
                    print("1.- Doc. Miguel")
                    print("2.- Doc. Daniel")

                    nombre_medico = int(input())
                    if nombre_medico == 1:
                        pac[f, i] = 'Doc. Miguel Carrasco'
                        pac[f, 12] = '12.345.678-9'
                        pac[f, 13] = 'Lunes a Viernes 8am a 17:00'
                        pac[f, 14] = 'Medico General'
                        pac[f, 15] = 'U. De Chile'
                        pac[f, 16] = '2002'
                        pac[f, 17] = '987654321'
                        pac[f, 18] = 'Stgo, Centro #4353'
                    
                    elif nombre_medico == 2:
                        pac[f, i] = 'Doc. Daniel Veserra'
                        pac[f, 12] = '11.543.678-9'
                        pac[f, 13] = 'Lunes a Viernes 8am a 17:00'
                        pac[f, 14] = 'Medico General y cirujano'
                        pac[f, 15] = 'U. De Chile'
                        pac[f, 16] = '1999'
                        pac[f, 17] = '982757521'
                        pac[f, 18] = 'Stgo, Centro #56756'

                elif i == 21:  # Inicio de datos del acompañante
                    print("Viene con acompañante. Si / No")
                    tiene_acompanante = input().lower()
                    if tiene_acompanante == 'si':
                        print("Ingrese nombre del acompañante")
                        pac[f, i] = input()
                        print("Ingrese apellido del acompañante")
                        pac[f, i + 1] = input()
                        print("Ingrese rut del acompañante")
                        pac[f, i + 2] = input()
                        print("Ingrese teléfono del acompañante")
                        pac[f, i + 3] = input()
                        print("Ingrese parentesco del acompañante")
                        pac[f, i + 4] = input()
                    else:
                        print("No viene con acompañante.")
                        pac[f, i] = "No"
                        pac[f, i + 1] = ""
                        pac[f, i + 2] = ""
                        pac[f, i + 3] = ""
                        pac[f, i + 4] = ""
            
            f += 1
        else:
            print("No hay suficiente espacio para agregar más pacientes.")

    elif opt == 2:
        print("Ingrese el RUT del paciente a buscar:")
        rut_buscar = input()

        encontrado = False
        for i in range(f):
            if pac[i, 2] == rut_buscar:
                print("----------------------------------------")
                print( "FICHA ENCONTRADA")
                print("----------------------------------------")
                print(f"Fecha ingreso: {pac[i, 19]}")
                print(f"Hora ingreso: {pac[i, 20]}")
                print(f"Nombre completo: {pac[i, 0]} {pac[i, 1]}")
                print(f"RUT: {pac[i, 2]}")
                print(f"Estado civil: {pac[i, 3]}")
                print(f"Domicilio: {pac[i, 4]}")
                print(f"Teléfono: {pac[i, 5]}")
                print(f"Sexo: {pac[i, 6]}")
                print(f"Edad: {pac[i, 7]}")
                print(f"Nivel de urgencia: {pac[i, 8]}")
                print(f"Diagnóstico: {pac[i, 9]}")
                print(f"Medicamentos recetados: {pac[i, 10]}")
                print("-----------------------------------------")
                print("DATOS DEL MEDICO DE TURNO")
                print("----------------------------------------")
                print(f"Nombre completo: {pac[i, 11]}")
                print(f"RUT: {pac[i, 12]}")
                print(f"Horario de atencion: {pac[i, 13]}")
                print(f"Titulo: {pac[i, 14]}")
                print(f"Universidad: {pac[i, 15]}")
                print(f"Año Egreso: {pac[i, 16]}")
                print(f"Telefono: {pac[i, 17]}")
                print(f"Direccion: {pac[i, 18]}")
                print("-----------------------------------------")
                if pac[i, 21] == "No":
                    print("No viene con acompañante")
                else:
                    print("----------------------------------------") 
                    print("DATOS DEL ACOMPAÑANTE")
                    print("----------------------------------------")
                    print(f"Nombre completo: {pac[i, 21]} {pac[i, 22]}")
                    print(f"Rut: {pac[i, 23]}")
                    print(f"Telefono: {pac[i, 24]}")
                    print(f"Parentesco: {pac[i, 25]}")

                encontrado = True
                break

        if not encontrado:
            print("No se encontró ningún paciente con el RUT ingresado.")

    elif opt == 3:
        print("Ingrese el RUT del paciente a buscar:")
        rut_buscar = input()
        encontrado = False

        for i in range(f):
            if pac[i, 2] == rut_buscar:
                print("MEDICAMENTOS ENCONTRADOS")
                print("----------------------------------------")
                print(f"medicamentos recetados para el paciente son: {pac[i, 10]}")
                encontrado = True
                break
            
        if not encontrado:
            print("No se encontró ningún paciente con el RUT ingresado.")

    elif opt == 4:
        print("ELIMINAR FICHA DEL PACIENTE")
        print("----------------------------------------")
        print("Ingrese el RUT del paciente para proceder a ELIMINAR FICHA:")
        rut_buscar = input()

        encontrado = False

        for i in range(f):
            if pac[i, 2] == rut_buscar:
                print("----------------------------------------")
                print("FICHA ENCONTRADA")
                print("----------------------------------------")
                print(f"Nombre: {pac[i, 0]}")
                print(f"Apellido: {pac[i, 1]}")
                print(f"RUT: {pac[i, 2]}")
                print(f"Estado civil: {pac[i, 3]}")
                print(f"Domicilio: {pac[i, 4]}")
                print(f"Teléfono: {pac[i, 5]}")
                print(f"Sexo: {pac[i, 6]}")
                print(f"Edad: {pac[i, 7]}")
                print(f"Nivel de urgencia: {pac[i, 8]}")
                print(f"Diagnóstico: {pac[i, 9]}")
                print(f"Medicamentos recetados: {pac[i, 10]}")

                confirmacion = input("¿Está seguro de eliminar esta ficha? (s/n): ").lower()
                if confirmacion == 's':
                    # Eliminar la ficha del paciente encontrada
                    for j in range(i, f - 1):
                        pac[j, :] = pac[j + 1, :]
                    f -= 1  # Decrementar el contador de pacientes

                    print("Ficha eliminada correctamente.")
                encontrado = True
                break
        
        if not encontrado:
            print("No se encontró ningún paciente con el RUT ingresado.")
        
    elif opt == 5:
        print("----------------------------------------")
        print("LISTA DE PACIENTES ATENDIDOS")
        print("----------------------------------------")
        for i in range(f):
            print(f"Ficha {i+1}:")
            print(f"Nombre: {pac[i, 0]}")
            print(f"Apellido: {pac[i, 1]}")
            print(f"RUT: {pac[i, 2]}")
            print(f"Estado civil: {pac[i, 3]}")
            print(f"Domicilio: {pac[i, 4]}")
            print(f"Teléfono: {pac[i, 5]}")
            print(f"Sexo: {pac[i, 6]}")
            print(f"Edad: {pac[i, 7]}")
            print(f"Nivel de urgencia: {pac[i, 8]}")
            print(f"Diagnóstico: {pac[i, 9]}")
            print(f"Medicamentos recetados: {pac[i, 10]}")
            if pac[i, 21] == "No":
                print("No viene con acompañante")
            else:
                print(f"Nombre del acompañante: {pac[i, 21]} {pac[i, 22]}")
                print(f"Rut del acompañante: {pac[i, 23]}")
                print(f"Teléfono del acompañante: {pac[i, 24]}")
                print(f"Parentesco del acompañante: {pac[i, 25]}")
            print()

    elif opt == 6:
        # Crear una lista de listas con datos válidos
        data_to_save = pac[:f].tolist()

        try:
            with open('pacientes.json', 'w') as paciente_json:
                json.dump(data_to_save, paciente_json, indent=4)
            print("Datos guardados correctamente en 'pacientes.json'.")
        except Exception as e:
            print(f"Error al guardar los datos en 'pacientes.json': {e}")
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
