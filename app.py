from chatterbot import ChatBot
from flask import Flask
import os
import socket

app = Flask(__name__)

chatbot = ChatBot(
    'Latency Tester',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

@app.route("/<question>")
def response(question):
    response = chatbot.get_response(question)
    html = "{botname}: {response}"
    return html.format(botname=chatbot.name, response=response)

if __name__ == "__main__":
    # Train based on the english corpus
    chatbot.train("chatterbot.corpus.english")
    app.run(host='0.0.0.0', port=80)