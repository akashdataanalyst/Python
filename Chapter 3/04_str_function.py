# =====================================
# 1. upper() - Convert into uppercase
# =====================================

name = "akash sharma"

print(name.upper())  # you can also use like this print("Akash".upper())
# Output: AKASH SHARMA


# =====================================
# 2. lower() - Convert into lowercase
# =====================================

name = "AKASH SHARMA"

print(name.lower())
# Output: akash sharma


# =====================================
# 3. capitalize() - First letter capital
# =====================================

name = "akash sharma"

print(name.capitalize())
# Output: Akash sharma


# =====================================
# 4. title() - First letter of each word capital
# =====================================

name = "akash sharma"

print(name.title()) 
# Output: Akash Sharma


# =====================================
# 5. swapcase() - Reverse letter cases
# =====================================

name = "Akash Sharma"

print(name.swapcase())
# Output: aKASH sHARMA


# =====================================
# 6. strip() - Remove spaces from both sides
# =====================================

name = "   Akash Sharma   "

print(name.strip())
# Output: Akash Sharma


# =====================================
# 7. lstrip() - Remove spaces from left side
# =====================================

name = "   Akash"

print(name.lstrip())
# Output: Akash


# =====================================
# 8. rstrip() - Remove spaces from right side
# =====================================

name = "Akash   "

print(name.rstrip())
# Output: Akash


# =====================================
# 9. replace() - Replace text All matching value Replace
# =====================================

name = "Hello Akash"

print(name.replace("Akash", "Rahul"))
# Output: Hello Rahul


# =====================================
# 10. split() - Convert string into a list
# =====================================

name = "Akash Sharma"

print(name.split())
# Output: ['Akash', 'Sharma']


# =====================================
# 11. join() - Convert list into a string
# =====================================

names = ["Akash", "Rahul", "Amit"]

print(" ".join(names))
# Output: Akash Rahul Amit


# =====================================
# 12. find() - Find the position of text Case synstive
# =====================================

name = "Hello Akash"

print(name.find("Akash"))
# Output: 6

# If text is not found, find() returns -1


# =====================================
# 13. count() - Count occurrences
# =====================================

name = "banana"

print(name.count("a"))
# Output: 3


# =====================================
# 14. startswith() - Check starting text
# =====================================

name = "Python Programming"

print(name.startswith("Python"))
# Output: True


# =====================================
# 15. endswith() - Check ending text
# =====================================

name = "Python Programming"

print(name.endswith("Programming"))
# Output: True


# =====================================
# 16. isalpha() - Check alphabets only A-Z
# =====================================

name = "Akash"

print(name.isalpha())
# Output: True

# Spaces and numbers are not allowed


# =====================================
# 17. isdigit() - Check digits only
# =====================================

number = "12345"

print(number.isdigit())
# Output: True


# =====================================
# 18. isalnum() - Check letters and numbers
# =====================================

name = "Akash123"

print(name.isalnum())
# Output: True

# Spaces and special characters are not allowed


# =====================================
# 19. isspace() - Check whitespace only
# =====================================

name = "   "

print(name.isspace())
# Output: True


# =====================================
# 20. len() - Find string length
# =====================================

name = "Akash"

print(len(name))
# Output: 5


# =====================================
# 21. center() - Center-align a string
# =====================================

name = "Hi"

print(name.center(6, "-"))
# Output: --Hi--

# 6 = Total width of the string
# "-" = Character used to fill empty spaces

text = "Hey"
print(text.center(30+len(text)+30,"-"))


# =====================================
# 22. ljust() - Left-align a string
# =====================================

name = "Hi"

print(name.ljust(6, "-"))
# Output: Hi----

# The string stays on the left


# =====================================
# 23. rjust() - Right-align a string
# =====================================

name = "Hi"

print(name.rjust(6, "-"))
# Output: ----Hi

# The string stays on the right


# =====================================
# 24. zfill() - Add zeros to the left
# =====================================

number = "25"

print(number.zfill(5))
# Output: 00025

# 5 = Total width of the string


# =====================================
# 25. partition() - Split into three parts
# =====================================

text = "a-b-c"

print(text.partition("-"))
# Output: ('a', '-', 'b-c')

# Returns a tuple containing:
# 1. Text before the first separator
# 2. The separator itself
# 3. Text after the first separator


# =====================================
# 26. rsplit() - Split from the right side
# =====================================

text = "a-b-c"

print(text.rsplit("-", 1))
# Output: ['a-b', 'c']

# 1 = Maximum number of splits
# Splitting starts from the right side


# =====================================
# 27. removeprefix() - Remove a prefix
# =====================================

text = "Hello.py"

print(text.removeprefix("Hello"))
# Output: .py

# Removes "Hello" only if it appears at the beginning


# =====================================
# 28. removesuffix() - Remove a suffix
# =====================================

text = "Hello.py"

print(text.removesuffix(".py"))
# Output: Hello

# Removes ".py" only if it appears at the end