"""
3) Desarrollar una aplicación que permita a un médico gestionar su agenda de citas utilizando los Tipos
Abstractos de Datos (TADs) que se consideren apropiados. Cada cita deberá contener la siguiente
información: DNI del paciente, nombre, obra social, teléfono, fecha de la cita y hora de la cita. El
sistema deberá brindar un menú de opciones mediante el cual el usuario pueda realizar distintas
operaciones sobre las citas almacenadas en la agenda.

a. Alta de citas:
Implementar la funcionalidad para registrar nuevas citas médicas, ingresando todos los datos
correspondientes al paciente.

b. Modificación de fecha y hora de una cita:
Permitir modificar la fecha y/o la hora de una cita ya existente, identificando al paciente mediante su
número de DNI.

c. Eliminación de citas individuales:
Implementar una opción para eliminar una cita específica de la agenda, ya sea por cancelación o
modificación del cronograma del médico.

d. Listado completo de citas:
Desarrollar una funcionalidad que permita mostrar todas las citas almacenadas, desplegando
ordenadamente todos los datos de cada paciente citado.

e. Traslado de citas de un día a otro:
Permitir al usuario mover todas las citas de una fecha determinada a una nueva fecha, facilitando la
reorganización de la agenda ante imprevistos.

f. Depuración y generación de lista filtrada:
o a) Eliminar todas las citas asociadas a una obra social específica, ingresada por el usuario.
o b) Generar una nueva cola que contenga únicamente los nombres y obras sociales de los
pacientes citados en un día específico, e imprimirla inmediatamente en pantalla.    
"""

from TAD.TADagendaCita import *
from TAD.TADcita import *
from TAD.TADcola import *
from validaciones.validaciones import *
from datetime import datetime
import os

agenda = crearAgenda()
cola = crearCola()

def mostrarCita(c):
    print(f"DNI: {verDni(c)}")
    print(f"Nombre: {verNombre(c)}")
    print(f"Obra Social: {verObraSocial(c)}")
    print(f"Telefono: {verTelefono(c)}")
    print(f"Fecha de la cita: {verFecha(c)}")
    print(f"Hora de la cita: {verHora(c)}")

#punto a
def altaDeCita():
    b = True
    while b:
        cita = crearCita()
        #val dni
        while True:
            dni = input("Ingrese el DNI del paciente: ").strip()
            if validar_dni(dni, agenda):
                break
            print("DNI invalido. debe contener solo numeros y tener 8 digitos.")
            
        #val nombre
        while True:
            nombre = input("Ingrese el nombre del paciente: ").strip()
            if validar_nombre(nombre):
                break
            print("El nombre no puede estar vacio o tiene caracteres no validos.")

        # val obra social
        while True:
            obraSocial = input("Ingrese la obra social del paciente: ").strip()
            if validar_obra_social(obraSocial):
                break
            print("La obra social no puede estar vacia.")

        # val de telefono
        while True:
            telefono = input("Ingrese el telefono del paciente: ").strip()
            if validar_telefono(telefono):
                break
            print("telefono invalido. Debe contener solo numero y tener entre 6 y 15 digitos.")

        # Validación de fecha
        while True:
            fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa): ").strip()
            if validar_fecha(fecha):
                break
            print("Fecha invalido. Debe ser una fecha futura y en formato dd/mm/aaaa.")

        # Validación de hora
        while True:
            hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
            if validar_hora(hora):
                break
            print("Hora invalida. Debe estar en formato HH:MM y ser una hora valida.")

        cargarCita(cita, dni, nombre, obraSocial, telefono, fecha, hora)
        agregarCita(agenda, cita)
        print("Cita registrada con exito.")
        limpiarPantalla()

        seguir = input("¿Desea registrar otra cita? (s/n): ").lower()
        if seguir != 's':
            b = False

