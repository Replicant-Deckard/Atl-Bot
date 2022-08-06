import discord
from discord.ext import commands
import pickle

"""
channelid      message





"""


class Setup_command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["setup"])
    @commands.has_permissions(ban_members=True)
    async def setup_command(self,ctx,mode,*,rest="default"):
        if self.client.hasrun == True:
            self.client.matrix = pickle.load(open("matrix.bin", "rb"))
        print(f"mode: {mode}, rest: {rest}")
        channelid = ctx.message.channel.id
        occurences = []
        messageinput = rest
        line = 0
        #print(f"init values: channelid:{channelid} occurences: {occurences} messageinput: {messageinput} line: {line}")

        if rest.lower() == "default":
            messageinput = "Welcome. Remember to read <#627826099723829283> to know how to get verified, and to not ping mods, or you might be ignored as punishment. We also recommend reading the <#695730364563325128>. Thanks!"

        if mode.lower() == "add": 
            print ("mode = add")

            #search that channelid is not in collumn 1 of matrix
                #if channelid is already in collumn 1 of matrix
                    #error message

                #if channelid is not in collumn 1 of matrix
                    #append channelid to collumn 1 of matrix
                        #append messageinput to collumn 2 of matrix

            for i in range(len(self.client.matrix)):
                print(f"verifying... {i} out of {len(self.client.matrix)}...")
                if channelid == self.client.matrix[i][0]:
                    self.ctx.channel.send(f"ERROR: channelid {channelid} is already in collumn 1 of matrix in line {i}: {self.client.matrix[i]}")
                    occurences.append(i)
                    print(f"occurences: {occurences}")
                    return

            print(len(occurences))
            if len(occurences) == 0:
                print("Instances of channel id in array = 0")
                hasinserted = False
                i = 0
                while hasinserted == False:

                    print("inserting...")
                    if self.client.matrix[i][0] == 0:
                        self.client.matrix[i][0]=channelid
                        self.client.matrix[i][1]=messageinput
                        hasinserted = True
                        #line = i
                        print(f"inserted: {hasinserted} in line {i}")
                        await ctx.channel.send(f'Setup correct: I will now say "{self.client.matrix[i][1]}" in channel <#{self.client.matrix[i][0]}>')
                        print("Saving matrix in pickle bin...")
                        pickle.dump(self.client.matrix, open("matrix.bin", "wb"))
                    i = i + 1

                for i in range(len(self.client.matrix)):    
                    print(self.client.matrix[i])
                
                return
                    



        elif mode.lower() == "remove":
            print("mode = remove")
            occurences = []
            listlenght = len(self.client.channelidlist)
            print(f"list lenght= {listlenght}")

            #search that channelid is in collumn 1 of matrix
                #if channelid is not in collumn 1 of matrix
                    #error message

                #if channelid is in collumn 1 of matrix (store the i row number in row variable)
                    #delete channelid in collumn 1 of matrix in 
                        #delete messageinput in collumn 2 of matrix

            for h in range (len(self.client.matrix)):
                print (f"verifying... {h} out of {len(self.client.matrix)}: {self.client.matrix[h]}")

                if self.client.matrix[h][0] == channelid:
                    print(f"channelid is in collumn {h} of matrix")
                    occurences.append(h)
                    print(f"occurences: {occurences}")
                
            
             
            if len(occurences) == 0:
                print ("error, channelid is not in collumn 1 of matrix")

            elif len(occurences) > 1:
                print ("hmm... channelid is more than once in first collumn of matrix... Creating exception and purging...")
                occurences = [0]

            elif len(occurences) ==1:
                
                for i in range(len(self.client.matrix)):
                    if self.client.matrix[i][0] == channelid:
                        self.client.matrix[i] = [0,"",0]
                        print(f"succesfully deleted row: {i}")
                        
                        print("Saving matrix in pickle bin...")
                        pickle.dump(self.client.matrix, open("matrix.bin", "wb"))
                        await ctx.channel.send("Succesfully removed channel from on_message event coroutine")

                for i in range(len(self.client.matrix)):    
                    print(self.client.matrix[i])


            else:
                print("remove unsuccesful, no parameters met")

    @setup_command.error
    async def setup_command_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"I'm sorry, {ctx.author.name}. I'm afraid I can't do that. \nYou need the following permissions to use this command: {error.missing_perms}. ")
    


def setup(client):
    client.add_cog(Setup_command(client))
    print("Succesfully loaded Setup module")

        
        
