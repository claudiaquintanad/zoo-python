from Clases.animal import Animal

class Leon(Animal):
    def __init__(self, name, edad, lifestyle):
        super().__init__("Leon " + name, edad, 0, 0)
        super().alimento()
        self.lifestyle = lifestyle
    #Atributo único: si el león antes ha vivido en manada o separada

    def alimento(self):
        self.salud += 7
        self.felicidad += 11
        print(f"El león {self.name} se alimenta. Aumenta su salud en {self.salud} y su felicidad en {self.felicidad}")
        return self

    def formavivir(self):
        if self.lifestyle == "manada":
            print(f"El león llamado {self.name} esta acostumbrado a vivir en manada")
        else:
            print(f"El león llamado {self.name} esta acostumbrado a vivir de manera separada")
