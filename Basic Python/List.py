#Access List Items****
#List - Ordered, Changeable, Allows Duplicates

print("List Example:")
fruits = ["apple", "banana", "cherry", "apple"]
print("List:", fruits)
fruits[1] = "mango"  # 2nd item change
fruits.append("orange") # add new item
print("Updated List:", fruits) 
print("Length of list:", len(fruits))
print("Type:", type(fruits))

#Tuple - Ordered, Unchangeable, Allows Duplicates
print("Tuple Example:")
numbers = (1, 2, 3, 2)
print("Tuple:", numbers)
print("Length of tuple:", len(numbers))
print("Type:", type(numbers))

#Set - Unordered, Unchangeable (items), No Duplicates
print("Set Example:")
fruits = {"apple", "banana", "cherry", "apple"}
print("Set (no duplicates):", fruits)
fruits.add("orange")  # add new item
fruits.discard("banana")  # remove item
print("Updated Set:", fruits)
print("Type:", type(fruits))

# Dictionary - Ordered, Changeable, No Duplicates
print("Dictionary Example:")
person = {
    "name": "Tahrim",
    "age": 22,
    "is_student": True
}
print("Dictionary:", person)
person["age"] = 21  # Change value
person["university"] = "KYAU"  # Add new key-value
print("Updated Dictionary:", person)
print("Type:", type(person))


#Change List Items***
# Initial List
thislist = ["apple", "banana", "cherry"]
print("\nOriginal List:", thislist)

#Change the second item (index 1)
thislist[1] = "blackcurrant"
print("Changed 2nd item:", thislist)

# Change a range of items (index 1 to 2 => "blackcurrant", "cherry")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  # 1:3 = index 1 to before 3
print("Changed range 1:3:", thislist)

# Insert more items than replaced
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print("Replaced 1 item with 2:", thislist)

# Insert less items than replaced
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(" Replaced 2 items with 1:", thislist)

# Insert item at specific index without replacing
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(" Inserted 'watermelon' at index 2:", thislist)


#Add List Items****
#Append Items
print(" \nAppend Example:")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")  # Adds "orange" at the end
print("After append:", thislist)

# Insert Items
print("\n Insert Example:")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # Inserts at index 1 (2nd position)
print("After insert:", thislist)

# Extend List with another list
print("\n🔹 Extend with another list:")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # Adds all items from tropical to thislist
print("After extend (list):", thislist)

# Extend List with a tuple
print("\n🔹 Extend with a tuple:")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)  # Adds items from tuple
print("After extend (tuple):", thislist)


#Remove List Items****
# Original List

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print("\nOriginal List:", thislist)

# remove() – removes the first item
thislist.remove("banana")
print("After remove('banana'):", thislist)

# pop(index) – removes item at a specific index
thislist.pop(2)  # Removes "kiwi"
print("After pop(2):", thislist)

# pop() – removes the last item
thislist.pop()
print("After pop():", thislist)

# del list[index] – removes specific index item
del thislist[0]  # Removes "apple"
print("After del thislist[0]:", thislist)

# del list – deletes entire list 
thislist = ["apple", "banana", "cherry"]
del thislist

# clear() – empties the list but keeps the list object
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("After clear():", thislist)  


#Loop Lists****
# Sample List
thislist = ["apple", "banana", "cherry"]

#  For Loop - Direct item access
print("\nFor Loop:")
for x in thislist:
    print(x)

# For Loop with Index
print("\nFor Loop with Index:")
for i in range(len(thislist)):
    print(thislist[i])

# While Loop
print("\nWhile Loop:")
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# List Comprehension*****

[print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# 1. Only fruits with "a"
with_b = [x for x in fruits if "b" in x]
print(" With 'b':", with_b)

# 2. Exclude "apple"
not_apple = [x for x in fruits if x != "apple"]
print("Not apple:", not_apple)

# 3. All fruits (no condition)
all_fruits = [x for x in fruits]
print("All fruits:", all_fruits)

# 4. Numbers 0 to 9
numbers = [x for x in range(10)]
print(" Numbers 0–9:", numbers)

# 5. Numbers less than 5
less_than_5 = [x for x in range(10) if x < 5]
print("Less than 5:", less_than_5)

# 6. Uppercase fruits
uppercase_fruits = [x.upper() for x in fruits]
print("Uppercase:", uppercase_fruits)

# 7. Replace all with 'hello'
all_hello = ['hello' for x in fruits]
print("All 'hello':", all_hello)

# 8. Replace "banana" with "orange"
replace_banana = [x if x != "banana" else "orange" for x in fruits]
print("Banana → Orange:", replace_banana)

#Sort Lists****
# 1. Sort list alphabetically 
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print("1. Alphabetical sort(A-Z):", fruits)

# 2. Sort list of numbers in ascending order
numbers = [100, 50, 65, 82, 23]
numbers.sort()
print("2. Number sort (ascending):", numbers)

# 3. Sort list in descending order (Z-A)
fruits_desc = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits_desc.sort(reverse=True)
print("3. Alphabetical sort (Z-A):", fruits_desc)

# 4. Sort numbers in descending order
numbers_desc = [100, 50, 65, 82, 23]
numbers_desc.sort(reverse=True)
print("4. Number sort (descending):", numbers_desc)

# 5. Custom sort: sort numbers based on closeness to 50
def myfunc(n):
    return abs(n - 50)

custom_sort = [100, 50, 65, 82, 23]
custom_sort.sort(key=myfunc)
print("5. Sort by closeness to 50:", custom_sort)

# 6. Case-sensitive alphabetical sort (uppercase comes first)
case_sensitive = ["banana", "Orange", "Kiwi", "cherry"]
case_sensitive.sort()
print("6. Case-sensitive sort:", case_sensitive)

# 7. Case-insensitive sort using str.lower as key
case_insensitive = ["banana", "Orange", "Kiwi", "cherry"]
case_insensitive.sort(key=str.lower)
print("7. Case-insensitive sort:", case_insensitive)

# 8. Reverse the order of list elements (does not sort, just reverses current order)
reverse_list = ["banana", "Orange", "Kiwi", "cherry"]
reverse_list.reverse()
print("8. Reversed order (no sorting):", reverse_list)


#Copy Lists****

# This creates a new list with the same elements as the original(copy())
list1 = ["apple", "banana", "cherry"]
copy1 = list1.copy()
print("1. Copy using copy() method:", copy1)

# This also creates a new list by converting the existing list into a new one(list())
list2 = ["apple", "banana", "cherry"]
copy2 = list(list2)
print("2. Copy using list() constructor:", copy2)

# This copies all the elements of the list from start to end(slicing [:])
list3 = ["apple", "banana", "cherry"]
copy3 = list3[:]
print("3. Copy using slicing [:] operator:", copy3)

# This is not an actual copy — it only creates a new reference to the same list
list4 = ["apple", "banana", "cherry"]
reference = list4
list4.append("mango")  
print("4. Wrong way (reference):", reference)


#join list
# This creates a new list by combining list1 and list2( Using the + operator)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
joined_list1 = list1 + list2
print("1. Joined using + operator:", joined_list1)

# This adds each item from list2 to list1 one by one(loop with append())
list3 = ["a", "b", "c"]
list4 = [1, 2, 3]
for x in list4:
    list3.append(x)
print("2. Joined using for loop + append():", list3)


# This adds all elements of list2 to the end of list1( the extend())
list5 = ["a", "b", "c"]
list6 = [1, 2, 3]
list5.extend(list6)
print("3. Joined using extend() method:", list5)

