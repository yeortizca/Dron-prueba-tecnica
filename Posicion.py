from ListaCircularDobleEnlazada import ListaCircularDobleEnlazada

class Posicion():

    def __init__(self,X=0,Y=0,direccion='N'):
        self._X = X
        self._Y = Y
        self._direccion = direccion

    @staticmethod
    def LeerDireccion(posiciones):
        txt = open('direcciones.txt')
        for camino in txt.readlines():
            camino = camino.split(',')
            aux = ListaCircularDobleEnlazada.primero
            posicion_final = Posicion()
          
            for paso in camino:
                if(paso == 'A'):
                    if(posicion_final.getDireccion() == 'N'):
                        posicion_final.setY(posicion_final.getY() + 1)
                    elif(posicion_final.getDireccion() == 'O'):
                        posicion_final.setX(posicion_final.getX() - 1)
                    elif(posicion_final.getDireccion() == 'S'):
                        posicion_final.setY(posicion_final.getY() - 1)
                    elif(posicion_final.getDireccion() == 'E'):
                        posicion_final.setX(posicion_final.getX() + 1)
                elif(paso == 'I'):
                    aux = aux.siguiente
                    posicion_final.setDireccion(aux.getClave())
                else:
                    aux = aux.anterior
                    posicion_final.setDireccion(aux.getClave())
            posiciones.append(posicion_final)
            print(len(posiciones))
        txt.close()

    @staticmethod
    def EscribirPosiciones(posiciones):
        posicion_final = open('posiciones.txt','w')
        for pos in posiciones:
            print("(" + str(pos.getX()) + "," + str(pos.getY()) + "," + pos.getDireccion() + ")")


                       
    def getX(self):
        return self._X

    def getY(self):
        return self._Y
    
    def getDireccion(self):
        return self._direccion
    
    def setX(self,x):
        self._X = x

    def setY(self,y):
        self._Y = y
    
    def setDireccion(self,direccion):
        self._direccion = direccion

    def getDireccion(self):
        return self._direccion

