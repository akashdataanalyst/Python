# 2. Write a program to fill in a letter template given below with name and date.
# letter
# Dear < | Name | >,
# You are selected!
# < | Date | >


latter = '''
Dear <|name|>, 
Your are Selected !
 <|Date|>'''

name = input("enter Your name :")
date = input("enter your Joining Date (DD-MM-YYYY):")
print(latter.replace("<|name|>",name).replace("<|Date|>",date))