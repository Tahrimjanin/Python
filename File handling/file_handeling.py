# 1.Create a new file(x mode) -if it doesn't exist, else raise an error
try:
    with open("myfile.txt", "x", encoding="utf-8") as f:
        f.write("This is a newly created file.\n")
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")
    
# 2.Write to a file(w mode) - overwriting existing content
with open("myfile.txt", "w", encoding="utf-8") as f:
    f.write("This file is overwritten with new content.\n")
print(" File overwritten.")

# 3.Append to a file(a mode) - adding new content
with open("myfile.txt", "a", encoding="utf-8") as f:
    f.write("This line is added using append mode.\n")
    f.write("Another line added.\n")
print(" Lines appended to file.")

# 4.Read from a file(r mode) - reading content
with open("myfile.txt", "r", encoding="utf-8") as f:
    print("\nFile Content:")
    print(f.read())
    
# 5.Read a file in binary mode(rb mode) - reading binary files (e.g., images)
try:
    with open("pic.jpg", "rb") as img_file:
        binary_data = img_file.read()
        print(f"\nImage read in binary mode. Size: {len(binary_data)} bytes.")
except FileNotFoundError:
    print("\n example.jpg image not found for binary read.")

