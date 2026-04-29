#1 Iterator example

my_list = [1, 2, 3, 4, 5]

my_iter = iter(my_list)

print("Iterator output:")
print(next(my_iter))
print(next(my_iter))


#2 Create custom iterator 

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


print("\nCustom Iterator:")
my_class = MyNumbers()
for num in my_class:
    print(num)


#3 Generator function

def my_generator():
    for i in range(1, 6):
        yield i


print("\nGenerator Function:")
for value in my_generator():
    print(value)


#4 Generator expression

gen_exp = (x * x for x in range(5))

print("\nGenerator Expression:")
for value in gen_exp:
    print(value)