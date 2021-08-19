print("hello world")

string1 = "I'm bixby and\nI'm on a new line"
print(string1)
print(len(string1))

string2 = "mahir is the best boy"
string3 = "and he is 29 years old"

print("mahir" in string2)
print(string3.startswith("k"))
print(string2.index("boy"))
print(string2.upper())
print(string2.lower())

messy_string = "    messy string   "
print(messy_string)
print(messy_string.strip())
print(messy_string.split())
print(messy_string.replace("string", "example"))
print(messy_string.replace("string", "example").strip())

string4 = "I am a big boy"
print(string4.rjust(25))
print(string4.rjust(25, "x"))
print(string4.ljust(25, "x"))
print("{} {} {}".format(len(string2), 5.0, 0x12))
print("{0} {2} {1}".format(len(string2), 5.0, 0x12))
print("{length}".format(length=len(string3)))

length = len(string4)
print(f"string4 is {length} characters long!!")
print(f"string4 is {length:.2f} characters long!!")