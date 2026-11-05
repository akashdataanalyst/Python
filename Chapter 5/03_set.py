# Empty Set create karne ke liye set() use karte hain.
# s = {} use nahi karna, kyunki ye empty dictionary create karega.

s = {}
print(type(s))  # Output: <class 'dict'>

e = set()
print(type(e))  # Output: <class 'set'>


# --------------------------------
# 1. Set Creation
# --------------------------------

# Set mein duplicate values automatically remove ho jaati hain.
# Set mein elements ka order fixed nahi hota.

set2 = {23, 2323, 2, 22, 2, 234}

print(set2)

# Output: {2, 22, 23, 234, 2323}


# --------------------------------
# 2. sum() - Returns sum of all elements
# --------------------------------

print(sum(set2))

# Output: 2604


# --------------------------------
# 3. Duplicate Values Automatically Remove
# --------------------------------

s2 = {12, 23, 2, 2, 21, 1, 21, 1, 2, 2, 212, 2}

print(s2)

# Output: {1, 2, 12, 21, 23, 212}
# Duplicate values automatically remove ho jaati hain.