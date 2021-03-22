#############################################################
#
#  BASIC PYTHON
#  @author: Antonio Scapellato
#
#  Book: Python - Everything to know to get started
#
#############################################################

# 1
print("Hello, World!")

# 2
integer = 1000
string = "1000"
float = 10.4567
complex = 1j

print(integer)
print(string)
print(float)
print(complex)

# 3
integer_to_string = str(integer)
string_to_integer = int(string)

# 4

string = "Hello, World!"
print(string[5])
print(string[5:8])

# 5

thislist = ["BMW", "Tesla", "Ferrari"]
print(thislist)
print(len(thislist))
print(type(mylist))

# 6

thisdict = {
  "brand": "Antonio Scapellato",
  "model": "Me",
  "year": 1999
}
print(thisdict)

# 7

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# 8

cars = ["Tesla", "Lamborghini", "Ferrari"]
for x in cars:
  print(x)
for x in "TESLA":
  print(x)


# 9

def my_function():
  print("Hello, World! This is a function")

my_function()

# 10

cars = ["Tesla", "Lamborghini", "BMW"]
print(cars[0])
cars[0] = "Toyota"
print(cars[0])

