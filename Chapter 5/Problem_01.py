# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!



words= {
    "Akash":"Sharma",
    "Varun":"Gupta",
    "Harsh":"Gupta"

}

# User se dictionary ki key input lena
word = input("Enter your Key Value: ")

# Aman key ki value print karna (Agar key nahi mili toh None aayega)
print(words.get("Aman"))

# User ne jo key enter ki hai, uski value print karna
print(words[word])



