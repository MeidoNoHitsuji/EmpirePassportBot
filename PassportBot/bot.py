import discord

from discord.ext import commands
from discord.ext.commands.cog import Cog
from discord_slash import SlashCommand, SlashContext, cog_ext

import logging
logger = logging.getLogger('discord_slash')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

command_prefix = '-'

class PassportBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'We have logged in as {self.user}')


intents = discord.Intents.all()
bot = PassportBot(command_prefix = command_prefix, intents = intents)
# bot.remove_command("help")

slash = SlashCommand(bot)

class Slash(Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test2", description="asdas", guild_ids=[878119580030074930])
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="Embed Test")
        await ctx.send(embed=embed)

bot.add_cog(Slash(bot))