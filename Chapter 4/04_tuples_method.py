
# ==========================================================
# PYTHON TUPLE - COMPLETE NOTES
# ==========================================================


# 1. TUPLE CREATION
# Tuple multiple values ko ek variable mein store karta hai.

a = (3434, 23, 33.4, 3, 333, 3)

# type() se data type check karte hain
print(type(a))          # <class 'tuple'>

# Empty tuple
empty = ()
print(empty)            # ()

# Single element tuple
# Single value ke baad comma lagana zaroori hai
single = (10,)
print(single)           # (10,)

# Different data types ek tuple mein store kar sakte hain
mixed = (10, "Akash", 33.4, True)
print(mixed)


# ==========================================================
# 2. INDEXING
# ==========================================================

a = (10, 20, 30, 40, 50)

# Indexing 0 se start hoti hai
print(a[0])             # 10
print(a[1])             # 20
print(a[2])             # 30

# Negative indexing right side se start hoti hai
print(a[-1])            # 50
print(a[-2])            # 40
print(a[-3])            # 30

# a[0] ka matlab first value
# a[-1] ka matlab last value


# ==========================================================
# 3. SLICING
# Syntax: tuple[start : stop : step]
# Start include hota hai, stop include nahi hota.
# ==========================================================

a = (10, 20, 30, 40, 50)

# Index 1 se index 3 tak
print(a[1:4])           # (20, 30, 40)

# Beginning se index 2 tak
print(a[:3])            # (10, 20, 30)

# Index 2 se last tak
print(a[2:])            # (30, 40, 50)

# Har doosra element
print(a[::2])           # (10, 30, 50)

# Index 1 se har doosra element
print(a[1::2])          # (20, 40)

# Tuple reverse karna
print(a[::-1])          # (50, 40, 30, 20, 10)

# Reverse direction mein index 4 se index 2 tak
print(a[4:1:-1])        # (50, 40, 30)


# ==========================================================
# 4. CONCATENATION (+)
# Do tuples ko join karna
# ==========================================================

a = (10, 20, 30)
b = (40, 50)

c = a + b

print(c)                # (10, 20, 30, 40, 50)

# Original tuples change nahi hote
print(a)                # (10, 20, 30)
print(b)                # (40, 50)


# ==========================================================
# 5. REPETITION (*)
# Tuple ko multiple times repeat karna
# ==========================================================

a = (10, 20, 30)

print(a * 2)            # (10, 20, 30, 10, 20, 30)
print(a * 3)            # (10, 20, 30, 10, 20, 30, 10, 20, 30)
print(a * 0)            # ()


# ==========================================================
# 6. MEMBERSHIP (in / not in)
# Kisi value ko tuple mein check karna
# ==========================================================

a = (10, 20, 30)

# in: Value available hai ya nahi
print(20 in a)          # True
print(100 in a)         # False

# not in: Value available nahi hai ya nahi
print(20 not in a)      # False
print(100 not in a)     # True


# ==========================================================
# 7. UNPACKING
# Tuple ki values ko alag variables mein store karna
# ==========================================================

a = (10, 20, 30)

x, y, z = a

print(x)                # 10
print(y)                # 20
print(z)                # 30

# Extended unpacking
a = (10, 20, 30, 40, 50)

first, *middle, last = a

print(first)            # 10
print(middle)           # [20, 30, 40]
print(last)             # 50

# *middle remaining values ko list mein collect karta hai.


# ==========================================================
# 8. NESTED TUPLE
# Tuple ke andar tuple
# ==========================================================

a = ((10, 20), (30, 40))

print(a[0])             # (10, 20)
print(a[1])             # (30, 40)

# Inner tuple ki values access karna
print(a[0][0])          # 10
print(a[0][1])          # 20
print(a[1][0])          # 30
print(a[1][1])          # 40

# a[0][1]:
# Pehle a[0] = (10, 20)
# Phir [1] = 20


# ==========================================================
# 9. TUPLE KE ACTUAL METHODS
# Tuple mein sirf 2 built-in methods hote hain.
# ==========================================================

a = (3434, 23, 33.4, 3, 333, 3)


# METHOD 1: count()
# Kisi value ki total occurrence count karta hai.

countofakash = a.count(3)

print(countofakash)     # 2

# 3 tuple mein do baar available hai.

print(a.count(23))      # 1
print(a.count(100))     # 0


# METHOD 2: index()
# Kisi value ka index position return karta hai.

indexofakash = a.index(23)

print(indexofakash)     # 1

# Duplicate value hone par first occurrence ka index deta hai.