#punto b
def ModificarCita(agenda):
    limpiarPantalla()
    if esVacia(agenda):
        print("La agenda esta vacia.")
        return
    
    # Mostrar todas las citas con indice
    print("Citas registradas:")
    for i, cita in enumerate(agenda, 1):
        mostrarCita(cita)
        print("-" * 40)
    dni_busqueda = input("Ingrese el DNI de la cita que desea modificar: ")

    for cita in agenda:
        if verDni(cita) == dni_busqueda:
            limpiarPantalla()
            print("Cita encontrada:")
            mostrarCita(cita)

            # Validar fecha
            while True:
                nueva_fecha = input("Ingrese la nueva fecha (dd/mm/aaaa): ")
                if validar_fecha(nueva_fecha):
                    break
                else:
                    print("Fecha invalida. Ingrese una fecha valida en formato dd/mm/aaaa.")

            # Validar hora
            while True:
                nueva_hora = input("Ingrese la nueva hora (HH:MM): ")
                if validar_hora(nueva_hora):
                    break
                else:
                    print("Hora invalida. Ingrese la hora en formato HH:MM (24hs).")
            
            # Modificar cita
            modFecha(cita, nueva_fecha)
            modHora(cita, nueva_hora)

            limpiarPantalla()
            print("Cita modificada con exito.")
            mostrarCita(cita)
            return
    print("No se encontro ninguna cita con ese DNI.")

#punto c
def EliminarCita(agenda):
    limpiarPantalla()

    if esVacia(agenda):
        print("La agenda esta vacia.")
        return

    print("Citas registradas:")
    for i in range(tamnioAgenda(agenda)):
        cita = recuperarCita(agenda, i + 1)
        mostrarCita(cita)
        print("-" * 40)

    # Validar entrada de DNI
    while True:
        dni_busqueda = input("Ingrese el DNI del paciente para eliminar su cita: ").strip()
        if validar_dni_busqueda(dni_busqueda):
            break
        else:
            print("Dni invalido, intenta de nuevo.")

    i = 0
    encontrado = False
    while i < tamnioAgenda(agenda):
        cita = recuperarCita(agenda, i + 1)
        if verDni(cita) == dni_busqueda:
            limpiarPantalla()
            print("Cita encontrada:")
            mostrarCita(cita)
            # Validar respuesta de confirmacion
            while True:
                confirmacion = input("Esta seguro que desea eliminar esta cita? (s/n): ").strip().lower()
                if confirmacion == 's':
                    eliminarCita(agenda, cita)
                    print("Cita eliminada con exito.")
                    encontrado = True
                    break
                elif confirmacion == 'n':
                    print("Eliminacion cancelada.")
                    encontrado = True
                    break
                else:
                    print("Respuesta invalida. Ingrese 's' para si o 'n' para no.")
            break
        else:
            i += 1
    if not encontrado:
        print("No se encontro ninguna cita con ese DNI.")

#punto d
def transladoCitas(agenda):
    limpiarPantalla()
    if esVacia(agenda):
        print("La agenda esta vacia.")
        return
    
    while True:
        fecha_original = input("Ingrese la fecha de origen (dd/mm/aaaa): ").strip()
        if validar_fecha_existente(fecha_original, agenda):
            break
        print("Fecha invalida o sin citas. Intente de nuevo.")

    while True:
        nueva_fecha = input("Ingrese la nueva fecha destino (dd/mm/aaaa): ").strip()
        if validar_fecha(nueva_fecha):
            break
        print("Fecha invalida. Debe estar en formato dd/mm/aaaa y ser futura.")

    trasladadas = 0
    for cita in agenda:
        if verFecha(cita) == fecha_original:
            modFecha(cita, nueva_fecha)
            trasladadas += 1
    
    limpiarPantalla()
    if trasladadas == 0:
        print(f"No se encontraron citas para la fecha {fecha_original}.")
    else:
        print(f"{trasladadas} cita(s) trasladadas exitosamente de {fecha_original} a {nueva_fecha}.")

