class Animal:
    def __init__(self):
        pass

    def walk(self):
        print("Animal is walking")

    def eat(self):
        pass


class Pet:
    def play(self):
        pass


class Spider(Animal):
    def eat(self):
        print("Spider is eating now")

    def __str__(self):
        return "Spider"


class Cat(Animal, Pet):
    def eat(self):
        print("Cat is eating now")

    def play(self):
        print("Cat is playing now")

    def __str__(self):
        return "Cat"


class Fish(Animal, Pet):
    def eat(self):
        print("Fish is eating now")

    def play(self):
        print("Fish is playing now")

    def walk(self):
        print("Fish is swimming now")

    def __str__(self):
        return "Fish"


zoo = [
    Cat(),
    Spider(),
    Fish(),
    Spider(),
    Cat(),
    Spider(),
    Fish(),
    Cat()
]
numberOfPets = 0
for animal in zoo:
    if isinstance(animal, Animal):
        numberOfPets += 1
print(numberOfPets)

