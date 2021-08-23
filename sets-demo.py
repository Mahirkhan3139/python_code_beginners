set1 = {"a", "b", "c"}
print(set1)
print(type(set1))
print(len(set1))

set2 = {"a", "a", "a"}
print(set2)
print(len(set2))

set3 = set(("a", "b", "c"))
print(set3)

set3.add("d")
print(set3)

set4 = {"a", 0, True}
set5 = {"b", 1, False}

set4.update(set5)
print(set4)

list1 = {4, 5, 6}
set3.update(list1)
print(set3)


set3.union(set3)
print(set3)

set3.discard(4)
print(set3)