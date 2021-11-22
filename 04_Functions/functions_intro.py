# DON'T
# REPEAT
# YOURSELF

# def print_something(string_to_print): # <-- defining the function
#     print(f"{string_to_print} has been printed")
#     print(f"{string_to_print} has been printed again")
#
# print_something("banana")
# print_something("orange")
# print_something("apple")

# def add_plus_one(int1, int2):
#     total = int1 + int2 + 1
#     return total
#
# x = add_plus_one(5, 7)
# print(x)
# print(x * 2)
#
# # Multiplies together everything in the tuple and divides the product by 2
# def product_divided_by_two(*args):
#     total = 1
#     for x in args:
#         total *= x
#     return total / 2
#
# print(product_divided_by_two(1, 2, 3, 4, 5))
# print(product_divided_by_two(100000, 20000, 0))

def shout_n_times(string_to_shout: str, number_of_times_to_shout=3, loud=True) -> str:
    if loud:
        string_to_shout = string_to_shout.upper()
    return string_to_shout * number_of_times_to_shout

x = shout_n_times("Hello!")

