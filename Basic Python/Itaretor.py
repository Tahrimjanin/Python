# Basic iterator from a tuple
print("Iterator from Tuple:")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Iterator from a string
print("\nIterator from String:")
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through a tuple
print("\nLoop through Tuple:")
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# Looping through a string
print("\nLoop through String:")
mystr = "banana"
for x in mystr:
    print(x)

# Creating a custom iterator
print("\nCustom Iterator:")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
