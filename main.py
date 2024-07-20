# animals_info.py is assumed to be in the same directory

from data import create_animals_list

class Animal:
    def __init__(self, name, weight, age, species):
        self.name = name
        self.weight = weight
        self.age = age
        self.species = species
    
    def display(self):
        print(f"Name: {self.name}, Weight: {self.weight}, Age: {self.age}, Species: {self.species}")

class Cow(Animal):
    def __init__(self, name, weight, age, breed):
        super().__init__(name, weight, age, "Cow")
        self.breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self.breed}")

class Bird(Animal):
    def __init__(self, name, weight, age, breed):
        super().__init__(name, weight, age, "Bird")
        self.breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self.breed}")

class Cats(Animal):
    def __init__(self, name, weight, age, color):
        super().__init__(name, weight, age, "Cat")
        self.color = color

    def display(self):
        super().display()
        print(f"Color: {self.color}")

class Chicken(Animal):
    def __init__(self, name, weight, age, breed):
        super().__init__(name, weight, age, "Chicken")
        self.breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self.breed}")

class Monkey(Animal):
    def __init__(self, name, weight, age, breed):
        super().__init__(name, weight, age, "Monkey")
        self.breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self.breed}")

class Dogs(Animal):
    def __init__(self, name, weight, age, breed):
        super().__init__(name, weight, age, "Dog")
        self.breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self.breed}")

class Garden:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def display_garden_info(self):
        print(f"Garden name: {self.name}")
        for animal in self.animals:
            animal.display()
            print("---")

class House:
    def __init__(self, name, address, has_garage):
        self.name = name
        self._address = address
        self.has_garage = has_garage
        self.gardens = []

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise ValueError("Address must be a string")
        self._address = value

    def add_garden(self, garden):
        self.gardens.append(garden)

    def display_house_info(self):
        print(f"House name: {self.name}, House address: {self.address}, Has garage: {self.has_garage}")
        for garden in self.gardens:
            garden.display_garden_info()

def create_animal(info):
    species = info.get("species", "").lower()
    if species == "dog":
        return Dogs(info["name"], info["weight"], info["age"], info["breed"])
    elif species == "cat":
        return Cats(info["name"], info["weight"], info["age"], info["color"])
    elif species == "cow":
        return Cow(info["name"], info["weight"], info["age"], info["breed"])
    elif species == "bird":
        return Bird(info["name"], info["weight"], info["age"], info["breed"])
    elif species == "chicken":
        return Chicken(info["name"], info["weight"], info["age"], info["breed"])
    elif species == "monkey":
        return Monkey(info["name"], info["weight"], info["age"], info["breed"])
    else:
        raise ValueError(f"Unknown species: {species}")

# Main script
animals_info = create_animals_list()

animals = []
for info in animals_info:
    try:
        animal = create_animal(info)
        animals.append(animal)
    except ValueError as e:
        print(f"Error creating animal: {e}")

print(f"Total animals created: {len(animals)}")

my_garden = Garden("Luminous Garden")
neighboring_garden = Garden("Shiny Garden")

for animal in animals:
    if isinstance(animal, Cats):
        if animal.color == "Yellow":
            my_garden.add_animal(animal)
        else:
            neighboring_garden.add_animal(animal)
    elif isinstance(animal, Dogs):
        if "shepard" in animal.breed.lower():
            my_garden.add_animal(animal)
        else:
            neighboring_garden.add_animal(animal)
    else:
        # Add all other animals to the neighboring garden
        neighboring_garden.add_animal(animal)

print("My Garden:")
my_garden.display_garden_info()

print("\nNeighboring Garden:")
neighboring_garden.display_garden_info()

house1 = House("Big house", "Xyz 13 49", False)
house2 = House("Medium house", "YxZ 12 43", True)

house1.add_garden(my_garden)
house2.add_garden(neighboring_garden)

print("\nHouse 1:")
house1.display_house_info()

print("\nHouse 2:")
house2.display_house_info()