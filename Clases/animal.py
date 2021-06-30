
class Animal:
    def __init__(self, name, edad, salud, felicidad):
        self.name = name
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
#También debe tener un método de alimentación que aumente la salud y la felicidad en 10.
    def alimento(self):
        self.salud += 10
        self.felicidad += 10
        return self