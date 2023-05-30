import discord # For discord
from discord.ext import commands # For discord commands and class

class Information(commands.Cog): # This is required to load the cog
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # Start a command
    async def ping(self, ctx): # This is a basic command
        await ctx.send("Pong!") # Return a message

async def setup(bot): # This is required to load the cog
    await bot.add_cog(Information(bot))