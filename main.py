import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.invites = True
intents.guilds = True

load_dotenv()

client = commands.Bot(command_prefix="+", intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="TechSUpport FR", url="https://www.twitch.tv/discord"))
    print(f"""
         ██████╗ ██╗   ██╗ ██████╗██╗  ██╗██████╗  ██████╗ ████████╗
         ██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
         ██║  ██║██║   ██║██║     █████╔╝ ██████╔╝██║   ██║   ██║
         ██║  ██║██║   ██║██║     ██╔═██╗ ██╔══██╗██║   ██║   ██║
         ██████╔╝╚██████╔╝╚██████╗██║  ██╗██████╔╝╚██████╔╝   ██║
         ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝
                        0.rsp | TechSupport FR
                     https://discord.gg/PqnJbkXn7J

           ╔═══════════════════════════════════════════════╗
           ║ ID du bot          : {client.user.id:<25}║
           ║ Nombre de serveurs : {len(client.guilds):<25}║
           ║ Nombre de membres  : {len(set(client.get_all_members())):<25}║
           ╚═══════════════════════════════════════════════╝
""")



async def load():
    for filename in os.listdir('./cogs'):
        if(filename.endswith('.py')):
            await client.load_extension(f'cogs.{filename[:-3]}')



async def main():
    token = os.getenv('DISCORD_TOKEN')

    if token is None:
        print("Erreur : le token Discord n'a pas été trouvé dans le fichier .env")
        return

    await load()
    await client.start(token)



if __name__ == "__main__":
    asyncio.run(main())
