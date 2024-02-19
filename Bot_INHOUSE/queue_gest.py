import discord
import datetime

from queues import _queue_1v1
from queues import _queue_2v2
from queues import _queue_3v3
from leave_queue import leave_fnc
from status_queue import disp_stats

bronze_silver_gold_1v1 = []
bronze_silver_gold_2v2 = []
bronze_silver_gold_3v3 = []

plat_d1_d2_1v1 = []
plat_d1_d2_2v2 = []
plat_d1_d2_3v3 = []

d3_c1_c2_1v1 = []
d3_c1_c2_2v2 = []
d3_c1_c2_3v3 = []

c3_gc1_gc2_1v1 = []
c3_gc1_gc2_2v2 = []
c3_gc1_gc2_3v3 = []

gc3_ssl_1v1 = []
gc3_ssl_2v2 = []
gc3_ssl_3v3 = []


async def queue(interaction: discord.Interaction, client, clear_queue, mod):
    member = interaction.user
    if mod == "1v1":
        await queue_1v1(interaction, client, clear_queue)
    elif mod == "2v2":
        await queue_2v2(interaction, client, clear_queue)
    elif mod == "3v3":
        await queue_3v3(interaction, client, clear_queue)

async def what_is_my_1v1_elo_queue(interaction: discord.Interaction):
    member = interaction.user
    role_list = member.roles

    for role in role_list:
        if role.name == "Bronze 1" or role.name == "Bronze 2" or role.name == "Bronze 3" or\
                role.name == "Silver 1" or role.name == "Silver 2" or role.name == "Silver 3" or\
                    role.name == "Gold 1" or role.name == "Gold 2" or role.name == "Gold 3":
                        return (bronze_silver_gold_1v1)
        elif role.name == "Plat 1" or role.name == "Plat 2" or role.name == "Plat 3" or\
                role.name == "Diamant 1" or role.name == "Diamant 2":
                    return (plat_d1_d2_1v1)
        elif role.name == "Diamant 3" or role.name == "Champion 1" or role.name == "Champion 2":
                return (d3_c1_c2_1v1)
        elif role.name == "Champion 3" or role.name == "GC 1" or role.name == "GC 2":
                return (c3_gc1_gc2_1v1)
        elif role.name == "GC 3" or role.name == "SSL":
                return (gc3_ssl_1v1)

async def what_is_my_2v2_elo_queue(interaction: discord.Interaction):
    member = interaction.user
    role_list = member.roles

    for role in role_list:
        if role.name == "Bronze 1" or role.name == "Bronze 2" or role.name == "Bronze 3" or\
                role.name == "Silver 1" or role.name == "Silver 2" or role.name == "Silver 3" or\
                    role.name == "Gold 1" or role.name == "Gold 2" or role.name == "Gold 3":
                        return (bronze_silver_gold_2v2)
        elif role.name == "Plat 1" or role.name == "Plat 2" or role.name == "Plat 3" or\
                role.name == "Diamant 1" or role.name == "Diamant 2":
                    return (plat_d1_d2_2v2)
        elif role.name == "Diamant 3" or role.name == "Champion 1" or role.name == "Champion 2":
                return (d3_c1_c2_2v2)
        elif role.name == "Champion 3" or role.name == "GC 1" or role.name == "GC 2":
                return (c3_gc1_gc2_2v2)
        elif role.name == "GC 3" or role.name == "SSL":
                return (gc3_ssl_2v2)

async def what_is_my_3v3_elo_queue(interaction: discord.Interaction):
    member = interaction.user
    role_list = member.roles

    for role in role_list:
        if role.name == "Bronze 1" or role.name == "Bronze 2" or role.name == "Bronze 3" or\
                role.name == "Silver 1" or role.name == "Silver 2" or role.name == "Silver 3" or\
                    role.name == "Gold 1" or role.name == "Gold 2" or role.name == "Gold 3":
                        return (bronze_silver_gold_3v3)
        elif role.name == "Plat 1" or role.name == "Plat 2" or role.name == "Plat 3" or\
                role.name == "Diamant 1" or role.name == "Diamant 2":
                    return (plat_d1_d2_3v3)
        elif role.name == "Diamant 3" or role.name == "Champion 1" or role.name == "Champion 2":
                return (d3_c1_c2_3v3)
        elif role.name == "Champion 3" or role.name == "GC 1" or role.name == "GC 2":
                return (c3_gc1_gc2_3v3)
        elif role.name == "GC 3" or role.name == "SSL":
                return (gc3_ssl_3v3)



async def queue_1v1(interaction: discord.Interaction, client, clear_queue):
    member = interaction.user
    my_elo_queue = await what_is_my_1v1_elo_queue(interaction)

    await _queue_1v1(interaction, client, clear_queue, my_elo_queue)


async def queue_2v2(interaction: discord.Interaction, client, clear_queue):
    member = interaction.user
    my_elo_queue = await what_is_my_2v2_elo_queue(interaction)

    await _queue_2v2(interaction, client, clear_queue, my_elo_queue)


async def queue_3v3(interaction: discord.Interaction, client, clear_queue):
    member = interaction.user
    my_elo_queue = await what_is_my_3v3_elo_queue(interaction)

    await _queue_3v3(interaction, client, clear_queue, my_elo_queue)


