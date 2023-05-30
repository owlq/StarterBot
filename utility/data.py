import discord, os # For discord, cog loading
from discord.ext import commands # For class

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prefix = kwargs.get("command_prefix")

    async def setup_hook(self):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{file[:-3]}")
                except Exception as e:
                    print(f"Error Loading: {file[:-3]} - {e}")

    async def on_message(self, message: discord.Message):
        if self.is_ready() or message.guild is None:
            await super().on_message(message)
        return