
from math import pi
#Exemplo de uma classe que estaria aberta a modificação
#Está classe tem duas funções, calcular a área de um retangulo e um trinagulo
#Como seria a possivel modificação? Se precisarmos calcular outro tipo de forma
#Teria que alterar o construtor, modificando a classe
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

if __name__ == '__main__':
    retangulo = Shape("rectangle", width=10, height=5)
    retangulo.calculate_area()

    circulo = Shape("circle", radius=5)
    circulo.radius()


