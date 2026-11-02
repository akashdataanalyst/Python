
# ==================================================
# 1. LIST CREATE KARNA AUR PRINT KARNA
# ==================================================

# List mein different data types store kar sakte hain
my_list = ["Akash", "Aman", 23, 3.2, True, "Sweta"]

# Original list print karna
print("Original List:", my_list)

# Output:
# Original List: ['Akash', 'Aman', 23, 3.2, True, 'Sweta']


# ==================================================
# 2. append() - LAST MEIN VALUE ADD KARNA
# ==================================================

# List ke last mein "varun" add karna
my_list.append("varun")

# Updated list print karna
print("After append:", my_list)

# Output:
# After append: ['Akash', 'Aman', 23, 3.2, True, 'Sweta', 'varun']


# ==================================================
# 3. sort() - LIST KO SORT KARNA
# ==================================================

# Numbers ki list banana
l1 = [2, 1, 23, 2, 323, 2432, 3, 2, 24, 1]

# Numbers ko ascending order mein arrange karna
l1.sort()

# Sorted list print karna
print("Sorted List:", l1)

# Output:
# Sorted List: [1, 1, 2, 2, 2, 3, 23, 24, 323, 2432]


# ==================================================
# 4. reverse() - LIST KA ORDER REVERSE KARNA
# ==================================================

# Numbers ki list banana
l2 = [2, 1, 23, 2, 323, 2432, 3, 2, 24, 1]

# List ka existing order reverse karna
l2.reverse()

# Reversed list print karna
print("Reversed List:", l2)

# Output:
# Reversed List: [1, 24, 2, 3, 2432, 323, 2, 23, 1, 2]


# ==================================================
# 5. insert() - SPECIFIC INDEX PAR VALUE ADD KARNA
# ==================================================

# List banana
l3 = ["Akash", "Aman", "varun", 23]

# Index 2 par "Kartik" insert karna
l3.insert(2, "Kartik")

# Updated list print karna
print("After insert:", l3)

# Output:
# After insert: ['Akash', 'Aman', 'Kartik', 'varun', 23]


# ==================================================
# 6. pop() - INDEX SE ELEMENT REMOVE KARNA
# ==================================================

# List banana
list4 = ["Akash", "Aman", "varun", "Sahil"]

# Index 2 ka element remove karna
# pop() removed element ko return bhi karta hai
value = list4.pop(2)

# Removed value print karna
print("Removed Value:", value)

# Updated list print karna
print("Updated List:", list4)

# Output:
# Removed Value: varun
# Updated List: ['Akash', 'Aman', 'Sahil']


# ==================================================
# 7. pop() - REMOVED VALUE DIRECTLY PRINT KARNA
# ==================================================

# Company names ki list
list5 = ["calco", "grid", "Corelytics", "Ampug"]

# Index 2 ka element remove karke print karna
print("Popped Value:", list5.pop(2))

# Updated list print karna
print("After pop:", list5)

# Output:
# Popped Value: Corelytics
# After pop: ['calco', 'grid', 'Ampug']


# ==================================================
# 8. remove() - VALUE KE THROUGH ELEMENT DELETE KARNA
# ==================================================

# Mixed data types ki list
list6 = [23, 34, 0, "Aman", "Akasj"]

# "Aman" ko list se remove karna
list6.remove("Aman")

# Updated list print karna
print("After remove:", list6)

# Output:
# After remove: [23, 34, 0, 'Akasj']


# ==================================================
# 9. extend() - MULTIPLE ELEMENTS ADD KARNA
# ==================================================

# Original list
l7 = ["Akash", "Aman"]

# Ek saath multiple elements add karna
l7.extend(["Varun", "Sahil", "Kartik"])

# Updated list print karna
print("After extend:", l7)

# Output:
# After extend: ['Akash', 'Aman', 'Varun', 'Sahil', 'Kartik']


# ==================================================
# 10. index() - ELEMENT KA INDEX FIND KARNA
# ==================================================

# Names ki list
l8 = ["Akash", "Aman", "Varun", "Sahil"]

# "Varun" ka index find karna
print("Varun Index:", l8.index("Varun"))

