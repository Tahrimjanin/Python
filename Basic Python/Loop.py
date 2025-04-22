# WHILE LOOP EXAMPLES

print("While Loop Basics")
i = 1
while i < 6:
    print(i)
    i += 1

print("While Loop with Break")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print(" While Loop with Continue")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("While Loop with Else")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# FOR LOOP EXAMPLES

print("\nFor Loop Through List")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("For Loop Through String ")
for x in "banana":
    print(x)

print("For Loop with Break (after print) ")
for x in fruits:
    print(x)
    if x == "banana":
        break

print("For Loop with Break (before print)")
for x in fruits:
    if x == "banana":
        break
    print(x)

print("For Loop with Continue ")
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("For Loop with range()")
for x in range(6):
    print(x)

print("For Loop with range(start, stop)")
for x in range(2, 6):
    print(x)

print("For Loop with range(start, stop, step)")
for x in range(2, 30, 3):
    print(x)

print("For Loop with Else")
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("For Loop with Break and Else")
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")  # Will not execute

print("Nested Loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

print("=== For Loop with Pass Statement ===")
for x in [0, 1, 2]:
    pass  # place holder
