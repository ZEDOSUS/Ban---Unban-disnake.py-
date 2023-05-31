# Import 
import disnake
from disnake.ext import commands 

# Prefix
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='$', intents = disnake.Intents.all(), case_insensitive=True)  
bot.remove_command("help")
    
# Sun 
@bot.command()
async def sum(ctx, x: int, y: int):
    await ctx.send(x+y)

# Load cog
bot.load_extensions('cogs')

# Bot run
bot.run("Y_TOKEN")