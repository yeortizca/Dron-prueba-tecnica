from Nodo import Nodo
from ListaCircularDobleEnlazada import ListaCircularDobleEnlazada
from Posicion import Posicion

class Main():

  posiciones = []

  @staticmethod
  def MenuPrincipal():
    ListaCircularDobleEnlazada.AgregarFinal('N')
    ListaCircularDobleEnlazada.AgregarFinal('O')
    ListaCircularDobleEnlazada.AgregarFinal('S')
    ListaCircularDobleEnlazada.AgregarFinal('E')
    aux = True
    while(aux):
       
      print("\n1.Leer Direcciones")
      print("2.Escribir Posicones")
      print("3.Salir")
      opcion = input("Ingrese la opcion que desea:")

      if(opcion == "1"):
        Posicion.LeerDireccion(Main.posiciones)
      elif(opcion == "2"):
        Posicion.EscribirPosiciones(Main.posiciones)
      elif(opcion == "3"):
        pass
      else:
        pass
            

if __name__=="__main__":
  Main.MenuPrincipal()