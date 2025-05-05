def cearCita():
    c=["","","","","",""]
    return c

def cargarCita(c,dni,nombre,obraSocial,telefono,fecha,hora):
    c[0] = dni
    c[1] = nombre
    c[2] = obraSocial
    c[3] = telefono
    c[4] = fecha
    c[5] = hora


def verDni(c):
    return c[0]

def verNombre(c):
    return c[1]

def verObraSocial(c):
    return c[2]

def verTelefono(c):
    return c[3]

def verFecha(c):
    return c[4]

def verHora(c):
    return c[5]

def modDni(c,dni):
    c[0] = dni

def modNombre(c,nombre):
    c[1] = nombre

def modObraSocial(c,obraSocial):
    c[2] = obraSocial

def modTelefono(c,telefono):
    c[3] = telefono

def modFecha(c,fecha):
    c[4] = fecha

def modHora(c,hora):
    c[5] = hora

def copiar(c1,c2):
    c1[:] = c2[:]

def mostrarCitas(c):
    return f"{verDni(c)} {verNombre(c)} {verObraSocial(c)} {verTelefono(c)} {verFecha(c)} {verHora(c)}"