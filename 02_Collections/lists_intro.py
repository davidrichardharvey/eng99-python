shopping_list = ["eggs", "bread", "cheese", "milk"]

print(shopping_list, type(shopping_list))

eggs = shopping_list[0]

print(shopping_list[2:])

shopping_list[1] = "bananas"
print(shopping_list)

shopping_list.append("doughnuts")
shopping_list.append("chocolate")
shopping_list.append("cheese")
print(shopping_list)
shopping_list.remove("cheese")
print(shopping_list)

shopping_list.sort()
print(shopping_list)

print(shopping_list.pop().upper())
print(shopping_list.pop().upper())
print(shopping_list.pop().upper())
print(shopping_list.pop().upper())
print(shopping_list)

mixed = [1, 2, 4.535, None, False, "Hello!"]
print(mixed)

nested = [
    [1, 2, 3],
    [1, 2, 3]
]
print(nested)

print(nested[1][2])