async def leave_queue(interaction: discord.Interaction, mod):
    my_elo_queue1v1 = await what_is_my_1v1_elo_queue(interaction)
    my_elo_queue2v2 = await what_is_my_2v2_elo_queue(interaction)
    my_elo_queue3v3 = await what_is_my_3v3_elo_queue(interaction)

    if mod == "1v1":
        await leave_fnc(interaction, my_elo_queue1v1, mod)
    elif mod == "2v2":
        await leave_fnc(interaction, my_elo_queue2v2, mod)
    elif mod == "3v3":
        await leave_fnc(interaction, my_elo_queue3v3, mod)


async def display_status(interaction: discord.Interaction, mod):
    my_elo_queue1v1 = await what_is_my_1v1_elo_queue(interaction)
    my_elo_queue2v2 = await what_is_my_2v2_elo_queue(interaction)
    my_elo_queue3v3 = await what_is_my_3v3_elo_queue(interaction)
    member = interaction.user
    role_list = member.roles

    if mod == "1v1":
        await disp_stats(interaction, my_elo_queue1v1, mod)
    elif mod == "2v2":
        await disp_stats(interaction, my_elo_queue2v2, mod)
    elif mod == "3v3":
        await disp_stats(interaction, my_elo_queue3v3, mod)
    elif mod == "all":
        for role in role_list:
            if role.name == "Admin" or role.name == "Modérateur":
                return (gc3_ssl_1v1)
        await disp_stats_all(interaction)

async def disp_stats_all(interaction: discord.Interaction):
    bronze_silver_gold_1v1_liste = " ".join([f"<@{user_id}>" for user_id in bronze_silver_gold_1v1])
    bronze_silver_gold_2v2_liste = " ".join([f"<@{user_id}>" for user_id in bronze_silver_gold_2v2])
    bronze_silver_gold_3v3_liste = " ".join([f"<@{user_id}>" for user_id in bronze_silver_gold_3v3])

    plat_d1_d2_1v1_liste = " ".join([f"<@{user_id}>" for user_id in plat_d1_d2_1v1])
    plat_d1_d2_2v2_liste = " ".join([f"<@{user_id}>" for user_id in plat_d1_d2_2v2])
    plat_d1_d2_3v3_liste = " ".join([f"<@{user_id}>" for user_id in plat_d1_d2_3v3])

    d3_c1_c2_1v1_liste = " ".join([f"<@{user_id}>" for user_id in d3_c1_c2_1v1])
    d3_c1_c2_2v2_liste = " ".join([f"<@{user_id}>" for user_id in d3_c1_c2_2v2])
    d3_c1_c2_3v3_liste = " ".join([f"<@{user_id}>" for user_id in d3_c1_c2_3v3])

    c3_gc1_gc2_1v1_liste = " ".join([f"<@{user_id}>" for user_id in c3_gc1_gc2_1v1])
    c3_gc1_gc2_2v2_liste = " ".join([f"<@{user_id}>" for user_id in c3_gc1_gc2_2v2])
    c3_gc1_gc2_3v3_liste = " ".join([f"<@{user_id}>" for user_id in c3_gc1_gc2_3v3])

    gc3_ssl_1v1_liste = " ".join([f"<@{user_id}>" for user_id in gc3_ssl_1v1])
    gc3_ssl_2v2_liste = " ".join([f"<@{user_id}>" for user_id in gc3_ssl_2v2])
    gc3_ssl_3v3_liste = " ".join([f"<@{user_id}>" for user_id in gc3_ssl_3v3])

    embed = discord.Embed(title=f"Voici la liste de toutes les queues", color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Queue 1v1 bronze - gold: ", value=bronze_silver_gold_1v1_liste, inline=False)
    embed.add_field(name="Queue 2v2 bronze - gold: ", value=bronze_silver_gold_2v2_liste, inline=False)
    embed.add_field(name="Queue 3v3 bronze - gold: ", value=bronze_silver_gold_3v3_liste, inline=False)

    embed.add_field(name="Queue 1v1 plat - d2: ", value=plat_d1_d2_1v1_liste, inline=False)
    embed.add_field(name="Queue 2v2 plat - d2: ", value=plat_d1_d2_2v2_liste, inline=False)
    embed.add_field(name="Queue 3v3 plat - d2: ", value=plat_d1_d2_3v3_liste, inline=False)

    embed.add_field(name="Queue 1v1 d3 - c2: ", value=d3_c1_c2_1v1_liste, inline=False)
    embed.add_field(name="Queue 2v2 d3 - c2: ", value=d3_c1_c2_2v2_liste, inline=False)
    embed.add_field(name="Queue 3v3 d3 - c2: ", value=d3_c1_c2_3v3_liste, inline=False)

    embed.add_field(name="Queue 1v1 c3 - gc2: ", value=c3_gc1_gc2_1v1_liste, inline=False)
    embed.add_field(name="Queue 2v2 c3 - gc2: ", value=c3_gc1_gc2_2v2_liste, inline=False)
    embed.add_field(name="Queue 3v3 c3 - gc2: ", value=c3_gc1_gc2_3v3_liste, inline=False)

    embed.add_field(name="Queue 1v1 gc3 - ssl: ", value=gc3_ssl_1v1_liste, inline=False)
    embed.add_field(name="Queue 2v2 gc3 - ssl: ", value=gc3_ssl_2v2_liste, inline=False)
    embed.add_field(name="Queue 3v3 gc3 - ssl: ", value=gc3_ssl_3v3_liste, inline=False)

    await interaction.response.send_message(embed=embed)

