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

        with open("hasrun.txt", "r") as infile:
            state = infile.read()


            if len(infile.readlines()) > 1 :
                print("File has more than 1 line")

            if state == "True":
                self.client.hasrun = True
                
            elif state == "False":
                self.client.hasrun = False
            else:
                print('Debug Error: "hasrun.txt" does not contain matching boolean data')
                print(f"State = {state}")

        if self.client.hasrun == True:
            #load channelid array
            print("Client has been previously run... attempting to load database...")
            
            self.client.matrix = pickle.load(open("matrix.bin", "rb"))

            print("Validating loaded database")

            tempmatrix = pickle.load(open("matrix.bin", "rb"))
            if self.client.matrix == tempmatrix:
                print("Internal matrix matches pickle bin")

            if len(self.client.matrix) < 1:
                #inicializamos matriz o diccionario
                print("Something went wrong. self.client.matrix is empty... Initializing new matrix")

                for i in range(100):
                    self.client.matrix.append([0,"",0])

                print("Storing matrix into pickle bin directory")

                pickle.dump(self.client.matrix, open("matrix.bin", "wb"))

                print("Validating stored matrix")
                tempmatrix = pickle.load(open("matrix.bin", "rb"))
                if self.client.matrix == tempmatrix:
                    print("Internal matrix matches pickle bin")

                print("Matrix:")
                for i in range(len(self.client.matrix)):    
                    print(self.client.matrix[i])

            if len(self.client.matrix) != 100:
                print(f"Hmm... Weird... matrix lenght is not 100... matrix lenght is: {len(self.client.matrix)}")
            
            print("Matrix:")

            for i in range(len(self.client.matrix)):    
                print(self.client.matrix[i])

        if self.client.hasrun == False:
            self.client.hasrun = True
            print("Welcome to Atl Bot. \nInitializing...")
            print(f'Setting cog.init attribute self.client.hasrun to: "{self.client.hasrun}"...')
            with open("hasrun.txt", "w") as outfile:
                 outfile.write(f"{self.client.hasrun}")
            print("Completed")
            
            print("Validating Hasrun state...")
            with open("hasrun.txt", "r") as infile:
                state = infile.read()
                print(f"Hasrun.txt state = {state}")

            print("Creating new database matrix array...")
            for i in range(100):
                self.client.matrix.append([0,"",0])

            print("Completed.")

            print("Storing matrix into pickle bin directory")

            pickle.dump(self.client.matrix, open("matrix.bin", "wb"))

            print("Validating stored matrix")
            tempmatrix = pickle.load(open("matrix.bin", "rb"))
            if self.client.matrix == tempmatrix:
                print("Internal matrix matches pickle bin")

            print("Matrix:")

            for i in range(len(self.client.matrix)):    
                print(self.client.matrix[i])

        self.client.channelidlist = pickle.load(open("chats.bin", "rb"))
            



def setup(client):
    client.add_cog(Init(client))
    print("Succesfully loaded init module")
