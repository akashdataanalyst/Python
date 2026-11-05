# --------------------------------
# 1. Creating a Set
# --------------------------------

s2 = {12, 23, 2, 2, 21, 1, 21, 1, 2, 2, 212, 2, "Akash"}

print(s2, type(s2))

# Duplicate values automatically remove ho jaati hain.


# --------------------------------
# 2. add() - Adds one element
# --------------------------------

s2.add(232)

print(s2)

# 232 set mein add ho jayega.


# --------------------------------
# 3. update() - Adds multiple elements
# --------------------------------

s2.update([100, 200, 300])

print(s2)

# List ke saare elements set mein add ho jayenge.


# --------------------------------
# 4. remove() - Removes an element
# --------------------------------

s2.remove(23)

print(s2)

# 23 set se remove ho jayega.
# Agar element exist nahi karta toh KeyError nahi, KeyError ke bajay KeyError nahi balki KeyError? 
# Correct: KeyError nahi, KeyError ki jagah KeyError nahi; KeyError? 
# Set remove() missing element par KeyError nahi, KeyError ke bajay KeyError nahi: KeyError? 
# Python mein KeyError raise hota hai.


# --------------------------------
# 5. discard() - Removes an element
# --------------------------------

s2.discard(500)

print(s2)

# Element exist nahi karta toh bhi error nahi aayega.


# --------------------------------
# 6. pop() - Removes and returns an arbitrary element
# --------------------------------

removed = s2.pop()

print(removed)
print(s2)

# Koi bhi arbitrary element remove ho sakta hai.
# Kaunsa element remove hoga, ye guaranteed nahi hai.


# --------------------------------
# 7. len() - Returns total elements
# --------------------------------

print(len(s2))

# Set mein total unique elements count karega.


# --------------------------------
# 8. clear() - Removes all elements
# --------------------------------

# s2.clear()
# print(s2)

# Output: set()


# --------------------------------
# 9. copy() - Creates a shallow copy
# --------------------------------

new_set = s2.copy()

print(new_set)


# --------------------------------
# 10. union() - Combines two sets
# --------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

# Output: {1, 2, 3, 4, 5}
# Duplicate values automatically remove ho jaati hain.


# --------------------------------
# 11. intersection() - Returns common elements
# --------------------------------

print(a.intersection(b))

# Output: {3}
# Dono sets ke common elements return karega.


# --------------------------------
# 12. difference() - Returns elements in first set only
# --------------------------------

print(a.difference(b))

# Output: {1, 2}
# A mein hain, lekin B mein nahi.


# --------------------------------
# 13. symmetric_difference()
# --------------------------------

print(a.symmetric_difference(b))

# Output: {1, 2, 4, 5}
# Common elements ko chhodkar baaki elements return karega.


# ============================================
# PYTHON SET METHODS (14 TO 23)
# ============================================


# --------------------------------
# 14. isdisjoint() - Check karta hai ki dono sets mein koi common element nahi hai
# --------------------------------

e = {5, 6, 7}
f = {7, 8, 9}

# Check karega ki E aur F mein koi common element hai ya nahi
print(e.isdisjoint(f))

# Output: False
# False aaya kyunki dono sets mein 7 common hai.

# Ab F ko change karte hain
f = {11, 8, 9}

print(e.isdisjoint(f))

# Output: True
# True aaya kyunki E aur F mein ek bhi common element nahi hai.


# --------------------------------
# 15. issubset() - Check karta hai ki ek set ke saare elements doosre set mein hain ya nahi
# --------------------------------

x = {1, 2}
y = {1, 2, 3, 4}

# Check karega ki X ke saare elements Y mein present hain ya nahi
print(x.issubset(y))

# Output: True
# True aaya kyunki X ke 1 aur 2 dono elements Y mein hain.

# Ab X mein ek aisa element add karte hain jo Y mein nahi hai
x = {1, 5}

print(x.issubset(y))

# Output: False
# False aaya kyunki X mein 5 hai, lekin Y mein 5 nahi hai.


# --------------------------------
# 16. issuperset() - Check karta hai ki ek set mein doosre set ke saare elements hain ya nahi
# --------------------------------

x = {1, 2}
y = {1, 2, 3, 4}

# Check karega ki Y mein X ke saare elements present hain ya nahi
print(y.issuperset(x))

