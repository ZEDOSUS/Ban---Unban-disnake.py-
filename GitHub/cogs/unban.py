# Import
import disnake
from disnake.ext import commands
from disnake import TextInputStyle

# Class
class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Unban
    @commands.slash_command()
    @commands.has_role("Admin")
    @commands.has_permissions(ban_members=True)
    async def unban(self, interaction, member: disnake.User, reason=None):
        await interaction.guild.unban(member)
        embed = disnake.Embed(title="Unban", description=f"  {member} was unban.", color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        embed = disnake.Embed(title="Unban", description=f"{interaction.author.mention} Unblocked the user {member} ", color=0x00ff00)
        await interaction.guild.get_channel(id_logo_channel).send(embed=embed)

    @unban.error
    async def unban_error(self, interaction, error):
        if isinstance(error, commands.MissingPermissions):
            embed = disnake.Embed(description="You don't have enough rights to use this command", color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True) 
            
        elif isinstance(error, commands.MissingAnyRole):
            embed = disnake.Embed(description="You don't have enough rights to use this command", color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True) 
        else:
            embed = disnake.Embed(description="An unknown error has occurred", color=0xff0000)
            await interaction.response.send_message(embed=embed, ephemeral=True) 

def setup(bot):
    bot.add_cog(Unban(bot))
    print("Unban cog load")