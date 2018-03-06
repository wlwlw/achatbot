from chatterbot import ChatBot
import sys
from threading import Thread

def trainThread(chatbot, length):
    print("start train "+chatbot.name)
    for i in range(length):
        chatbot.train("chatterbot.corpus.english")

if __name__ == "__main__":
    length = int(sys.argv[1])
    width = int(sys.argv[2])
    print("Run throughput with %d threads of size %d" % (width, length))
    threads = []
    for i in range(width):
        chatbot = ChatBot(
            'Throughput-bot-'+str(i),
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
        print("start " + chatbot.name)
        threads.append(Thread(target=trainThread, args=(chatbot, length), name=str(i)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
