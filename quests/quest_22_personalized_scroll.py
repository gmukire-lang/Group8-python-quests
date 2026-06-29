def personalized_greeting(name, quest):
    print(f"Dear {name},you'll go on a quest to {quest}.")

user_name = input("Enter Name: ")
user_quest = input("Enter Quest: ")

personalized_greeting(user_name, user_quest)
