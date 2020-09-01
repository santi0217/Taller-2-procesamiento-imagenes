#  Fecha: 31 de agosto del 2020
#
#  Autor: Santiago Márquez Álvarez
#
#  Descripción: el codigo consiste en la utilización de una clase llamada imageShape
#               la cual recibe del usuario las dimensiones de una imagen que se quiere
#               generar. Esta clase contiene una funcion la cual se encarga de generar
#               aleatoriamente un triangulo, cuadrado, rectangulo o circulo, centrado
#               en un fondo negro; otra funcion la cual permite visualizar la imagen
#               generada si esta esta disponible, sino visualiza una imagen de color
#               negro; otra funcion que retorna la imagen generada y el nombre de la
#               figura contenida; y por ultimo, una funcion que se encarga de recibir
#               dicha imagen y clasificarla entre las 4 clases de figuras por medio de
#               umbralizacion y analisis de contornos.
#               El objetivo de utilizar esta clase descrita es generar una imagen con
#               una figura, que se debe clasificar por medio de la ultima funcion y
#               se debe verificar con la tercera funcion que la clasificacion de la
#               figura se hizo correctamente.
#


# importa la clase de imageShape
from imageShape import *

# funcion principal main
if __name__ == '__main__':

    print('Ingrese el ancho de la imagen a generar:')  # solicita el ancho de la imagen al usuario
    width = input()  # lee el ancho dado por el usuario
    width_ = int(width)
    print('Ingrese el alto de la imagen a generar:')  # solicita el alto de la imagen al usuario
    height = input()  # lee el alto dado por el usuario
    height_ = int(height)
    Shape = imageShape(width_, height_) # construye la clase con esas dimensiones
    Shape.showShape() # visualiza una imagen en negro ya que no se ha generado ninguna figura
    Shape.generateShape() # genera una figura de color cian y fondo negro
    Shape.showShape() # visualiza la imagen generada con la figura
    The_shape, Name_of_shape = Shape.getShape() # guarda en las dos variables la imagen y el string retornado
    #Shape.whatShape(The_shape)


