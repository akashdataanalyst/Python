# ==========================================
# PYTHON STRING AND STRING SLICING
# ==========================================

# String can be written using double quotes
name = "Akash"

# String can also be written using single quotes
name2 = 'Akash'

# Triple quotes are used for multiline strings
name3 = '''akash
sharma'''

print(name3)

# ==========================================
# STRING SLICING
# ==========================================

# Syntax:
# string[start_index : end_index]
#
# Start index is INCLUDED.
# End index is EXCLUDED.

# Example 1:
name4 = name[0:3]
print(name4)  # Output: Aka

# Explanation:
# Index 0 = A
# Index 1 = k
# Index 2 = a
# Index 3 = s (Excluded)


# Example 2:
print(name[0:])
# Output: Akash
# Start from index 0 and go till the end of the string.
# If end index is not given, Python takes the full length.


# Example 3:
print(name[:])
# Output: Akash
# If both start and end indices are not given,
# Python returns the complete string.


# Example 4:
print(name[:6])
# Output: Akash
# Start from index 0 by default.
# Go up to index 6 (excluding 6).
# Since the string length is 5, all characters are printed.


# Example 5:
print(name[-5:-1])
# Output: Akas
# Negative indexing:
# -5 = A
# -4 = k
# -3 = a
# -2 = s
# -1 = h (Excluded)