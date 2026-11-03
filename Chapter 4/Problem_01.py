# 1. Write a program to store seven fruits in a list entered by the user.

# ==========================================
# PART 1: Using Individual Variables
# ==========================================

# Creating an empty list
lists = []

# Taking first fruit input and adding it to the list
f1 = input("Enter Your Fruit : ")
lists.append(f1)

# Printing updated list
print(lists)

# Taking second fruit input and adding it to the list
f2 = input("Enter Your Fruit : ")
lists.append(f2)

# Printing updated list
print(lists)

# Taking third fruit input and adding it to the list
f3 = input("Enter Your Fruit : ")
lists.append(f3)

# Printing updated list
print(lists)

# Taking fourth fruit input and adding it to the list
f4 = input("Enter Your Fruit : ")
lists.append(f4)

# Printing updated list
print(lists)

# Taking fifth fruit input and adding it to the list
f5 = input("Enter Your Fruit : ")
lists.append(f5)

# Printing updated list
print(lists)

# Taking sixth fruit input and adding it to the list
f6 = input("Enter Your Fruit : ")
lists.append(f6)

# Printing updated list
print(lists)


# ==========================================
# PART 2: Using For Loop and If Condition
# ==========================================

# Creating an empty list
lists2 = []

# Defining how many fruits we want to store
numberoffruits = 7

# Running loop 7 times
for i in range(7):

    # Checking whether list contains less than 7 fruits
    if len(lists2) < 7:

        # Taking fruit name from user
        fruits = input("Enter Your Fruits:")

        # Adding fruit to the list
        lists2.append(fruits)

# If loop completes, print Stop
else:
    print("Stop")

# Printing final list
print(lists2)