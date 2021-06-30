from Clases.leon import Leon
from Clases.koala import Koala
from Clases.pulpo import Pulpo

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add(self, animal):
        self.animals.append(animal)

    def display_info(self):
        for animal in self.animals:
            print(f"""
                Nombre: {animal.name}
                Salud: {animal.salud}
                Felicidad: {animal.felicidad} """)
        return self
    def atributounico(self):
        for animal in zoo1.animals:
            if animal.name == "Leon Memo":
                animal.formavivir()
        return self
    def alimentartodos(self):
        for animal in zoo1.animals:
            animal.alimento()
        return self
    
zoo1 = Zoo("Zoologico")
zoo1.add(Leon("Memo", 3, "manada"))
zoo1.add(Koala("Paul", 1))
zoo1.add(Pulpo("Luismi", 2))
zoo1.display_info()
zoo1.atributounico()
zoo1.alimentartodos()
zoo1.display_info()
