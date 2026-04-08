#Activity 3.2.2 Step 7
from post import Post

# How will you save the posts you will create? Review the for loop 
# near the end of this code for an answer.
all_posts_archive = []

# What is the user name they want to use?
username = input("welcome, what is your username?")

# Welcome user to the program 
print("ok", username, "what do you want to do next?")

# Store initial user input in a variable identified by user_input

# You may need to use this statement again to complete the activity.

user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")

# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":
    
    # code for adding a post here
    if user_input == "add":
        message = input("what is the message")
        post1 = Post(username, message)
        all_posts_archive.append(post1)
        print(post1)
    # code for removing a post here
    elif user_input == "remove":
        (all_posts_archive) == ("EMPTY")
    # code for changing the current user here
    elif user_input == "change user":
        username = input("Ok, what is your new username?")
        print(username)
    # code to display all posts, you can use the code in comments below
    elif user_input == "print":
        for post in all_posts_archive:
            print (post)
    # code to inform the user that their input was not valid here
    else:
        print("please choose a valid option")
    # code that will allow the user to make a new selection
    # This code will finish the loop
    user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")