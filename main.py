import discord
from discord.ext import commands
from discord.embeds import Embed


client = commands.Bot(command_prefix="$" , intents = discord.Intents.all())
client.remove_command("help")

token = "you'r bot token"

@client.event
async def on_ready():
    print(f"We have logged in as...\n{client.user}")

@client.command()
async def unban(ctx):
    counter = 0
    banned = ctx.guild.bans()
    async for users in banned:
        user = users.user
        try:
            await ctx.guild.unban(user)
            print(Fore.GRENN + f"Unbanned user: {user}")
        except:
            print(Fore.RED + f"Can't Unbanned user: {user}")
        counter += 1
    await ctx.channel.send(f"Unbanned {counter} members")

@client.event
async def on_member_unban(guild, user):
    print("Unbanned a user!")

client.run(token)
