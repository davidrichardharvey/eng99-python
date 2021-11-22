# # Iterable
#
# # numbers = [1, 5, 435, 64, 565, 234]
# # print(len(numbers))
# #
# # for number in numbers:
# #     square = number ** 2
# #     print(square)
# #
# # print("Finished looping")
#
# d = {"name": "David", "profession": "trainer", "likes": ["pizza", "video games"]}
# for key, value in d.items():
#     if key == "likes":
#         for thing in value:
#             print(f"I like {thing}")
#     else:
#         print(f"My {key} is {value}")

menu = [
    {"food": "pizza", "price": 13.00},
    {"food": "burger", "price": 9.50},
    {"food": "chips", "price": 2.60}
]

# Calculate the total cost for 1 of each item in the menu
total = 0
for item in menu:
    price = item.get("price")
    if price:
        total += price

print(sum([item["price"] for item in menu])) # List Comprehension