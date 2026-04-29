import math
import random

#1 Built-in functions
numbers = [4, 9, -3, 16]

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Absolute:", abs(-10))
print("Round:", round(3.567, 2))
print("Power:", pow(2, 3))

#2 math module
print("\nSquare root:", math.sqrt(16))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Pi:", math.pi)
print("Sin(90 degrees):", math.sin(math.radians(90)))

#3 random module
print("\nRandom float:", random.random())
print("Random integer:", random.randint(1, 10))

items = ["apple", "banana", "cherry"]
print("Random choice:", random.choice(items))

random.shuffle(items)
print("Shuffled list:", items)