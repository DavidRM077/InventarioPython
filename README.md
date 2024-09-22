Ejercicio Intermedio:

Problema: Sistema de Gestión de Inventario

Crea un programa que simule un sistema de gestión de inventario. El programa debe permitir realizar las siguientes operaciones:
1.	Agregar un producto: Permite al usuario agregar un nuevo producto al inventario. Cada producto debe tener un nombre, una cantidad y un precio. Almacena los productos en un diccionario donde el nombre del producto es la clave y un diccionario con cantidad y precio es el valor.
2.	Actualizar la cantidad de un producto: Permite al usuario actualizar la cantidad de un producto existente en el inventario.
3.	Eliminar un producto: Permite al usuario eliminar un producto del inventario.
4.	Mostrar todos los productos: Muestra una lista completa de todos los productos con su cantidad y precio.
5.	Buscar un producto: Permite al usuario buscar un producto por nombre y mostrar su cantidad y precio.

   
Instrucciones:
1.	Crear un diccionario vacío para almacenar los productos.
2.	Definir funciones para cada operación:
o	agregar_producto(inventario, nombre, cantidad, precio): Agrega un nuevo producto.
o	actualizar_cantidad(inventario, nombre, nueva_cantidad): Actualiza la cantidad de un producto existente.
o	eliminar_producto(inventario, nombre): Elimina un producto del inventario.
o	mostrar_productos(inventario): Muestra todos los productos en el inventario.
o	buscar_producto(inventario, nombre): Busca y muestra la información de un producto.
3.	Mostrar un menú con las opciones mencionadas y permitir al usuario seleccionar opciones hasta que elija salir.
4.	Usar bucles para manejar la entrada del usuario y realizar las operaciones correspondientes.
