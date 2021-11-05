import discord
from discord.ext import commands
from discord_slash.context import SlashContext
from PassportBot.bot import bot, slash

@bot.command(name = 'generate')
async def generate(ctx: commands.Context):
    pass

@slash.slash(name="test3", description="asdsfsddgf", guild_ids=[878119580030074930])
async def test(ctx: SlashContext):
    embed = discord.Embed(title="Embed Test")
    await ctx.send(embed=embed)