import discord
import datetime

async def leave_fnc(interaction: discord.Interaction, mylist, mod):
    member = interaction.user

    if member.id in mylist:
        mylist.remove(member.id)
        embed = discord.Embed(title=f"{len(mylist)} membres dans la queue {mod}", description=f"{member.mention} a quitter la queue {mod}.", color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Tu n'est pas dans la queue.", ephemeral=True)
