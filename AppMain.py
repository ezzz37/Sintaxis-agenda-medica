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
from datetime import datetime

def menu():
    print("\n1. Alta de citas")
    print("2. Modificar fecha y hora de una cita") 
    print("3. Eliminar cita")
    print("4. Listado completo de citas")
    print("5. Traslado de citas de un dia a otro")
    print("6. Eliminar citas de una obra social")
    print("7. Generar lista filtrada de pacientes de un daa")
    print("0. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    elif opcion == 7:
        pass
    elif opcion == 0:
        print("Saliendo...")


if __name__ == "__main__":
    menu()
