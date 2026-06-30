import os

current_dir = os.getcwd()
print("Current Directory:", current_dir)

new_dir = os.listdir(current_dir)
print("Files in directory:", new_dir)