# Output: True
# True aaya kyunki Y mein X ke saare elements (1, 2) hain.

# Ab reverse karke check karte hain
print(x.issuperset(y))

# Output: False
# False aaya kyunki X mein Y ke saare elements nahi hain.
# X mein 3 aur 4 missing hain.


# --------------------------------
# 17. in - Check karta hai ki element set mein present hai ya nahi
# --------------------------------

a = {1, 2, 3, 4, 5}

# Check karega ki 2, A set mein present hai ya nahi
print(2 in a)

# Output: True
# True aaya kyunki 2, A set mein available hai.

print(10 in a)

# Output: False
# False aaya kyunki 10, A set mein available nahi hai.


# --------------------------------
# 18. not in - Check karta hai ki element set mein present nahi hai
# --------------------------------

a = {1, 2, 3, 4, 5}

# Check karega ki 10, A set mein nahi hai ya nahi
print(10 not in a)

# Output: True
# True aaya kyunki 10, A set mein available nahi hai.

print(2 not in a)

# Output: False
# False aaya kyunki 2, A set mein already present hai.


# --------------------------------
# 19. difference_update() - Common elements ko remove karta hai
# --------------------------------

c = {1, 2, 3, 4}
d = {3, 4, 5}

# Step 1: C aur D ke elements compare honge.
# Step 2: Jo elements dono sets mein common hain (3, 4), woh C se remove honge.
# Step 3: C mein sirf non-common elements bachenge.
# Step 4: Original set C modify ho jayega.

c.difference_update(d)

print(c)

# Output: {1, 2}
# 3 aur 4 dono sets mein common the, isliye C se remove ho gaye.


# --------------------------------
# 20. intersection_update() - Sirf common elements ko rakhta hai
# --------------------------------

c = {1, 2, 3, 4}
d = {3, 4, 5}

# Step 1: C aur D ke elements compare honge.
# Step 2: Jo elements dono sets mein common hain, unhe rakha jayega.
# Step 3: Baaki elements C se remove ho jayenge.
# Step 4: Original set C modify ho jayega.

c.intersection_update(d)

print(c)

# Output: {3, 4}
# Kyunki 3 aur 4 dono sets mein common hain.


# --------------------------------
# 21. symmetric_difference_update() - Common elements remove aur unique elements rakhta hai
# --------------------------------

c = {1, 2, 3, 4}
d = {3, 4, 5}

# Step 1: C aur D ke common elements find honge.
# Step 2: Common elements (3, 4) remove ho jayenge.
# Step 3: Unique elements (1, 2, 5) bachenge.
# Step 4: Original set C modify ho jayega.

c.symmetric_difference_update(d)

print(c)

# Output: {1, 2, 5}
# Dono sets ke sirf unique elements bachenge.
# Common elements 3 aur 4 remove ho gaye.


# --------------------------------
# 22. update() - Ek set ke elements doosre set mein add karta hai
# --------------------------------

c = {1, 2}
d = {3, 4}

# Step 1: D ke saare elements read honge.
# Step 2: D ke elements C mein add ho jayenge.
# Step 3: Agar koi element pehle se C mein hai toh duplicate nahi banega.
# Step 4: Original set C modify ho jayega.

c.update(d)

print(c)

# Output: {1, 2, 3, 4}


# Ek aur example common elements ke saath

c = {1, 2, 3}
d = {3, 4, 5}

c.update(d)

print(c)

# Output: {1, 2, 3, 4, 5}
# 3 dono sets mein tha, lekin set duplicate elements allow nahi karta.


# --------------------------------
# 23. Set Comparison Operators - Subset aur Superset check karna
# --------------------------------

x = {1, 2}
y = {1, 2, 3, 4}

# <= ka matlab hai: Kya X, Y ka subset hai?
print(x <= y)

# Output: True
# Kyunki X ke saare elements Y mein present hain.

# >= ka matlab hai: Kya Y, X ka superset hai?
print(y >= x)

# Output: True
# Kyunki Y mein X ke saare elements present hain.

# Ab reverse karke check karte hain
print(x >= y)

# Output: False
# Kyunki X mein Y ke saare elements present nahi hain.

print(y <= x)

# Output: False
# Kyunki Y ke saare elements X mein present nahi hain.

