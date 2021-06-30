from Clases.animal import Animal

class Koala(Animal):
    def __init__(self, name, edad):
        super().__init__("Koala " + name, edad, 0, 0)
        super().alimento()

    def alimento(self):
        self.salud += 4
        self.felicidad += 15
        print(f"El koala {self.name} se alimenta. Aumenta su salud en {self.salud} y su felicidad en {self.felicidad}")
        return self