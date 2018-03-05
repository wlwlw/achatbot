from chatterbot import ChatBot
import sys

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

if __name__ == "__main__":
    count = int(sys.argv[1])
    for i in range(count):
        chatbot.train("chatterbot.corpus.english")