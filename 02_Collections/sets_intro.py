car_parts = {"wheels", "doors", "exhaust"}
print(car_parts, type(car_parts))

car_parts.add("seats")
print(car_parts)

car_parts.add(7)
print(car_parts)

l = [1, 4, 2, 3, 4, 2, 2, 5, 3, 4, 1, 4, 3]
unique = list(set(l))

print(unique)

# # Frozen Set
#
# f = frozenset((1, 2, 3, 4))
# print(f)