import os
from dotenv import load_dotenv

load_dotenv() #Костыльно, можно найти решение куда лучше

from PassportBot import configs, bot
from PassportBot.bot import bot

def run(): 
    bot.run(configs.DISCORD_TOKEN)

if __name__ == '__main__':
    run()