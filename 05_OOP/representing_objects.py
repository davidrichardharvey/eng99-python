# Write the init method so that we can initalise a latitude and longitude

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"
#
# bham_academy = Location(latitude=52.488647, longitude=-1.887249)
# print(bham_academy)
# print(repr(bham_academy))
#
#
# print(f"The Sparta Global Birmingham Academy is located at {bham_academy}")


n = 0.004837

print(f"Percentage: {n:.2%}")
print(f"Fixed Point: {n:f}")
print(f"Exponential Notation: {n:e}")

class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old Dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old Dog"
        else:
            return self.__str__()

fido = Dog(5)
print(fido)
print(f"Fido is {fido:dog}")