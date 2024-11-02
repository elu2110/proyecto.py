 
'''
 los productos 

 [nombre(str),precio(float),cantidad(int)]

 '''

productos = [ 
 ["pañales",20000,10],
 ["toallitas humedas",2300,15],
 ["oleo calcareo",4000,10],
 ["mamadera recien nacido",5000,5],

]

while   True:
    print("*" * 20)
    print("Menu De Opciones\n")
    print("1. agregar productos ")
    print("2. Modificacion ")
    print("3. Eliminar ")
    print("4. mostra todo ")
    print("5. Mas vendido ")
    print("0. Salir ")
    print("*" * 20)


    opcion = input("Ingresa una opcion ")
    opcion=int(opcion)
    if opcion == 0:
        print("nos vemos!!!")
        break
    elif opcion == 1:
        print("agregar productos")
        nombre = input("nombre del producto :")
        precio = float(input("precio:"))
        cantidad = int(input("cantidad:"))

        # se armo las lista de productos ingresados

        producto = [nombre,precio,cantidad]
        #agregar productos al listado 
        productos.append(producto)

    elif opcion == 2:
        print("aaa") 
    elif opcion == 3:
        print("aaa") 
    elif opcion == 4:
        print("listado")
        if len(productos) == 0:
          
           
          print("todavia no se cargo el stock")
        else:
            #print(productos)
            for producto in productos:
                print(f"{producto[0].ljust(30)} {str(producto[1]).ljust(10)} {producto[2]}")
    else:
        print(" se debe ingresar una opcion valida ")

