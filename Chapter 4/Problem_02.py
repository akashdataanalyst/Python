# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.


# ==========================================
# PART 1: Using Individual Variables
# ==========================================

# Creating an empty list
marks = []

# Taking first student marks and adding to the list
marks1 =int(input("Enter Your Marks: "))
marks.append(marks1)

# Taking second student marks and adding to the list
marks2 =int(input("Enter Your Marks: "))
marks.append(marks2)

# Taking third student marks and adding to the list
marks3 =int(input("Enter Your Marks: "))
marks.append(marks3)

# Taking fourth student marks and adding to the list
marks4 =int(input("Enter Your Marks: "))
marks.append(marks4)

# Taking fifth student marks and adding to the list
marks5 =int(input("Enter Your Marks: "))
marks.append(marks5)

# Taking sixth student marks and adding to the list
marks6 =int(input("Enter Your Marks: "))
marks.append(marks6)

# Sorting marks in ascending order
marks.sort()

# Printing sorted marks list
print("This is sorted list:", marks)


# ==========================================
# PART 2: Using For Loop and If Condition
# ==========================================

# Creating an empty list
marks2 = []

# Defining how many students' marks we want to store
numberofstudents = 6

# Running loop 6 times
for i in range(numberofstudents):

    # Checking whether list contains less than 6 marks
    if len(marks2) < numberofstudents:

        # Taking marks from user
        m1 =int(input("Enter Your Marks: "))

        # Adding marks to the list
        marks2.append(m1)

# If loop completes normally, print Stop
else:
    print("Stop")

# Sorting marks in ascending order
marks2.sort()

# Printing final sorted marks list
print("This is your sorted list:", marks2)
