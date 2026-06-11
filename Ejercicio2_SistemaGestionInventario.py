#================================
#SISTEMA DE GESTION DE INVENTARIO
#================================

#Lista que almacenara los libros
inventario=[]

def registrar_libro():
    codigo=input("Ingrese codigo de libro: ")
    
    #Validar codigo repetido
    for libro in inventario:
        if libro["codigo"]==codigo:
            print("El codigo ya existe!!")
            return
    titulo=input("Ingrese titulo: ") 
    autor=input("Ingrese autor: ")
    
    try:
        
        cantidad=int(input("Ingrese cantidad: "))
        precio=float(input("Ingrese precio: "))
    except ValueError:
        print("Error: debe ingresar valores numericos")
        return
    
    libro={
        "codigo": codigo,
        "titulo":titulo,
        "autor":autor,
        "cantidad": cantidad,
        "precio":precio
        
    }
    
    inventario.append(libro)
    print("Libro registrado correctamente")
    
def buscar_libro():
    codigo=input("Ingrese codigo a buscar: ")
    
    for libro in inventario:
        if libro["codigo"]==codigo:
            print("\n===LIBRO ENCONTRADO===")
            print("Codigo: ", libro["codigo"])
            print("Titulo: ", libro["titulo"])
            print("Autor: ",libro["autor"] )
            print("Cantidad: ", libro["cantidad"])
            print("Precio: ", libro["precio"])
            return

    print("Libro no encontrado")

def actualizar_stock():
    codigo= input("Ingrese codigo del libro: ")
    
    for libro in inventario:
        if libro["codigo"]==codigo:
            try:
                nueva_cantidad=int(input("Ingrese nuevo stock: "))
                libro["cantidad"]=nueva_cantidad
                print("Stock Actualizado correctamente")
            except ValueError:
                print("Debe ingresar un numero entero")
            return
        
    print("Libro no encontrado")

def mostrar_inventario():
    if len(inventario)==0:
        print("No existen libros registrados")
        return
    
    print("\n====INVENTARIO====")
    
    for libro in inventario:
        print("Codigo: ", libro["codigo"])
        print("Titulo: ", libro["titulo"])
        print("Autor: ", libro["autor"])
        print("Cantidad: ", libro["cantidad"])
        print("Precio: $", libro["precio"])
        print("-"*30)
        
def libro_mas_caro():
    if len(inventario)==0:
     print("No existen libros registrados")
     return

    mas_caro=inventario[0]
    for libro in inventario:
        if libro["precio"]>mas_caro["precio"]:
            mas_caro=libro
    
    print("\n===LIBRO MAS CARO===")
    print("Codigo: ", mas_caro["codigo"])
    print("Titulo: ", mas_caro["titulo"])
    print("Autor: ", mas_caro["autor"])
    print("Cantidad: ", mas_caro["cantidad"])
    print("Precio: $", mas_caro["precio"])
    

def eliminar_libro():
    codigo=input("Ingrese codigo de libro a eliminar: ")
    
    for libro in inventario:
        if libro["codigo"]==codigo:
            inventario.remove(libro)
            print("Libro eliminado correctamente")
            return
        
    print("Libro no encontrando")

def valor_total_inventario():
    total=0
    
    for libro in inventario:
        total +=libro["cantidad"]*libro["precio"]
        
    print(f"valor total del inventario es:{total} ")
    
#Menu Principal:
while True:
    print("===LIBRERIA===")
    print("1.Registrar Libro")
    print("2.Buscar Libro") 
    print("3.Actualizar Stock")
    print("4.Mostrar inventario")
    print("5.Mostrar Libro mas Caro")
    print("6.Eliminar Libro")
    print("7.Mostrar el valor total del inventario")
    print("8.Salir")
    
    try:
        opcion=int(input("Ingrese una opcion valida: "))
        
        if opcion==1:
            registrar_libro()
            
        elif opcion==2:
            buscar_libro()
            
        elif opcion==3:
            actualizar_stock()
            
        elif opcion==4:
            mostrar_inventario()
            
        elif opcion==5:
            libro_mas_caro()
            
        elif opcion==6:
            eliminar_libro()
            
        elif opcion==7:
            valor_total_inventario()
        
        elif opcion==8:
            print("Saliendo del programa.....")
            break
        else:
            print("Ingrese una opcion valida")
    
    except ValueError:
        print("Ingrese un numero entero valido")               
              
            
            
        
                    
               
        

    