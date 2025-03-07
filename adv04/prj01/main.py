import os


print(os.listdir())


with open("new_file.txt ","w")as f:
    f.write("Hello MicroPython")

print(os.listdir())


os.remove("new_file.txt")

print(os.listdir())