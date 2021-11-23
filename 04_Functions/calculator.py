print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors(num: int) -> list:
    divisors_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list

print(divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function)

# A1b:
def comparison(num1, num2):
    # return num2 in divisors(num1) or num1 in divisors(num2)
    return num1 % num2 == 0 or num2 % num1 == 0

print(comparison(12, 6))
print(comparison(12, 7))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def alphabet_position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    position = alphabet.index(letter.lower())
    return position + 1

print(alphabet_position("A"))
print(alphabet_position("Z"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

name = "david"
for letter in name:
    print(letter, alphabet_position(letter))
    name += "."
    print(name)

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
for digit in "429572349":
    print(digit)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def solution(i):
    return int(i)


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def solution2(i):
    # Check that i is just digits
    return int(i)
    # If not, print a warning message and return None


# -------------------------------------------------------------------------------------- #



