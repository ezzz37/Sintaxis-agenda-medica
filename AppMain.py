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
            print("El nombre no puede estar vacio")

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
        print(f"{i}. DNI: {verDni(cita)} - Nombre: {verNombre(cita)} - Fecha: {verFecha(cita)} - Hora: {verHora(cita)}")

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
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            altaDeCita()
        elif opcion == 2:
            ModificarCita(agenda)
        elif opcion == 3:
            pass
        elif opcion == 4:
            limpiarPantalla()
            if not agenda:
                print("No hay citas registradas.")
            else:
                for cita in agenda:
                    mostrarCita(cita)
                    print("-" * 40)
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
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
