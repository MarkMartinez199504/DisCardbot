import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
           guild = discord.Object(id=os.getenv('DEV_SERVER_ID'))
           synced = await self.tree.sync(guild=guild)
           print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = Client(command_prefix="lmao", intents=intents)

load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD_ID = discord.Object(id=os.getenv('DEV_SERVER_ID'))


@client.tree.command(name="hello", description="Say Hello!", guild=GUILD_ID)
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")



client.run(TOKEN)