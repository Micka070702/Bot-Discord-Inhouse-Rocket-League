import discord
import datetime
import random

from logs_generator import generate_log

async def _queue_1v1(interaction: discord.Interaction, client, clear_queue, queue_list):
    member = interaction.user

    if member.id not in queue_list:
        queue_list.append(member.id)
        embed = discord.Embed(title=f"{len(queue_list)} membres dans la liste 1v1", description=f"{member.mention} a rejoint la queue.", color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("You are already registered in the queue.", ephemeral=True)

    if len(queue_list) == 2:
        await send_is_full_message(interaction, client, clear_queue, queue_list, "1v1")



async def _queue_2v2(interaction: discord.Interaction, client, clear_queue, queue_list):
    member = interaction.user

    if member.id not in queue_list:
        queue_list.append(member.id)
        embed = discord.Embed(title=f"{len(queue_list)} membres dans la liste 2v2", description=f"{member.mention} a rejoint la queue.", color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("You are already registered in the queue.", ephemeral=True)

    if len(queue_list) == 4:
        await send_is_full_message(interaction, client, clear_queue, queue_list, "2v2")



async def _queue_3v3(interaction: discord.Interaction, client, clear_queue, queue_list):
    member = interaction.user

    if member.id not in queue_list:
        queue_list.append(member.id)
        embed = discord.Embed(title=f"{len(queue_list)} membres dans la liste 3v3", description=f"{member.mention} a rejoint la queue.", color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("You are already registered in the queue.", ephemeral=True)

    if len(queue_list) == 6:
        await send_is_full_message(interaction, client, clear_queue, queue_list, "2v2")




async def send_is_full_message(interaction, client, clear_queue, queue_list, mod):
    participants = " ".join([f"<@{user_id}>" for user_id in queue_list])

    embed = discord.Embed(title=f"Nous avons atteint les {len(queue_list)} membres dans la queue {mod}!", description="Les logs vous sont envoyés en MP", color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Membres participants: ", value=participants, inline=False)

    game_creator = random.choice(queue_list)
    embed.add_field(name="Créateur de la game: ", value=f"<@{game_creator}>", inline=False)

    member = interaction.guild.get_member(game_creator)
    if member:
        bot_permissions = interaction.guild.me.permissions_in(member)
        if bot_permissions.send_messages:
            await member.send("Vous avez été désigné comme créateur de partie, à vous !")
        else:
            clear_queue(queue_list)
            await interaction.response.send_message(f"{member.mention} ne peut pas recevoir de messages privés.")

    logs = generate_log()

    for user_id in queue_list:
        member = interaction.guild.get_member(user_id)
        if member:
            bot_permissions = interaction.guild.me.permissions_in(member)
            if bot_permissions.send_messages:
                await member.send(str(logs))
            else:
                clear_queue(queue_list)
                await interaction.response.send_message(f"{member.mention} ne peut pas recevoir de messages privés.")

    random.shuffle(queue_list)

    middle_index = len(queue_list) // 2
    team_red = queue_list[:middle_index]
    team_blue = queue_list[middle_index:]

    team_red_mentions = " ".join([f"<@{user_id}>" for user_id in team_red])
    team_blue_mentions = " ".join([f"<@{user_id}>" for user_id in team_blue])

    embed.add_field(name="Équipe Rouge: ", value=team_red_mentions, inline=False)
    embed.add_field(name="Équipe Bleue: ", value=team_blue_mentions, inline=False)

    await interaction.followup.send(embed=embed)
    await clear_queue(queue_list)


