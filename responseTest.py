# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import string
import random
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    database='./db.sqlite3',
    read_only=True
)

# Get a response to the input text 'How are you?'
response = chatbot.get_response(random_string(16))

print(response)