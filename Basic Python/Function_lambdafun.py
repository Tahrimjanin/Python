# 1. Basic Function
def my_function():
    print("Hello from a function")
my_function()

# 2. Function with One Argument
def my_function(tahrim):
    print(tahrim+ " ABC")

my_function("tahrim")
my_function("janin")


# 3. Function with Two Arguments
def my_function(tahrim, janin):
    print(tahrim+ " " + janin)

my_function("Emil", "Refsnes")

# 4. Arbitrary Arguments (*args)
def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function("tahrim", "janin")

# 5. Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="abc", child2="bcd", child3="efg")

# 6. Arbitrary Keyword Arguments (**kwargs)
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

# 7. Default Parameter Value
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 8. Passing a List as Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# 9. Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# 10. The pass Statement
def myfunction():
    pass

# 11. Positional-Only Arguments
def my_function(x, /):
    print(x)

my_function(3)

# 12. Keyword-Only Arguments
def my_function(*, x):
    print(x)

my_function(x=3)

# 13. Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)

# 14. Recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

#LambdaFunction

# 1. A simple lambda function that adds 10 to the argument
x = lambda a: a + 10
print("Add 10:", x(5))  # Output: 15

# 2. A lambda function that multiplies two arguments
x = lambda a, b: a * b
print("Multiply:", x(5, 6))  # Output: 30

# 3. A lambda function that sums three arguments
x = lambda a, b, c: a + b + c
print("Sum:", x(5, 6, 2))  # Output: 13

# 4. Using lambda inside another function (function returns a lambda)

def myfunc(n):
    return lambda a: a * n

# 5. A function that always doubles the input
mydoubler = myfunc(2)
print("Double of 11:", mydoubler(11))  # Output: 22

# 6. A function that always triples the input
mytripler = myfunc(3)
print("Triple of 11:", mytripler(11))  # Output: 33

# 7. Using both doubler and tripler
print("Double of 11 again:", mydoubler(11))  # Output: 22
print("Triple of 11 again:", mytripler(11))  # Output: 33
