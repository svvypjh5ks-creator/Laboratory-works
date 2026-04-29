#1 Generator for squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i * i

print("Squares up to 5:")
for value in square_generator(5):
    print(value)


#2 Even numbers between 0 and n (comma separated)
n = int(input("Enter n for even numbers: "))
even_gen = (str(i) for i in range(n + 1) if i % 2 == 0)
print("Even numbers:", ",".join(even_gen))


#3 Numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Divisible by 3 and 4 up to 100:")
for num in divisible_by_3_and_4(100):
    print(num)


#4 Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

print("Squares from 3 to 7:")
for value in squares(3, 7):
    print(value)


#5 Generator from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for num in countdown(5):
    print(num)