# ================================
# FILE HANDLING
# ================================

# --------------------------------
# 1. Opening Files
# --------------------------------

# open() is used to open a file.

# Syntax:
# open(filename, mode)

file = open("example.txt", "r")
file.close()


# --------------------------------
# 2. File Modes
# --------------------------------

# "r" -> Read Mode (Default)
# Opens an existing file for reading.
# Gives an error if the file does not exist.

file = open("example.txt", "r")
file.close()


# "w" -> Write Mode
# Creates a new file if it doesn't exist.
# Overwrites all existing data.

file = open("example.txt", "w")
file.write("Hello Python!")
file.close()


# "a" -> Append Mode
# Creates a new file if it doesn't exist.
# Adds data at the end without deleting old data.

file = open("example.txt", "a")
file.write("\nWelcome!")
file.close()


# --------------------------------
# 3. Reading Files
# --------------------------------

# read() -> Reads the entire file

file = open("example.txt", "r")
print(file.read())
file.close()


# readline() -> Reads one line at a time

file = open("example.txt", "r")
print(file.readline())
file.close()


# readlines() -> Reads all lines and returns a list

file = open("example.txt", "r")
print(file.readlines())
file.close()


# --------------------------------
# 4. Writing Files
# --------------------------------

# write() -> Writes a single string

file = open("example.txt", "w")
file.write("Python File Handling")
file.close()


# writelines() -> Writes multiple strings

lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

file = open("example.txt", "w")
file.writelines(lines)
file.close()


# --------------------------------
# 5. Context Manager
# --------------------------------

# with open() automatically closes the file.
# No need to use file.close().

with open("example.txt", "r") as file:
    print(file.read())


# Writing using with open()

with open("example.txt", "a") as file:
    file.write("\nHave a nice day!")