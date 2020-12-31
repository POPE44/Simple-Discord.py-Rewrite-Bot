mport discord, random, asyncio
from discord.ext import commands
from random import randint
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


client = commands.Bot(command_prefix="!")

#startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('P!help    | Custom Status '))
    print("------------------------------------\n           Bot is Running:  \n------------------------------------")


#test dms
@client.command()
async def test(ctx):
    if ctx.channel.id == ("Channel Id Here"):
        await ctx.author.send("Testing your Dms, 123")
        await ctx.send("Test Dm Sent! ")
    else:
        await ctx.send("Not The right channel sorry")

#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Bot Response Time: {round(client.latency * 1000)}ms')

#randomint
@client.command()
async def rng(ctx):
    stock_opt = randint(0, 4)
    if stock_opt <= int(2):
        await ctx.send("Number is low!!")    
    else:
        stock_opt > int(2)
        await ctx.send("Number is High!!")  


#Dm a line from a .txt
@client.command()
async def nord(ctx):
    if ctx.channel.id == ("channel id"):
        with open("C:\\Users\\range\\Desktop\\.txt\\") as f:     #Have the path there (obv)
            lines = f.readlines()
            await ctx.author.send(random.choice(lines))
            await ctx.send("Check Dms!")
    else:
        await ctx.send("Not The right channel sorry")

#Kick
@client.command()

@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
        try: 
            await member.kick()
            await ctx.message.add_reaction(" ")
            await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
            await log_channel.send(f"{ctx.author.name} has kicked {member.display_name}")
                
        except: discord.ext.commands.CommandInvokeError = await ctx.send("I dont have the right permissions for that :( ")

#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

#Ban
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#Unban
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#help 
client.remove_command("help")
@client.command()
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Permanent Invite link To My Server! --> https://discord.gg/Server ", colour = ctx.author.colour)
    em.add_field(name = "Set 1", value = "1\n2\n3\n4\n5\n6\n7\n8\n")
    em.add_field(name = "Set 2", value = "1, 2")
    em.add_field(name = "Moderation", value = "ban\n kick\n Warn\n")

    await ctx.send(embed = em)

client.run("Token")

#Made By Grizz#7690
