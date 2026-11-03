# 3. Check that a tuples type cannot be changed in python.  


# ==========================================
# PART 1: Creating a Tuple
# ==========================================

# Creating a tuple with different data types
my_tuple = ("Akash", 23, 23, 221, "Aman")

# Printing original tuple
print("Original Tuple:", my_tuple)


# ==========================================
# PART 2: Trying to Change Tuple Value
# ==========================================

# Trying to change the value at index 3
my_tuple[3] = "Sharma"

# Printing updated tuple
print("Updated Tuple:", my_tuple)


# ==========================================
# PART 3: Final Output / Explanation
# ==========================================

# Output:
# Original Tuple: ('Akash', 23, 23, 221, 'Aman')
# TypeError: 'tuple' object does not support item assignment

# Conclusion:
# Tuple cannot be changed after creation.
# Tuple is Immutable in Python.
# We cannot directly add, remove or modify tuple elements.