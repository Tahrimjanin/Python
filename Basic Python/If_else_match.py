# 1. if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

# 2. if_elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# 3. if_elif_else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# 4. if_else
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# 5. short hand if
a = 200
b = 33
if a > b: print("a is greater than b")

# 6. short hand if_else
a = 2
b = 330
print("A") if a > b else print("B")

# 7. nested short hand
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# 8. and operator
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# 9. or operator
if a > b or a > c:
    print("At least one condition is True")

# 10. not operator
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# 11. nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# 12. pass
a = 33
b = 200
if b > a:
    pass ## This does nothing, avoids error when block is empty

#Match statement

# Python match-case statement demonstration

day = 3
month = 4


match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")

    case _:
        print("Invalid day number")

print("---")

# Match with default (_) value
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

print("---")

# Match with combined values using |
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

print("---")

# Match with guard (if) conditions
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
