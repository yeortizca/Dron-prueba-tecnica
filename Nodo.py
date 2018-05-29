class Nodo():

    def __init__(self,clave):
        self._clave = clave
        self._siguiente = None
        self._anterior = None

    def getClave(self):
    	return self._clave