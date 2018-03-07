from chatterbot import ChatBot
import sys
from threading import Thread
import string
import random

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

def trainThread(i, length):
    chatbot = ChatBot(
        'Throughput-bot-'+str(i),
        trainer='chatterbot.trainers.ListTrainer'
    )
    print("start train "+chatbot.name)
    trainSet = [random_string(16) for i in range(length)]
    for i in range(length):
        chatbot.train(trainSet)

if __name__ == "__main__":
    length = int(sys.argv[1])
    width = int(sys.argv[2])
    print("Run throughput with %d threads of size %d" % (width, length))
    threads = []
    for i in range(width):
        threads.append(Thread(target=trainThread, args=(i, length), name=str(i)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
