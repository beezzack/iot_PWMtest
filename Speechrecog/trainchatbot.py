from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Hey Robot')
bot.set_trainer(ListTrainer)

for _file in os.listdir('corpus'):
    print(_file)
    chats = open('corpus/'+_file, 'r').readlines()
    bot.train(chats)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ',response)
