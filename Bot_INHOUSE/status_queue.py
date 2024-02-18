import discord
import datetime

async def disp_stats(interaction: discord.Interaction, mylist, mod):
    participants = " ".join([f"<@{user_id}>" for user_id in mylist])

    embed = discord.Embed(title=f"Il y a {len(mylist)} membres dans la queue {mod}", description=participants, color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
    await interaction.response.send_message(embed=embed)
