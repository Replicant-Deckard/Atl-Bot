import discord
from discord.ext import commands
import pandas as pd
import re
import asyncio
import datetime



class Dataset(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild = discord.Guild

      
    @commands.command()
    async def dataset(self,ctx,rest=50000,*,name="data"):
        async with ctx.typing():
            if ctx.author.id == 819344097247887470:
                data = [
                    ["name","message"] 
                ]

                

                emoji= ":new_moon:"
                sent = await ctx.send(f"Collecting data...{emoji}")  
                cont = 0
                nummes = 0
                thismessage = 0
                lastmessage = 0
                thismessagecontent = ""
                lastmessagecontent = ""
                """firstmsg = await ctx.fetch_message()"""

                async for msg in ctx.channel.history(limit=rest, oldest_first =True): 
                #async for msg in ctx.channel.history(limit=rest, oldest_first =True, after=firstmsg): <- If you wanna set a limit for the oldest message
                    cont = cont + 1
                    """if cont > 50000:
                        break"""
                    


                    thismessage = msg.author.id
                    percent = (cont/rest) * 100

                    if percent%1 ==0:
                        if cont == (float(rest)*0.25):
                            emoji = ":waning_crescent_moon:"
                        if cont == (float(rest)*0.5 ):
                            emoji =":last_quarter_moon:"
                        if cont == (float(rest)*0.75 ):
                            emoji=":waning_gibbous_moon:"
                        if cont == (float(rest)*0.9 ): 
                            emoji=":full_moon: finalizing..."

                        
                        await sent.edit(content=f"Collecting data... {percent}% {emoji} \nParsed {cont} out of {rest}. \nAppended {nummes}.")

                    content = msg.content
                    content = re.sub(r'http\S+', '', content)
                    content = re.sub("[<].*[>]", "", content)
                    content = " ".join(content.split())
                    hascommand = False
                    prefixes = ["!",
                                    "?",
                                    "-",
                                    ".",
                                    "$"]

                    for prefix in prefixes:
                        if (content.startswith(prefix)):
                            hascommand = True

                    if msg.author != self.client.user: 
                        if msg.author.bot == False:
                            if content != "" and content !=" ":
                                if hascommand ==False:
                                    print(thismessage,lastmessage)
                                    if thismessage != lastmessage:
                                        line = content
                                        data.append([msg.author.name, line]) 
                                        nummes = nummes + 1

                                    elif thismessage == lastmessage:
                                        #print(f"{lastmessagecontent}")
                                        line = f"{lastmessageline}. {content}"
                                        data[nummes]=[msg.author.name, line]
                                        
                                    lastmessage = thismessage
                                    lastmessageline = line


                await sent.edit(content="Completed collecting data... :full_moon_with_face: Writing file... ")


                with open(ctx.channel.name +".txt", "w", encoding="utf-8") as outfile:
                
                    for i in range(len(data)):
                        outfile.write(f"{data[i][1]} \n")
                        #outfile.write(f"{data[i][0]}: {data[i][1]} \n")
                    await sent.edit(content=f"Completed collecting data... :full_moon_with_face: Writing file... {i} out of {len(data)}")
                    
                await sent.edit(content=f"Completed collecting data... :full_moon_with_face: Finished writing file!")
            else:
                await ctx.send("RESTRICTED COMMAND")
                return
            

        


def setup(client):
    client.add_cog(Dataset(client))
    print("Succesfully loaded Dataset module")