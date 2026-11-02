
# 1. Tuple with multiple integer values
a = (1, 2, 3, 4, 5)

print(type(a))  # <class 'tuple'>


# 2. Empty Tuple
# Empty tuple banane ke liye empty parentheses use karte hain
b = ()

print(type(b))  # <class 'tuple'>


# 3. Single value without comma
# Sirf parentheses lagane se tuple nahi banta
# Python ise integer samajhta hai
c = (1)

print(type(c))  # <class 'int'>


# 4. Single Element Tuple
# Single value tuple banane ke liye comma (,) zaroori hai
d = (1,)

print(type(d))  # <class 'tuple'>


# 5. Mixed Data Type Tuple
# Tuple mein different data types store kar sakte hain
# Integer, Float, String aur Boolean
# Duplicate values bhi allowed hain
e = ("Akash", 23, 33.4, True, "Akash")

print(type(e))  # <class 'tuple'>
print(e)        # ('Akash', 23, 33.4, True, 'Akash')


# 6. Tuple is Immutable
# Tuple ki existing value ko directly change nahi kar sakte
# Neeche wala code execute karne par TypeError aayega

# e[0] = "Aman"

# Error:
# TypeError: 'tuple' object does not support item assignment


# 7. Tuple values ko access kar sakte hain
print(e[0])  # Akash
print(e[1])  # 23
print(e[-1]) # Akash
