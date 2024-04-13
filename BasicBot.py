from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

#logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    database_uri='sqlite:///database-basicBot.sqlite3'
)

# "./cornell_movie-dialogs_corpus/movie_lines.txt"

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.english",
    #"chatterbot.corpus.telugu",
    #"chatterbot.corpus.hindi"
)

while True:
    try:
        bot_input = bot.get_response(input('> '))
        print('Bot> ', bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
