# ================================
# MODULES & LIBRARIES (BASICS)
# ================================

# --------------------------------
# 1. Importing Modules
# --------------------------------

# A module is a Python file that contains
# functions, classes, and variables.
# Modules help organize and reuse code.

# Import the entire module

import math

print(math.sqrt(25))      # 5.0


# Import specific functions from a module

from math import sqrt, pi

print(sqrt(49))           # 7.0
print(pi)                 # 3.141592653589793


# Import a module with an alias

import math as m

print(m.factorial(5))     # 120


# --------------------------------
# 2. Built-in Modules
# --------------------------------

# Built-in modules come pre-installed with Python.
# No installation is required.


# --------------------------------
# math Module
# --------------------------------

# Used for mathematical operations.

import math

print(math.sqrt(16))      # Square Root
print(math.pow(2, 3))     # Power
print(math.ceil(4.2))     # Round Up
print(math.floor(4.8))    # Round Down
print(math.pi)            # Value of Pi


# --------------------------------
# random Module
# --------------------------------

# Used to generate random numbers or select random items.

import random

print(random.randint(1, 10))          # Random integer
print(random.choice(["A", "B", "C"])) # Random element


# --------------------------------
# datetime Module
# --------------------------------

# Used to work with date and time.

import datetime

today = datetime.datetime.now()

print(today)
print(today.date())
print(today.time())
print(today.year)


# --------------------------------
# os Module
# --------------------------------

# Used to interact with the operating system.

import os

print(os.getcwd())          # Current Working Directory

# Create a folder
# os.mkdir("NewFolder")

# Rename a folder/file
# os.rename("OldName", "NewName")

# Remove a folder
# os.rmdir("NewFolder")


# --------------------------------
# 3. Package Management
# --------------------------------

# pip is Python's package manager.
# It is used to install, update, and remove external libraries.


# Check pip version
# Command:
# pip --version


# --------------------------------
# 4. Installing External Libraries
# --------------------------------

# Install a package

# Command:
# pip install package_name

# Example:
# pip install numpy
# pip install pandas


# --------------------------------
# 5. Updating Packages
# --------------------------------

# Update an installed package

# Command:
# pip install --upgrade package_name

# Example:
# pip install --upgrade numpy


# --------------------------------
# 6. Uninstalling Packages
# --------------------------------

# Remove an installed package

# Command:
# pip uninstall package_name

# Example:
# pip uninstall numpy
