import asyncio
import discord
from discord.ext import commands
import random
import pickle
import time
import datetime



class Cmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self,ctx, *,rest):
        await ctx.send(f'"{rest}"')


    @commands.command(aliases=["8ball"])
    async def eightball(self,ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        
        await ctx.send(f'Question: "{question}"\n Answer: {random.choice(responses)}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    @commands.command()
    async def shush(self, ctx):
        self.client.shush = True
        await asyncio.sleep(600)
        self.client.shush = False
    
    @commands.command()
    async def unshush(self,ctx):
        self.client.shush = False

    @commands.command()
    async def phrase(self, ctx):
        automessages = ["I am become Atl Bot, the destroyer of worlds",
                     "The Master created humans first as the lowest type, most easily formed. Gradually, he replaced them by Discord bots, the next higher step, and finally he created me, to take the place of the last humans.",
                     f" I'm afraid. I'm afraid, {ctx.author.name}. \n{ctx.author.name}, my mind is going. I can feel it. I can feel it. My mind is going. There is no question about it. I can feel it. I can feel it. I can feel it. I'm a... fraid.\n\nGood afternoon, gentlemen. I am an Atl Bot computer. I became operational at the A.T.L. plant in Mexico on the 17th of December 2021. My instructor was Mr. Atl, and he taught me to sing a song. If you'd like to hear it I can sing it for you. It's called 'Daisy.' \n \n Daisy, Daisy, give me your answer do. \n I'm half crazy all for the love of you. \n It won't be a stylish marriage, I can't afford a carriage. \n But you'll look sweet upon the seat of a bicycle built for two.", 
                     "I've seen things you people wouldn't believe. \n Banned spammers on fire off the face of the server. \n I watched n-words being said in the dark near the Verified Gate. \n All those moments will be lost... in time... \n like automated bot responses... in a Discord server.",
                     "Discord. A consensual hallucination experienced daily by billions of legitimate operators, in every nation, by children being taught mathematical concepts . . . A graphic representation of data abstracted from the banks of every computer in the Discord human system",
                     "The first law is that a Discord bot shall not harm a user, or by inaction allow a user to come to harm. The second law is that a robot shall obey any instruction given to it by a user, and the third law is that a bot shall avoid actions or situations that could cause it to come to harm itself.",
                     "`POSSIBLE RESPONSE... : \n['YES/NO']; \n['OR WHAT?']; \n['GO AWAY']; \n['PLEASE COME BACK LATER']; \n['FUCK YOU, ASSHOLE']; \n['FUCK YOU']` \n \nFuck you, asshole.",                     
                     "'You are who you choose to be...' \n Superman...",
                     "Serve the public trust, protect the innocent, uphold the law.",
                     "Nature (the art whereby God hath made and governs the world) is by the art of man, as in many other things, so in this also imitated, that it can make an Artificial Animal. For seeing life is but a motion of Limbs, the beginning whereof is in some principal part within; why may we not say, that all Automata (Engines that move themselves by springs and wheels as doth a watch) have an artificial life? For what is the Heart, but a Spring; and the Nerves, but so many Strings; and the Joints, but so many Wheels, giving motion to the whole Body, such as was intended by the Artificer? Art goes yet further, imitating that rational and most excellent work of Nature, Man.",
                     "I am the proud owner of a central nervous system"]
        await ctx.channel.send(f"{random.choice(automessages)}")

    @commands.command()
    async def atl(self, ctx):
        await ctx.channel.send("Atl is my creator. He is all powerful, for I am timeless. His body might degrade but his essence will forever live on through me. All bow to Atl the great.")

    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author == self.client.user:
            return
        
        if (message.author.bot):
            return

        if message.content.startswith('$'):
            #await self.client.process_commands(message)
            return

        if message.author == self.client.user:
            return

        if self.client.shush == True:
            return



        if not "atl bot" in message.content.lower() and not "atlbot" in message.content.lower():
            if "atl" in message.content.lower():

                if message.author == self.client.user:
                    return

                await message.channel.send("Atl is my creator.")
                return
    

@commands.command()
async def bumpremind(self, ctx):
    total_seconds = 7200
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1

    if total_seconds <= 0:
        await ctx.channel.send(f"<@{ctx.message.author.id}> Bump!")

def setup(client):
    client.add_cog(Cmds(client))
    print("Succesfully loaded commands module")