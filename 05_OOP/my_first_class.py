class Dog:
    def __init__(self, name, coat_colour): # "dunder init" (double-underscore initialise)
        self.legs = 4
        self.animal_kind = "canine"
        self.name = name
        self.__colour = coat_colour
        print(self.bark())

    def bark(self): # method
        return f"Woof! I am a {self.animal_kind}"

    def get_colour(self):
        return self.__colour

    def set_colour(self, new_colour):
        self.__colour = new_colour


fido = Dog("Fido", "black") # instantiation (instance)
print(fido.get_colour())
fido.set_colour("green")
print(fido.get_colour())
fido.__colour = "turquoise"
print(fido.get_colour())

fido.tail = True

print(fido.tail)