valid = True
not_valid = False
print(valid)
print(not_valid)

valid == True
not_valid == True
print(valid)
print(not_valid)

print(valid != True)
print(not_valid != True)

print(not valid)
print(not not_valid)

print("-----------")

print((10 == 10) == True)
print((10 != 10) == True)

print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)

print("----------")

print(bool(0))
print(bool(1))


print(bool(0) == True)
print(bool(1) == False)

print(bool(0) != True)
print(bool(1) != False)

print(10 / 10)
print(10 // 10)
print(10 * 10)
print(10 ** 10)
print(10 % 10)
print(10 % 5)

mahir = 5 % 10 ;
print(mahir)
a = 5
b = 10
ans = b % a
print(ans)

x = 10
x = x + 10
print(x)

x += 10
print(x)

x -= 10
print(x)

print(bin(x) [2:].rjust(4, "0"))