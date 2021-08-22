list1 = ["A", "B", "C", "D"]
print(list1)
print(type(list1))

list2 = ["A", "B", 1, 2.0, ["A"], [], list(), True]
print(list2)
print(type(list2))

print(list2[0])
print(list2[-1])
print(list2[:9])
print(list2[::2])
print(list2[4][0])
print(list2[4][-1])

print(type(str(1+1)))

list1[0] = "Y"
print(list1)

del list1[0]
print(list1)

list1.insert(0, "A")
print(list1)

del list1[0]
print(list1)

list1 =["A"] + list1
print(list1)

list1.append("K")
print(list1)

print(min(list1))
print(max(list1))

print(list1.index("C"))
print(list1[list1.index("C")])

list1.reverse()
print(list1)

list1 = list1[::-1]
print(list1)

print(list1.count("A"))

list1.append("A")
print(list1.count("A"))

list1.pop()
print(list1)

list3 = ["O", "L", "M"]
print(list3)

list1.extend(list3)
print(list1)

list4 = [20, 5, 12, 9, 18, 6]
print(list4)

list4.sort()
print(list4)

list4.reverse()
print(list4)

list4.sort(reverse = True)
print(list4)

list5 = list4
print(list5)

list5[0] = "X"
print(list5)
print(list4)

list6 = list3.copy()
print(list6)

list6[0] = 12
print(list6)
print(list3)

list8 = [1, 2, 3]
print(list8)
print(list(map(float, list8)))