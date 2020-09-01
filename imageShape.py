# biblioteca de opencv y numpy
import cv2
import numpy as np

# clase imageShape
class imageShape:

    # constructor de la clase
    def __init__(self,width,height):
        self.width = width # recibe el ancho de la imagen
        self.height = height # recibe la altura de la imagen
        self.flag = False # bandera que dice si ya se almaceno algo en self.shape

    #  funcion que genera aleatoriamente una de las 4 figuras en fondo negro
    def generateShape(self):
        size = (self.height, self.width, 3) # establece las dimenciones de la imagen
        self.shape = np.zeros(size) # coloca los valores de la imagen en 0
        self.ind_shapes = np.random.randint(1, 5) # genera un numero entero aleatorio entre 1 y 4

        #si el numero aleatorio es 1, se genera un triangulo
        if self.ind_shapes == 1:
            # se establecen los vertices del triangulo segun las medidas pedidas
            side = min(self.width, self.height)/2
            point1 = (self.width/2, (self.height/2) - ((0.866*side)/2))
            point2 = ((self.width/2) - (side/2), (self.height/2) + ((0.866*side)/2))
            point3 = ((self.width/2) + (side/2), (self.height/2) + ((0.86603*side)/2))

            triangle = np.array([point1, point2, point3]) # genera un arreglo con los vertices del triangulo
            cv2.drawContours(self.shape, [triangle.astype(int)], 0, (227, 160, 0), -1) # dibuja y rellena la figura de color cian segun los vertices

        # si el numero aleatorio es 2, se genera un cuadrado girado 45 grados
        elif self.ind_shapes == 2:
            # se establecen los vertices del triangulo segun las medidas pedidas
            side = min(self.width, self.height) / 2
            point1 = (self.width / 2, (self.height / 2) - ((np.sqrt(2*(side**2))) / 2))
            point2 = ((self.width / 2) - ((np.sqrt(2*(side**2))) / 2), self.height / 2)
            point3 = (self.width / 2, (self.height / 2) + ((np.sqrt(2*(side**2))) / 2))
            point4 = ((self.width / 2) + ((np.sqrt(2*(side**2))) / 2), self.height / 2)

            square = np.array([point1, point2, point3, point4]) # genera un arreglo con los vertices del cuadrado
            cv2.drawContours(self.shape, [square.astype(int)], 0, (227, 160, 0), -1) # dibuja y rellena la figura de color cian segun los vertices

        # si el numero aleatorio es 3, se genera un rectangulo
        elif self.ind_shapes == 3:
            # se establecen los vertices del triangulo segun las medidas pedidas
            horizontal_side = self.width / 2
            vertical_side = self.height / 2
            point1 = ((self.width / 2) + (horizontal_side / 2), (self.height / 2) - (vertical_side / 2))
            point2 = ((self.width / 2) - (horizontal_side / 2), (self.height / 2) - (vertical_side / 2))
            point3 = ((self.width / 2) - (horizontal_side / 2), (self.height / 2) + (vertical_side / 2))
            point4 = ((self.width / 2) + (horizontal_side / 2), (self.height / 2) + (vertical_side / 2))

            rectangle = np.array([point1, point2, point3, point4]) # genera un arreglo con los vertices del rectangulo
            cv2.drawContours(self.shape, [rectangle.astype(int)], 0, (227, 160, 0), -1)# dibuja y rellena la figura de color cian segun los vertices

        # si el numero aleatorio es 4, se genera un circulo
        elif self.ind_shapes == 4:
            # se establece el centro y radio del circulo segun las medidas pedidas
            center = (int(self.width/2), int(self.height/2))
            ratio = min(self.width,self.height)/4
            cv2.circle(self.shape, center, int(ratio), (227, 160, 0), -1) # dibuja y rellena la figura de color cian segun su radio y centro

        self.flag = True # levanta la bandera de que en self.shape ya se almaceno algo

    # funcion que muestra una imagen en negro si no se ha almacenado nada en self.shape, o muestra la iamgen almacenada, ambas por 5 segundos
    def showShape(self):
        # mostrar la imagen self.shape
        if self.flag == True:
            cv2.imshow("Shape Image", self.shape)
            cv2.waitKey(5000)
        # si no crear y mostrar una imagen negra con las medidas dadas por el usuario
        else:
            size = (self.height, self.width,3)
            black_image = np.zeros(size)
            cv2.imshow("Black Image", black_image)
            cv2.waitKey(5000)

    # funcion que retorna la imagen alamacenada y un string con el nombre de la figura dentro de la imagen
    def getShape(self):
        if self.ind_shapes == 1:
            name_Shape = "Triangle"
        elif self.ind_shapes == 2:
            name_Shape = "Square"
        elif self.ind_shapes == 3:
            name_Shape = "Rectangle"
        elif self.ind_shapes == 4:
            name_Shape = "Circle"
        return self.shape, name_Shape

    # funcion que clasifica la imagen recibida segun la forma de su figura
    def whatShape(self,shape):
        self.image = shape
        shape_copy = self.image.copy()
        Gray_Image = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY) # pasa la imagen a escala de grises
        ret, Ibw_shape = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # hace la umbralizacion con metodo OTSU
        contours, hierarchy = cv2.findContours(Ibw_shape, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # encuentra los contornos
        for ind in countours:
            points = cv2.approxPolyDP(ind, 0.01*cv2.arcLength(ind,True),True) # aproxima los vertices del contorno
