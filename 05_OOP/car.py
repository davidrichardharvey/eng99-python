# Define a car class

# Initialised with a current speed (start at 0) and top speed attribute
# Accelerate method
# Brake method

# Do the accelerate and brake methods work as you would expect?

class Car:
    def __init__(self, max_speed):
        self._current_speed = 0
        self.max_speed = max_speed

    def get_speed(self):
        return self._current_speed

    def accelerate(self, extra_mph):
        # if self.current_speed + extra_mph < self.max_speed:
        #     self.current_speed += extra_mph
        # else:
        #     self.current_speed = self.max_speed
        self._current_speed = min(self._current_speed + extra_mph, self.max_speed)

    def brake(self, delta):
        if self._current_speed - delta > 0:
            self._current_speed -= delta
        else:
            self._current_speed = 0
        # self.current_speed = max(self.current_speed - delta, 0)

car = Car(180)
car.accelerate(100)
print(car.get_speed())
car.accelerate(1000)
print(car.get_speed())
car.brake(13453453)
print(car.get_speed())
