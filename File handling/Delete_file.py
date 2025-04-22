import os
import shutil

# Nmae of the files and folder to be deleted
filename = "Examplefile.txt"
image_file = "image.jpg"
foldername = "Example Folder"


# 1️. General file delete (os.remove)
if os.path.exists(filename):
    os.remove(filename)
    print(f"File '{filename}' deleted.")
else:
    print(f" File '{filename}' does not exist.")
    
    
# 2.️ Image file delete (os.remove)
if os.path.exists(image_file):
    os.remove(image_file)
    print(f"Image file '{image_file}' deleted.")
else:
    print(f"Image file '{image_file}' not found.")


# 3.Folder delete 
if os.path.exists(foldername):
    try:
        os.rmdir(foldername)  # Try to remove the folder
        print(f"Empty folder '{foldername}' deleted.")
    except OSError:
        # If the folder is not empty, handle the exception
        print(f"Folder '{foldername}' is not empty. Using shutil to remove...")
        shutil.rmtree(foldername)
        print(f"Folder '{foldername}' and all contents deleted.")
else:
    print(f"Folder '{foldername}' does not exist.")