b = (10, 20, 30, 20, 40)

print(b.index(20))      # 1

# Starting index dekar search kar sakte hain.
print(b.index(20, 2))   # 3

# Value nahi milne par ValueError aata hai.
# print(b.index(100))


# ==========================================================
# 10. BUILT-IN FUNCTIONS
# Ye tuple ke methods nahi, Python ke built-in functions hain.
# ==========================================================

a = (3434, 23, 33.4, 3, 333, 3)


# 1. len()
# Tuple mein total elements count karta hai.

print(len(a))           # 6

# Duplicate values bhi count hoti hain.


# 2. max()
# Sabse badi value return karta hai.

print(max(a))           # 3434


# 3. min()
# Sabse chhoti value return karta hai.

print(min(a))           # 3


# 4. sum()
# Sabhi numeric values ka total karta hai.

print(sum(a))           # 3826.4

# 3434 + 23 + 33.4 + 3 + 333 + 3


# 5. sorted()
# Values ko ascending order mein sort karta hai.
# IMPORTANT: sorted() LIST return karta hai, tuple nahi.

print(sorted(a))
# [3, 3, 23, 33.4, 333, 3434]

# Descending order
print(sorted(a, reverse=True))

# Agar sorted tuple chahiye:
b = tuple(sorted(a))

print(b)                # (3, 3, 23, 33.4, 333, 3434)
print(type(b))          # <class 'tuple'>


# 6. tuple()
# List, string ya range ko tuple mein convert karta hai.

a = [10, 20, 30]

b = tuple(a)

print(b)                # (10, 20, 30)
print(type(b))          # <class 'tuple'>

# String conversion
print(tuple("AKASH"))
# ('A', 'K', 'A', 'S', 'H')

# Range conversion
print(tuple(range(1, 5)))
# (1, 2, 3, 4)


# 7. any()
# Agar ek bhi value True ho toh True return karta hai.

a = (0, 0, 10, 0)

print(any(a))           # True

# 10 non-zero hai, isliye True.

b = (0, 0, 0)

print(any(b))           # False

# Sabhi values zero hain.


# 8. all()
# Agar saari values True hon toh True return karta hai.

a = (10, 20, 30)

print(all(a))           # True

# Sabhi values non-zero hain.

b = (10, 0, 30)

print(all(b))           # False

# Ek value 0 hai, isliye False.

# Empty tuple ka special behaviour
print(any(()))          # False
print(all(()))          # True


# 9. reversed()
# Tuple ko reverse order mein iterate karta hai.
# reversed() khud tuple nahi, iterator return karta hai.

a = (10, 20, 30, 40)

b = reversed(a)

print(tuple(b))         # (40, 30, 20, 10)


# 10. enumerate()
# Index aur value dono ek saath deta hai.

a = (10, 20, 30)

for index, value in enumerate(a):
    print(index, value)

# Output:
# 0 10
# 1 20
# 2 30

# start=1 dene par index 1 se start hoga.

for index, value in enumerate(a, start=1):
    print(index, value)

# Output:
# 1 10
# 2 20
# 3 30


# ==========================================================
# 11. TUPLE IMMUTABLE HOTA HAI
# Existing tuple elements ko directly change nahi kar sakte.
# ==========================================================

a = (10, 20, 30)

# a[0] = 100
# Is line ko uncomment karne par TypeError aayega.

# Change karne ka tarika:
# Step 1: Tuple ko list mein convert karo.

b = list(a)

# Step 2: List ki value change karo.
b[0] = 100

# Step 3: List ko wapas tuple mein convert karo.
a = tuple(b)

print(a)                # (100, 20, 30)


# ==========================================================
# 12. QUICK REVISION
# ==========================================================

# Actual Tuple Methods:
# 1. count()  - Value kitni baar aayi hai.
# 2. index()  - Value ka index position.

# Built-in Functions:
# 1. len()       - Total elements
# 2. max()       - Maximum value
# 3. min()       - Minimum value
# 4. sum()       - Total sum
# 5. sorted()    - Sorting (returns list)
# 6. tuple()     - Convert iterable to tuple
# 7. any()       - At least one truthy value
# 8. all()       - All values truthy
# 9. reversed()  - Reverse iterator
# 10. enumerate()- Index and value together

# Tuple Operations:
# Indexing, Slicing, Concatenation, Repetition,
# Membership, Unpacking, Nested Tuple.

# IMPORTANT:
# Tuple ordered hota hai.
# Duplicate values allowed hain.
# Different data types allowed hain.
# Tuple immutable hota hai.

print("TUPLE COMPLETE!")
