# Creating a list (used as array in Python)
cars = ["Ford", "Volvo", "BMW"]
print("Initial cars list:", cars)

# Accessing an element
print("First car:", cars[0])

#  Modifying an element
cars[0] = "Toyota"
print("Modified first car:", cars)

#  Length of array/list
print("Total number of cars:", len(cars))

#  Looping through the list
print("All cars:")
for car in cars:
    print(car)

#  Adding an element
cars.append("Honda")
print("After appending Honda:", cars)

# Removing by index
cars.pop(1)  # Removes 2nd element
print("After popping index 1:", cars)

# Removing by value
cars.remove("BMW")  # Removes the value "BMW"
print("After removing BMW:", cars)

#  Using list methods
cars.append("Nissan")
cars.append("Toyota")
print("Updated cars list:", cars)

# clear() - removes all elements
copied_cars = cars.copy()  # copy the list
print("Copied list:", copied_cars)

print("Count of 'Toyota':", cars.count("Toyota"))  # Count of specific value

# extend() - add multiple elements
cars.extend(["Audi", "Mazda"])
print("After extending", cars)

# index() - find position of value
print("Index of 'Nissan':", cars.index("Nissan"))

# insert() - insert at specific position
cars.insert(2, "Hyundai")
print("After inserting Hyundai at index 2:", cars)

# reverse() - reverse the list
cars.reverse()
print("Reversed list:", cars)

# sort() - sort list alphabetically
cars.sort()
print("Sorted list:", cars)

# clear() - removes all items
cars.clear()
print("List after clear:", cars)
