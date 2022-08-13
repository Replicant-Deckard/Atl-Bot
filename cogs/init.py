import discord
from discord.ext import commands
import pickle





class Init(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        print(f"We have logged in as {self.client.user}")

        activity = discord.Activity(name="How to Become Human", type=discord.ActivityType.watching)
        await self.client.change_presence(status=discord.Status.online, activity=activity)

        print("Welcome to Atl Bot. \nInitializing...")
        print("Ready")
            



def setup(client):
    client.add_cog(Init(client))
    print("Succesfully loaded init module")
