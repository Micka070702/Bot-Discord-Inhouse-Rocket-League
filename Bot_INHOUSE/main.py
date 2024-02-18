#####################################################################################################################################################
##|Imports|##########################################################################################################################################
#####################################################################################################################################################

import os
import discord
import time
import platform
import datetime
import asyncio

from discord.ext import commands
from colorama import Back, Fore, Style
from dotenv import load_dotenv


from queue_gest import queue, leave_queue, display_status


#####################################################################################################################################################
##|Loading env & Bot|################################################################################################################################
#####################################################################################################################################################


load_dotenv(dotenv_path="config")
activity = discord.Game(name="RL Inhouse BOT by @KcFiffty")
client = commands.Bot(command_prefix=".", intents=discord.Intents.all(), activity=activity, status=discord.Status.do_not_disturb)


#####################################################################################################################################################
##|Starting Bot|#####################################################################################################################################
#####################################################################################################################################################


@client.event
async def on_ready():
    prfx = (Back.LIGHTBLACK_EX + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prfx + " Logged in as : " + Fore.YELLOW + client.user.name)
    print(prfx + " Bot Id : " + Fore.YELLOW + str(client.user.id))
    print(prfx + " Discord Version : " + Fore.YELLOW + discord.__version__)
    print(prfx + " Python Version : " + Fore.YELLOW + str(platform.python_version()))
    synced = await client.tree.sync()
    print(prfx + " Slash CMDs Synced : " + Fore.YELLOW + str(len(synced)) + " Commands")


#####################################################################################################################################################
##|Stop command|#####################################################################################################################################
#####################################################################################################################################################


@client.tree.command(name="stop", description="Shutting down the bot")
async def shutdown(interaction: discord.Interaction):
    await interaction.response.send_message(content="Shutting down the bot")
    await client.close()


#####################################################################################################################################################
##|Class Button|#####################################################################################################################################
#####################################################################################################################################################


class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="1v1", style=discord.ButtonStyle.primary, custom_id="1v1")
    async def join_1v1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await queue(interaction, client, clear_queue, "1v1")


    @discord.ui.button(label="2v2", style=discord.ButtonStyle.primary, custom_id="2v2")
    async def join_2v2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await queue(interaction, client, clear_queue, "2v2")


    @discord.ui.button(label="3v3", style=discord.ButtonStyle.primary, custom_id="3v3")
    async def join_3v3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await queue(interaction, client, clear_queue, "3v3")


#####################################################################################################################################################
##|Queue commands|####################################################################################################################################
#####################################################################################################################################################


@client.tree.command(name="q", description="S'enregistrer dans la queue")
async def queue_command(interaction: discord.Interaction):
    view = MyView()
    await interaction.response.send_message("Choisissez une option :", view=view, ephemeral=True)


@client.tree.command(name="qleave", description="quitter la queue (1v1 / 2v2 / 3v3)")
async def leave_command(interaction: discord.Interaction, mod: str):
    if mod != "1v1" and mod != "2v2" and mod != "3v3":
        await interaction.response.send_message("Argument invalide (1v1 ou 2v2 ou 3v3)", ephemeral=True)
    else:
        await leave_queue(interaction, mod)


@client.tree.command(name="qstatus", description="Affiche les membres dans la file d'attente (1v1 / 2v2 / 3v3)")
async def status_command(interaction: discord.Interaction, mod: str):
    if mod != "1v1" and mod != "2v2" and mod != "3v3":
        await interaction.response.send_message("Argument invalide (1v1 ou 2v2 ou 3v3)", ephemeral=True)
    else:
        await display_status(interaction, mod)


async def clear_queue(myliste = []):
    myliste.clear()



client.run(os.getenv("TOKEN"))
