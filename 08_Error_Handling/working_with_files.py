try:
    with open("order.txt") as file:
        orders = file.read().split("\n")

except FileNotFoundError as errmsg:
    print(f"The file cannot be found: {errmsg}")
    raise
finally:
    print("Always do this, whatever happens")

with open("tickets.txt", "w+") as file:
    print(file.read().split("\n"))
    for order in orders:
        file.write(f"One {order} coming right up!\n")

# r - Read
# w - Write
# a - Append
# x - eXclusive creation
# + - ???