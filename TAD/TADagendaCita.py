from TAD.TADcita import *

def crearAgenda():
    a = []
    return a

def agregarCita(a, cita):
    a.append(cita)

def eliminarCita(a, cita):
    a.remove(cita)

def recuperarCita(a,ind):
    return a[ind-1]

def tamnioAgenda(a):
    return len(a)

def esVacia(a):
    return len(a) == 0