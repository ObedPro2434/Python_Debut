## Mini projet
"""Welcome to the first miniprojet! I am an application that takes a message and a letter from you.
My task is to coun how many times this letter occured and to calculate its percentage."""

user_name = input("Please enter your name : ")
user_message = input("Enter your message : ")
user_letter = input("Please enter a letter: ")
count = user_message.count(user_letter)
len_message = len(user_message)
perc = count/len_message * 100
print("The count of the letter ",user_letter,"is ", count,"and his percentage is ",perc)
