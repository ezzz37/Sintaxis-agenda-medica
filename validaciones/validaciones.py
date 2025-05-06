from datetime import datetime
from TAD.TADagendaCita import *
from TAD.TADcita import *
import os

def validar_dni(dni, agenda):
    if not (dni.isdigit() and len(dni) == 8): #isdigit verifican que sean string de numeros
        return False
    for cita in agenda:
        if verDni(cita) == dni:
            print("Ya existe una cita registrada con ese DNI.")
            return False
    return True


def validar_nombre(nombre):
    nombre = nombre.strip()
    return bool(nombre) and nombre.isalpha() and len(nombre) <= 10


def validar_obra_social(obraSocial):
    obraSocial = obraSocial.strip() #strip() saca espacios vacios
    return bool(obraSocial) and obraSocial.isalpha() and len(obraSocial) <= 10 #isalpha() verifica que sean string de letras y no numeros

def validar_telefono(telefono):
    return telefono.isdigit() and 6 <= len(telefono) <= 15

def validar_fecha(fecha):
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y") #strptime convierte un string a un objeto datetime
        return fecha_dt.date() >= datetime.today().date() #verifica que la fecha sea mayor o igual a la fecha actual
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def validFloat(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Ingrese un num valido.")

def validFecha(msg):
    while True:
        fecha = input(msg)
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Formato de fecha invalido. Intente de nuevo (dd/mm/aaaa).")

def validar_dni_busqueda(dni):
    return dni.isdigit() and len(dni) == 8

def validar_fecha_existente(fecha, agenda):
    for cita in agenda:
        if verFecha(cita) == fecha:
            return True
    return False