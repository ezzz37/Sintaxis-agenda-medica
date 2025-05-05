from datetime import datetime
from TAD.TADagendaCita import *
from TAD.TADcita import *

def validar_dni(dni, agenda):
    if not (dni.isdigit() and len(dni) == 8): #isdigit verifican que sean string de numeros
        return False
    for cita in agenda:
        if verDni(cita) == dni:
            print("Ya existe una cita registrada con ese DNI.")
            return False
    return True


def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_obra_social(obra_social):
    return bool(obra_social.strip()) #strip() saca espacios vacios

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
