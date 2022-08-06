# the os module helps us access environment variables
# i.e., our API keys
import os

# these modules are for querying the Hugging Face model
import json
import requests

# the Discord Python API
import discord
from discord.ext import commands


from transformers import AutoModelWithLMHead, AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")


# this is my Hugging Face profile link
API_URL = 'https://api-inference.huggingface.co/models/a01709042/'
model_name = "DialoGPT-medium"

class Letobot(commands.Cog):

    def __init__(self, client):
        self.client = client
        super().__init__()
        self.api_endpoint = API_URL + model_name
        # retrieve the secret API token from the system environment
        huggingface_token = "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"
        # format the header in our request to Hugging Face
        self.request_headers = {
            'Authorization': 'Bearer {}'.format(huggingface_token)
        }


    def query(self, payload):
        """
        make request to the Hugging Face model API
        """
        data = json.dumps(payload)
        response = requests.request('POST',
                                    self.api_endpoint,
                                    headers=self.request_headers,
                                    data=data)
        ret = json.loads(response.content.decode('utf-8'))
        return ret

    async def on_ready(self):
        # send a request to the model without caring about the response
        # just so that the model wakes up and starts loading
        self.query({'inputs': {'text': 'Hello!'}})


    @commands.command()
    async def leto(self, ctx):
        msg = ctx.message.content.replace("$leto", "")
        bot_input_ids = tokenizer.encode(msg + tokenizer.eos_token, return_tensors='pt')

        chat_ids = model.generate(
            bot_input_ids, 
            max_length=1000, 
            top_k=50, 
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )

        messagebot = tokenizer.decode(chat_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        tosend = "no comment" if messagebot == "" else messagebot
        await ctx.channel.send(tosend)
        print('Message from {0.author}: {0.content}'.format(ctx.message))
        print('Message from bot {}'.format(tosend))

def setup(client):
    client.add_cog(Letobot(client))
    print("Succesfully loaded letobot module")