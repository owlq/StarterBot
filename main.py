import discord  # For discord
from utility.data import Bot # This loads the cogs
import logging # Shows important information of something goes wrong in the connection
from utility.config import token # This loads the token from the config file

bot = Bot(
    intents=discord.Intents.all(),
    command_prefix='!',
    case_insensitive=True,
    owner_id="Your ID",
    activity=discord.Streaming(
        name = "STATUS",
        url = "https://www.twitch.tv/twitch"
    ),
    allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=False, users=True, roles=False)
)

logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print(f"-----\nlogged in as: {bot.user} : {bot.user.id}\n-----")


bot.run(token, reconnect=True)
