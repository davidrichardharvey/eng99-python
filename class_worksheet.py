print("\nQ2a\n")
# Q2a: Using the predefined class and method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        return self.integer % n == 0


primes = []
for num in list_of_numbers:
    number = Number(num)
    print(number.integer)
    if number.is_prime():
        primes.append(num)

print(primes)
