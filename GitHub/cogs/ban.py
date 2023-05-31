# Import
import disnake
from disnake.ext import commands
from disnake import TextInputStyle

# Class
class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Ban
    @commands.slash_command()
    @commands.has_role("Admin")
    @commands.has_permissions(ban_members=True)
    async def ban(self, interaction, member: disnake.Member, reason):
        try:
            embed = disnake.Embed(title="You have been blocked on the OnlyChill server", description=f"Reason: {reason}", color=0xff0000)
            await member.send(embed=embed)
        except:
            pass
        await member.ban(reason=reason)
        embed = disnake.Embed(title="Ban", description=f" User {member} was banned.\nReason: {reason}", color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        embed = disnake.Embed(title="Ban", description=f"{interaction.author.mention} Blocked the user {member}\n Reason: {reason} ", color=0x00ff00)
        await interaction.guild.get_channel(id_logo_channel).send(embed=embed)

    @ban.error
    async def ban_error(self, interaction, error):
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
    bot.add_cog(Ban(bot))
    print("Ban cog load")