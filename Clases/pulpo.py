from Clases.animal import Animal

class Pulpo(Animal):
    def __init__(self, name, edad):
        super().__init__("Pulpo " + name,  edad, 0, 0)
        super().alimento()

    def alimento(self):
        self.salud += 8
        self.felicidad += 12
        print(f"El pulpo {self.name} se alimenta. Aumenta su salud en {self.salud} y su felicidad en {self.felicidad}")
        return self