import asyncio
import discord
from discord.ext import commands
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import pickle





class Chatter(commands.Cog):
    def __init__(self, client):
        self.client = client

    chatbot = ChatBot("Atl Bot",

    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        'chatterbot.logic.MathematicalEvaluation'
        #'chatterbot.logic.TimeLogicAdapter'
        
    ],
   
    database_uri='sqlite:///database.sqlite3'
    )



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def chatsetup(self,ctx):
        isnew = True
        for id in self.client.channelidlist:
            if ctx.channel.id == id:
                isnew = False
                await ctx.channel.send("This channel is already set up as a chatbot channel")

        if isnew:
            self.client.channelidlist.append(ctx.channel.id)
            pickle.dump(self.client.channelidlist, open("chats.bin", "wb"))
        
    @chatsetup.error
    async def setup_command_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"I'm sorry, {ctx.author.name}. I'm afraid I can't do that. \nYou need the following permissions to use this command: {error.missing_perms}. ")
    



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def chatremove(self,ctx):
        exists = True
        num = 0
        for id in self.client.channelidlist:

            if ctx.channel.id == id:
                exists = True
                self.client.channelidlist[num] = 0
                pickle.dump(self.client.channelidlist, open("chats.bin", "wb"))
            num = num + 1
                
            
        if exists == False:
            await ctx.channel.send("This channel is not already set up as a chatbot channel")

    @chatremove.error
    async def setup_command_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"I'm sorry, {ctx.author.name}. I'm afraid I can't do that. \nYou need the following permissions to use this command: {error.missing_perms}. ")
    


    @commands.Cog.listener()
    async def on_message(self, message):



        for id in self.client.channelidlist:
            if message.channel.id == id:

                if message.author == self.client.user:
                    return
                
                if (message.author.bot):
                    return

                if message.content.startswith('$'):
                    #await self.client.process_commands(message)
                    return

                try:
                    bot_input = self.chatbot.get_response(message.content)
                    await message.channel.send(bot_input)
                except(KeyboardInterrupt, EOFError, SystemExit):
                    await message.channel.send("There was an error, could not get response from Atl Bot")

    @commands.command()
    async def train(self,ctx):
        if ctx.author.id == 819344097247887470:
            trainer = ChatterBotCorpusTrainer(self.chatbot)
            trainer.train("chatterbot.corpus.english")

def setup(client):
    client.add_cog(Chatter(client))
    print("Succesfully loaded Chatterbot module")


