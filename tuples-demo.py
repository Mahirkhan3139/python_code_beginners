tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3, 4)
print(tuple_numbers)
print(type(tuple_numbers))

tuple_mixed = ("A", 1, 2,("A", "B"))
print(tuple_mixed)
print(type(tuple_mixed))

tuple_combine = ("combine ") * 4
print(tuple_combine)

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

print("item1" in tuple_items)
print("item4" in tuple_items)

print(tuple_items.index("item3"))

print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

print(len(item1))
print(tuple_items[-1])
print(tuple_items[-2])

print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])


string1 = "I am a boy"
print(string1[:6])
print(string1[-1])
print(string1[:-1])