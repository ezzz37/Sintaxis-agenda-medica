#la funcionalidad de este tad es crear una cola temporal para el punto f_b

def crearCola():
    cola = []
    return cola

def encolar(cola, cita):
    cola.append(cita)

def desencolar(cola):
    if esVacia(cola):
        return
    e = cola[0]
    cola.pop(0)
    return e

def tamCola(cola):
    return len(cola)

def esVacia(cola):
    return len(cola) == 0

def copiarCola(c1,c2):
    aux = crearCola()
    while not esVacia(c2):
        e = desencolar(c2)
        if e is not None:
            encolar(aux, e)
    while not esVacia(aux):
        e = desencolar(aux)
        encolar(c2, e)
        encolar(c1, e)