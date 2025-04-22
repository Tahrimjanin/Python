print("\nArithmetic Operators")
x = 10
y = 5
print("x + y =", x + y)    # Add
print("x - y =", x - y)  # Sub
print("x * y =", x * y)  # Multi
print("x / y =", x / y) # Div
print("x % y =", x % y)  # Mod
print("x ** y =", x ** y) # Exponentiation
print("x // y =", x // y) # Floor division

print("\nAssignment Operators")
 
a = 10
a += 5
print("a += 5:", a)
a -= 3
print("a -= 3:", a)
a *= 2
print("a *= 2:", a)
a /= 4
print("a /= 4:", a)
a %= 3
print("a %= 3:", a)
a //= 2
print("a //= 2:", a)
a **= 3
print("a **= 3:", a)
a = 5
a &= 3
print("a &= 3:", a)
a |= 3
print("a |= 3:", a)
a ^= 2
print("a ^= 2:", a)
a >>= 1
print("a >>= 1:", a)
a <<= 2
print("a <<= 2:", a)

print("\nComparison Operators")

x = 10
y = 20
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

print("\nLogical Operators")
print( x < 15 and y > 15)
print( x < 15 or y < 15)
print(not(x < 15 and y > 15))

print("\nIdentity Operators")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)
print(x is z)
print(x is not z)

print("\n Membership Operators")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)
print("10 not in my_list:", 10 not in my_list)

print("\nBitwise Operators")
x = 5  # 0101
y = 3  # 0011
print("x & y =", x & y)#AND
print("x | y =", x | y)#OR
print("x ^ y =", x ^ y)#XOR
print("~x =", ~x) #NOT
print("x << 2 =", x << 2)#Left Shift
print("x >> 2 =", x >> 2)#Right Shift

print("\n Operator Precedence")
print("(6 + 3) - (6 + 3) =", (6 + 3) - (6 + 3))
print("100 + 5 * 3 =", 100 + 5 * 3)
print("5 + 4 - 7 + 3 =", 5 + 4 - 7 + 3)


print("\n Walrus Operator")
print(x := 7)
