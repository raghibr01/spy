# Importing datetime to display the chat time and date
from datetime import datetime

# made a class for spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        # Initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        # Count the number of words
        self.count = 0

# a class for chat_messages
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Ankit', 'Mr.', 20, 3)

friend_one = Spy('rohit', 'Mr.', 27, 4.8)
friend_two = Spy('aman', 'Mr.', 21, 4.7)
friend_three = Spy('suhani', 'Ms.', 27 , 4.5)

# List of friends
friends = [friend_one, friend_two, friend_three]
