class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        area = 3.14 * (self.raio ** 2)
        print(f"Área do círculo: {area}")

circulo = Circulo(5)
circulo.area()
