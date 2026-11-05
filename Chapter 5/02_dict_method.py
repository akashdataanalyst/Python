# Dictionary: Data ko Key-Value pair mein store karta hai
# Key unique honi chahiye, lekin values duplicate ho sakti hain.
# Key kisi bhi immutable data type ki ho sakti hai, jaise string, int, tuple.

marks = {
    "Akash": 86,
    "Aman": 34,
    "Rohan": 23,
    35: "Sharma"
}


# --------------------------------
# 1. items() - Returns all key-value pairs
# --------------------------------
print(marks.items())

# Output:
# dict_items([('Akash', 86), ('Aman', 34), ('Rohan', 23), (35, 'Sharma')])


# --------------------------------
# 2. values() - Returns all values
# --------------------------------
print(marks.values())

# Output:
# dict_values([86, 34, 23, 'Sharma'])


# --------------------------------
# 3. keys() - Returns all keys
# --------------------------------
print(marks.keys())

# Output:
# dict_keys(['Akash', 'Aman', 'Rohan', 35])


# --------------------------------
# 4. update() - Add new key-value or update existing value
# --------------------------------
marks.update({
    "Akash": 99,  # Existing key ki value update hogi
    "Rohit": 67    # New key-value pair add hoga
})

print(marks)


# --------------------------------
# 5. Access value using key
# --------------------------------
print(marks["Akash"])

# Output: 99


# --------------------------------
# 6. get() - Returns value if key exists, otherwise None
# --------------------------------
print(marks.get("Akash2"))

# Output: None

# Custom default value bhi de sakte hain
print(marks.get("Akash2", 0))

# Output: 0


# --------------------------------
# 7. Direct key access using []
# --------------------------------
# Key exist nahi karti toh KeyError aayega

# print(marks["Akash2"])  # KeyError


# --------------------------------
# 8. pop() - Removes key and returns its value
# --------------------------------
removed_value = marks.pop("Aman")

print(removed_value)  # 34
print(marks)          # Aman remove ho gaya


# --------------------------------
# 9. popitem() - Removes and returns last inserted pair
# --------------------------------
last_item = marks.popitem()

print(last_item)


# --------------------------------
# 10. setdefault() - Returns existing value or inserts new key
# --------------------------------
marks.setdefault("Ravi", 50)

print(marks)

# Ravi exist nahi karta tha, isliye add ho gaya.
# Agar Ravi pehle se hota toh uski existing value return hoti.


# --------------------------------
# 11. copy() - Creates a shallow copy of dictionary
# --------------------------------
new_marks = marks.copy()

print(new_marks)


# --------------------------------
# 12. fromkeys() - Creates dictionary from given keys
# --------------------------------
students = ["Akash", "Aman", "Rohan"]

new_dict = dict.fromkeys(students, 0)

print(new_dict)

# Output:
# {'Akash': 0, 'Aman': 0, 'Rohan': 0}


# --------------------------------
# 13. clear() - Removes all items
# --------------------------------

dict_2 = {
    "akash":34,
    "Rohan":54,
    "varun":65
}

dict_2.clear()
print(dict_2)
# Output: {}

print("Example 13")


# --------------------------------
# 14. len() - Returns total number of key-value pairs
# --------------------------------
print(len(marks))


# --------------------------------
# 15. in - Checks whether key exists
# --------------------------------
print("Akash" in marks)  # True
print("Rahul" in marks)  # False


# --------------------------------
# 16. del - Deletes a particular key-value pair
# --------------------------------
del marks["Rohan"]

print(marks)


# --------------------------------
# 17. Dictionary iteration using for loop
# --------------------------------

# Print only keys
for key in marks:
    print(key)

# Print only values
for value in marks.values():
    print(value)

# Print both keys and values
for key, value in marks.items():
    print(key, ":", value)