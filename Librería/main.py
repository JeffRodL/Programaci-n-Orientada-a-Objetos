from Biblioteca import Biblioteca
from Libro import Libro

if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        print("---Biblioteca---")
        opcion = int(input("¿Qué vas hacer?:\n1-Crear Biblioteca\n2- Agregar libro\n3- Ver Catalogo\n4-Quitar Libro\n5-Salir\n:"))

        if opcion == 1:
            nombre = input("Nombre de la Biblioteca")
            biblioteca = Biblioteca(nombre)
            print("Se creo la biblioteca: {}".format(biblioteca.consultar_nombre_biblioteca))
        elif opcion == 2:
            titulo = input("Titulo:")
            autor = input("Autor:")
            cantidad_de_paginas = input("Cantidad de Paginas:")
            genero = input("Genero:")   
            sinopsis = input("Sinopsis:")   
            libro = Libro(titulo,autor,cantidad_de_paginas,genero,sinopsis)
            biblioteca.agregar_libro(libro)
        
        elif opcion == 3:
            print("Catalogo de libros: ")
            for i in biblioteca.consultar_libros():
                print(i)

        elif opcion == 4:
            indice = input("Id del libro a eliminar: ")
            biblioteca.quitar_libro(indice)

        elif opcion == 5:
            ejecutar = False

        else:
            print("Opcion incorrecta")
