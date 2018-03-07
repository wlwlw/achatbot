# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import string
import random
import sys
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    database="english.db",
    read_only=True
)

# Get a response to the input text
try:
	question = sys.argv[1]
except IndexError:
	question = random_string(16)
	
response = chatbot.get_response(question)

print(response)