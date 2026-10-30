
# 4. Write a python program to print the contents of a directory using the os module.


# Directory ke contents print karne ka program

import os  # Operating system se related functions use karne ke liye os module import kiya

path = "."  # "." ka matlab current working directory hai

contents = os.listdir(path)  # Diye gaye folder ki files aur folders ke naam ki list banata hai

for item in contents:  # List ke har item ko ek-ek karke access karta hai
    print(item)  # Current item ka naam print karta hai



# Specific directory ke contents print karne ka program

print("Printing....")  # Screen par message print karta hai

import os  # Directory ke saath kaam karne ke liye os module import karta hai

path = r"C:\Users\Dell\Downloads"  # Target folder ka complete path store karta hai
# r ka matlab raw string hai, jo Windows path mein backslash ko handle karna aasan banata hai

contents = os.listdir(path)  # Specific folder ke andar ki files aur folders ki list banata hai

for item in contents:  # List ke har item par ek-ek karke loop chalata hai
    print(item)  # Har file ya folder ka naam alag line mein print karta hai