# Output:
# Varun Index: 2


# ==================================================
# 11. count() - ELEMENT KITNI BAAR AAYA HAI
# ==================================================

# Numbers ki list
l9 = [10, 20, 10, 30, 10, 40]

# Number 10 ki occurrences count karna
print("Count of 10:", l9.count(10))

# Output:
# Count of 10: 3


# ==================================================
# 12. len() - LIST KI LENGTH FIND KARNA
# ==================================================

# List banana
l10 = ["Akash", "Aman", "Varun", "Sahil"]

# Total elements count karna
print("List Length:", len(l10))

# Output:
# List Length: 4


# ==================================================
# 13. clear() - SAARE ELEMENTS REMOVE KARNA
# ==================================================

# List banana
l11 = [10, 20, 30, 40]

# List ke saare elements remove karna
l11.clear()

# Empty list print karna
print("After clear:", l11)

# Output:
# After clear: []


# ==================================================
# 14. copy() - LIST KI SHALLOW COPY BANANA
# ==================================================

# Original list
l12 = ["Akash", "Aman", "Varun"]

# List ki separate shallow copy banana
l13 = l12.copy()

# Copy wali list mein change karna
l13.append("Sahil")

# Dono lists print karna
print("Original:", l12)
print("Copy:", l13)

# Output:
# Original: ['Akash', 'Aman', 'Varun']
# Copy: ['Akash', 'Aman', 'Varun', 'Sahil']


# ==================================================
# 15. del - INDEX SE ELEMENT DELETE KARNA
# ==================================================

# List banana
l14 = ["Akash", "Aman", "Varun", "Sahil"]

# Index 1 ka element delete karna
del l14[1]

# Updated list print karna
print("After del:", l14)

# Output:
# After del: ['Akash', 'Varun', 'Sahil']


# ==================================================
# 16. LIST SLICING - MULTIPLE ELEMENTS ACCESS KARNA
# ==================================================

# Numbers ki list
l15 = [10, 20, 30, 40, 50, 60]

# Index 1 se 3 tak ke elements lena
# Ending index 4 include nahi hota
print("Slice:", l15[1:4])

# Output:
# Slice: [20, 30, 40]


# Starting se index 2 tak elements lena
print("First Three:", l15[:3])

# Output:
# First Three: [10, 20, 30]


# Index 3 se last tak elements lena
print("From Index 3:", l15[3:])

# Output:
# From Index 3: [40, 50, 60]


# Puri list ki shallow copy banana
print("Full Slice:", l15[:])

# Output:
# Full Slice: [10, 20, 30, 40, 50, 60]


# ==================================================
# 17. LIST MUTABLE HAI - VALUE CHANGE KARNA
# ==================================================

# Original list
l16 = ["Akash", "Aman", "Varun"]

# Index 0 ki value change karna
l16[0] = "Rahul"

# Updated list print karna
print("Mutable List:", l16)

# Output:
# Mutable List: ['Rahul', 'Aman', 'Varun']


# ==================================================
# 18. STRING IMMUTABLE HAI - STRING CHANGE KARNA
# ==================================================

# Original string
name = "Akash"

# String ke first character ko change karne ki koshish
# Isse TypeError aayega, kyunki strings immutable hoti hain

# name[0] = "R"
# Output:
# TypeError: 'str' object does not support item assignment

# Nayi string banana ek valid tarika hai
name = "R" + name[1:]

# Nayi string print karna
print("New String:", name)

# Output:
# New String: Rkash


# ==================================================
# 19. LIST AUR STRING KA PRACTICAL COMPARISON
# ==================================================

# List banana
fruits = ["Apple", "Banana", "Mango"]

# List ke first element ko change karna
fruits[0] = "Orange"

# Updated list print karna
print("Changed List:", fruits)

# Output:
# Changed List: ['Orange', 'Banana', 'Mango']


# String banana
fruit = "Apple"

# String ko directly change nahi kar sakte
# Isliye ek nayi string create kar rahe hain
fruit = "O" + fruit[1:]

# Nayi string print karna
print("New Fruit String:", fruit)

# Output:
# New Fruit String: Opple