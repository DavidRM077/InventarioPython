# Libreria para controlar el tiempo del menu
import time as tp

# Diccionario donde se almacenaran los productos
Producto = {} 

# Funcion que hara el papel de agregar productos al diccionario
def Agregar_Producto(Datos):
    
    print("Siga las Instrucciones para registrar el producto en el inventario. \n")
    Nombre = input("Ingrese el Nombre del Producto: ")
    Cantidad = int(input("Ingrese la Cantidad del Producto: "))
    Precio = int(input("Ingrese el Precio: "))
    print("Producto Agregado con Exito")

    Datos[Nombre] = {
        "Cantidad": Cantidad,
        "Precio": Precio
    }

def Eliminar_Producto():
  Nombre = input("Introduzca el nombre del producto")
  del Producto[Nombre]

def Buscar_Producto():
  Nombre = input("Introduzca el nombre del Producto")
  Producto[Nombre]
  print(f"El Producto que desea es: {Producto[Nombre]}")

while True:
 tp.sleep(5)
 print("BIENVENIDO AL ALMACEN DE JUDGE \n")
 print(" 1- Agregar un Producto")
 print(" 2- Actualizar Producto")
 print(" 3- Eliminar un Producto")
 print(" 4- Mostrar Inventario")
 print(" 5- Buscar Producto")
 print(" 6- Salir \n")

 
 Opciones = int(input("Porfavor, Introduzca una Opcion \n"))
  
 match Opciones:
  case 1:
    Agregar_Producto(Producto)
    
    Respuesta = input("Desea Registrar Otro Producto?")
    while Respuesta.lower() != "no":
      Agregar_Producto(Producto)
      Respuesta = input("Desea Registrar Otro Producto?")

  case 2:
   print("Actualizado")
   
  case 3:
     Eliminar_Producto()
     print("Eliminando Producto")
  case 4:
     print(Producto)
  case 5:
     Buscar_Producto()
  case 6:
     "Saliendo del inventario"
     break



   



 