# Python String Slicing - Skip Value (Step)

name = "Akash Sharma"

# Syntax:
# string[start : end : step]


# 1. Skip 1 (Default Step)
print(name[::1])
# Output: Akash Sharma


# # 2. Skip 2
print(name[::2])
# # Output: Aahsam


# # 3. Skip 3
print(name[::3])
# # Output: AsSr


# # 4. Start from index 1 and Skip 3
print(name[1::3])
# # Output: khhm


#Akash Sharma # 5. Start from index 2 and Skip 2
print(name[2::2])
# # Output: ahSam


# Akash Sharma# 6. Start from index 1, End at 15, Skip 2
print(name[1:len(name):2])
# # Output: ks hra


#Akash Sharma # 7. Reverse String
print(name[::-1])
# # Output: amrahS hsakA


#Akash Sharma # 8. Reverse and Skip 2
print(name[::-2])
# # Output: arh sk


#Akash Sharma # 9. Reverse and Skip 3
print(name[::-3])
#output : aa a

#Akash Sharma# 10. Negative Start and Negative Step
print(name[-1::-2])
# # Output: arh sk


# # 11. Negative Start, End and Step
print(name[-1:-10:-2])
# # Output: arh s


# Akash Sharma 12. Negative start , End with Negative ,Positive skip
print(name[::1])
#Output: Akash sharma

# Akash Sharma 13. Negative start , End with Negative ,Positive skip
print(name[-10:-2:2])
#Output: ahSa
