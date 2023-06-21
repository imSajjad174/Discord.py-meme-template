import discord
import requests
import random
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)




@bot.command()
async def memetemplate(ctx):
    """Generates a random meme."""
    try:
        response = requests.get('https://api.imgflip.com/get_memes')
        data = response.json()
        memes = data['data']['memes']
        random_meme = random.choice(memes)
        meme_url = random_meme['url']
        
        embed = discord.Embed()
        embed.set_image(url=meme_url)
        
        message = await ctx.send(embed=embed)
        await message.add_reaction('👍') 
        await message.add_reaction('👎')  
        
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')


  
  
  
  
  
@bot.event
async def on_slash_command_error(ctx, ex):
    await ctx.send(str(ex))

bot.run(TOKEN)
