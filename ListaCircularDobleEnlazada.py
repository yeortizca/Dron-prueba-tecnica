from Nodo import Nodo

class ListaCircularDobleEnlazada():
    primero = None
    ultimo = None

    @staticmethod
    def ListaVacia():
        if(ListaCircularDobleEnlazada.primero == None):
            return True
        else:
            return False
    
    @staticmethod
    def AgregarInicio(clave):
        if(ListaCircularDobleEnlazada.ListaVacia()):
            ListaCircularDobleEnlazada.primero = ListaCircularDobleEnlazada.ultimo = Nodo(clave)
        else:
           aux = ListaCircularDobleEnlazada.primero
           ListaCircularDobleEnlazada.primero = Nodo(clave)
           ListaCircularDobleEnlazada.primero.siguiente = aux
           aux.anterior = ListaCircularDobleEnlazada.primero
        ListaCircularDobleEnlazada.EnlaceFinalNodos()
    
    @staticmethod
    def AgregarFinal(clave):
        if(ListaCircularDobleEnlazada.ListaVacia()):
            ListaCircularDobleEnlazada.primero = ListaCircularDobleEnlazada.ultimo = Nodo(clave)
        else:
            aux = ListaCircularDobleEnlazada.ultimo
            ListaCircularDobleEnlazada.ultimo = aux.siguiente = Nodo(clave)
            ListaCircularDobleEnlazada.ultimo.anterior = aux
        ListaCircularDobleEnlazada.EnlaceFinalNodos()
    
    @staticmethod
    def EnlaceFinalNodos():
        ListaCircularDobleEnlazada.primero.anterior = ListaCircularDobleEnlazada.ultimo
        ListaCircularDobleEnlazada.ultimo.siguiente = ListaCircularDobleEnlazada.primero