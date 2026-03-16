

print('Hello world')

print("5" * 5)

name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter Your Age: "))

if age >= 18:
    print("You are Eligible to vote")
else: 
    print(" You are not Elligible to vote")


scores = int(input("input your scores: "))


if scores >= 70 and scores<=100 :
    print("You belong to the Grade A")
elif scores>= 50 and scores <=69 :
    print("You belong to Grade B")
elif scores < 50 or scores >= 0:
    print("You belong to Grade C and You have failed the exam")
else: 
    print("the Scores not Known ")

# ==  equal
# !=  not equal
# >   greater
# <   less
# >=  greater or equal
# <=  less or equal

# and
# or
# not

# Looops

for i in range(5):
    print(i)

b = 0

for i in range(5):
    print(i)
    for b in range(0) :
        print(b[i])

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

i = 1

while i <= 5:
    print(i)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p = Person("Tresor")
p.greet()

for i in range(0,5):
    print("*" * i)