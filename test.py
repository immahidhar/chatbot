from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'AuthBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    database_uri='sqlite:///database.sqlite3'
)

"""
trainer = ListTrainer(bot)

trainer.train([
    'Hi',
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])
"""

conv = open('movie_lines.txt', 'r').readlines()
trainer = ListTrainer(bot)
trainer.train(conv)

while True:
    try:
        bot_input = bot.get_response(input('You:'))
        print('AuthBot: ',bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break