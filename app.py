from chatterbot import ChatBot
from flask import Flask
import os
import socket

app = Flask(__name__)

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
#chatbot.get_response("Hello, how are you today?")
@app.route("/")
def hello():
    html = "<b>{botname} at {hostname}: </b> Hello {name}!"
    return html.format(botname=chatbot.name, hostname=socket.gethostname(), name=os.getenv("NAME", "world"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)