import discord
import datetime

from queues import _queue_1v1
from queues import _queue_2v2
from queues import _queue_3v3
from leave_queue import leave_fnc
from status_queue import disp_stats

queue_list_1v1_low = []
queue_list_1v1_mid = []
queue_list_1v1_high = []

queue_list_2v2_low = []
queue_list_2v2_mid = []
queue_list_2v2_high = []

queue_list_3v3_low = []
queue_list_3v3_mid = []
queue_list_3v3_high = []

async def queue(interaction: discord.Interaction, client, clear_queue, mod):
    member = interaction.user
    if mod == "1v1":
        await queue_1v1(interaction, client, clear_queue)
    elif mod == "2v2":
        await queue_2v2(interaction, client, clear_queue)
    elif mod == "3v3":
        await queue_3v3(interaction, client, clear_queue)

async def queue_1v1(interaction: discord.Interaction, client, clear_queue):
    member = interaction.user
    role_list = member.roles

    for role in role_list:
        if role.name == "high_elo":
            await _queue_1v1(interaction, client, clear_queue, queue_list_1v1_high)
        elif role.name == "mid_elo":
            await _queue_1v1(interaction, client, clear_queue, queue_list_1v1_mid)
        elif role.name == "low_elo":
            await _queue_1v1(interaction, client, clear_queue, queue_list_1v1_low)


async def queue_2v2(interaction: discord.Interaction, client, clear_queue):
    member = interaction.user
    role_list = member.roles

    for role in role_list:
        if role.name == "high_elo":
            await _queue_2v2(interaction, client, clear_queue, queue_list_2v2_high)
        elif role.name == "mid_elo":
            await _queue_2v2(interaction, client, clear_queue, queue_list_2v2_mid)
        elif role.name == "low_elo":
            await _queue_2v2(interaction, client, clear_queue, queue_list_2v2_low)


async def queue_3v3(interaction: discord.Interaction, client, clear_queue):
    member = interaction.user
    role_list = member.roles

    for role in role_list:
        if role.name == "high_elo":
            await _queue_3v3(interaction, client, clear_queue, queue_list_3v3_high)
        elif role.name == "mid_elo":
            await _queue_3v3(interaction, client, clear_queue, queue_list_3v3_mid)
        elif role.name == "low_elo":
            await _queue_3v3(interaction, client, clear_queue, queue_list_3v3_low)


async def leave_queue(interaction: discord.Interaction, mod):
    member = interaction.user
    role_list = member.roles

    if mod == "1v1":
        for role in role_list:
            if role.name == "high_elo":
                await leave_fnc(interaction, queue_list_1v1_high, mod)
            elif role.name == "mid_elo":
                await leave_fnc(interaction, queue_list_1v1_mid, mod)
            elif role.name == "low_elo":
                await leave_fnc(interaction, queue_list_1v1_low, mod)
    elif mod == "2v2":
        for role in role_list:
            if role.name == "high_elo":
                await leave_fnc(interaction, queue_list_2v2_high, mod)
            elif role.name == "mid_elo":
                await leave_fnc(interaction, queue_list_2v2_mid, mod)
            elif role.name == "low_elo":
                await leave_fnc(interaction, queue_list_2v2_low, mod)
    elif mod == "3v3":
        for role in role_list:
            if role.name == "high_elo":
                await leave_fnc(interaction, queue_list_3v3_high, mod)
            elif role.name == "mid_elo":
                await leave_fnc(interaction, queue_list_3v3_mid, mod)
            elif role.name == "low_elo":
                await leave_fnc(interaction, queue_list_3v3_low, mod)


async def display_status(interaction: discord.Interaction, mod):
    member = interaction.user
    role_list = member.roles

    if mod == "1v1":
        for role in role_list:
            if role.name == "high_elo":
                await disp_stats(interaction, queue_list_1v1_high, mod)
            elif role.name == "mid_elo":
                await disp_stats(interaction, queue_list_1v1_mid, mod)
            elif role.name == "low_elo":
                await disp_stats(interaction, queue_list_1v1_low, mod)
    elif mod == "2v2":
        for role in role_list:
            if role.name == "high_elo":
                await disp_stats(interaction, queue_list_2v2_high, mod)
            elif role.name == "mid_elo":
                await disp_stats(interaction, queue_list_2v2_mid, mod)
            elif role.name == "low_elo":
                await disp_stats(interaction, queue_list_2v2_low, mod)
    elif mod == "3v3":
        for role in role_list:
            if role.name == "high_elo":
                await disp_stats(interaction, queue_list_3v3_high, mod)
            elif role.name == "mid_elo":
                await disp_stats(interaction, queue_list_3v3_mid, mod)
            elif role.name == "low_elo":
                await disp_stats(interaction, queue_list_3v3_low, mod)