#punto e.a
def eliminarCitasObraSocial(agenda):
    limpiarPantalla()

    if esVacia(agenda):
        print("La agenda esta vacia.")
        return
    
    while True:
        obra_social = input("Ingrese el nombre de la obra social para eliminar sus citas: ").strip()
        if validar_obra_social(obra_social):
            break
        print("Obra social invalida. Intente de nuevo.")

    total = tamnioAgenda(agenda)
    eliminadas = 0
    i = 0

    while i < total:
        cita = recuperarCita(agenda, i + 1) #acomodar indice(el 1er elemento tine indice 0 no 1)
        if verObraSocial(cita).lower() == obra_social.lower():
            eliminarCita(agenda, cita)
            eliminadas += 1 #aumento el cont para llevar reg de cuantas se eliminaron
            total -= 1 #aumento el total para que no se repitan los indices
        else:
            i += 1 #si no es la obra social que buscamos, avanzo al siguiente elemento

    limpiarPantalla()

    if eliminadas == 0:
        print(f"No se encontraron citas asociadas a la obra social '{obra_social}'.")
    else:
        print(f"{eliminadas} citas eliminadas de la obra social '{obra_social}'.")

#punto e.b

def generarListaFiltrada(agenda):
    limpiarPantalla()

    if esVacia(agenda):
        print("La agenda esta vacia.")
        return
    
    while True:
        fecha = input("Ingrese la fecha para filtrar las citas (dd/mm/aaaa): ").strip()
        if validar_fecha(fecha):
            break
        print("Fecha invalida. Debe estar en formato dd/mm/aaaa.")

    cola_filtrada = crearCola()

    for cita in agenda:
        if verFecha(cita) == fecha:
            nombre = verNombre(cita)
            obra_social = verObraSocial(cita)

            encolar(cola_filtrada,(nombre, obra_social)) #encolar el nombre y la obra social
    limpiarPantalla()
    if esColaVacia(cola_filtrada):
        print(f"No se encontraron citas para la fecha {fecha}.")
    else:
        print(f"Citas filtradas para la fecha {fecha}:")
        while not esColaVacia(cola_filtrada):
            nombre, obra_social = desencolar(cola_filtrada)
            print(f"Nombre: {nombre}, Obra Social: {obra_social}")

def menu():
    limpiarPantalla()
    print("\n1. Alta de citas")
    print("2. Modificar fecha y hora de una cita") 
    print("3. Eliminar cita")
    print("4. Listado completo de citas")
    print("5. Traslado de citas de un dia a otro")
    print("6. Eliminar citas de una obra social")
    print("7. Generar lista filtrada de pacientes de un dia")
    print("0. Salir")
    op = input("Ingrese una opcion: ").strip() #el strip elimina los espacios
    try:  
        if len(op) != 1 or op not in "01234567": #el len obtiene la longitud y si no es 1 no esta en el rango de 0 a 7
            raise ValueError("la opcion no es valida")

        opcion = int(op)
         
        if opcion == 1:
            altaDeCita()
        elif opcion == 2:
            ModificarCita(agenda)
        elif opcion == 3:
            EliminarCita(agenda)
        elif opcion == 4:
            limpiarPantalla()
            if not agenda:
                print("No hay citas registradas.")
            else:
                for cita in agenda:
                    mostrarCita(cita)
                    print("-" * 40)
        elif opcion == 5:
            transladoCitas(agenda)
        elif opcion == 6:
            eliminarCitasObraSocial(agenda)
        elif opcion == 7:
            generarListaFiltrada(agenda)
        elif opcion == 0:
            print("Saliendo...")
        else:
            print("opcion no valida, por favor ingrese una opcion entre 0 y 7.")
    except ValueError:
            print("Por favor, ingrese un numero valida entre 0 y 7.")

if __name__ == "__main__":
    while True:
        menu()
        if input("¿Desea continuar? (s/n): ").lower() != 's':
            break
