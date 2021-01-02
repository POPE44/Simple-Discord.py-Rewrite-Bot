import discord, random, asyncio
from discord.ext import commands
from random import randint
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from keep_alive import keep_alive


client = commands.Bot(command_prefix="m.")

#startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('m.help   | Moderation Bot For Your Server Invite it here --> http://bit.ly/383IjtK '))
    print("------------------------------------\n           Bot is Running:  \n------------------------------------")

#New Member Joining
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "Member")
    await member.add_roles(role)

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
        await ctx.send(stock_opt)   
    else:
        stock_opt > int(2)
        await ctx.send("Number is High!!")  
        await ctx.send(stock_opt)

#Dm a line from a .txt
@client.command()
async def txt(ctx):
    if ctx.channel.id == ("channel id"):
        with open("C:\\Users\\range\\Desktop\\.txt\\") as f:     #Have the path there (obv)
            lines = f.readlines()
            await ctx.author.send(random.choice(lines))
            await ctx.send("Check Dms!")
    else:
        await ctx.send("Not The right channel sorry")

#Kick
@client.command(name="kick", pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send("User " + member.display_name + " has been kicked")



#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the Perms :angry:")
    #if isinstance(error, discord.ext.commands.CommandInvokeError):
        #await ctx.send("I dont have all the Perms to do that :angry:")

#Ban
@client.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason =None):
    await member.ban(reason=reason)
    await ctx.send("User " + member.display_name + " has been Banned")

#Unban
@client.command()
async def unban(ctx, user: discord.User):
    guild = ctx.guild
    mbed = discord.Embed(
        title = "Success!",
        description = f"{user} has been successfully unbanned"
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=mbed)
        await guild.unban(user=user)

#delete a channel
@client.command()
async def deletechannel(ctx, channel: discord.TextChannel):
    await channel.delete()
    mbed = discord.Embed(
        title = "Success",
        description = f"Channel: {channel} has been deleted",
    )
    if ctx.author.guild_permissions.manage_channels: 
        await ctx.send(embed=mbed)

#create channel
@client.command()
async def addchannel(ctx, channelName):
    guild = ctx.guild
    mbed = discord.Embed(
        title = "Channel Created!",
        description = "{} has been succesfully created".format(channelName)
    )
    if ctx.author.guild_permissions.manage_channels:
        await guild.create_text_channel(name="{}".format(channelName))
        await ctx.send(embed=mbed)


#snipe
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@client.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Said By {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        embed.set_author(name= f"<@{snipe_message_author}>")
        await message.channel.send(embed=embed)
        return        




#clear
@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

#exapmle
@client.command()
async def example(ctx):
    mbed = discord.Embed(title = "Example command", description = "```m.deletechannel 794732280680546344```")
    mbed.add_field(name = "Explanation", value = "here we see the prefix is m. and the channel ID is a number so we've deleted a channel. Right click a channel for its ID")
    await ctx.send(embed = mbed)

#invite
@client.command()
async def invite(ctx):
    mbed = discord.Embed(title = "Invite Link For Bot!! Spread It Around!!", description = "```http://bit.ly/383IjtK```")
    await ctx.send(embed = mbed)


#servercount
@client.command(pass_context = True)
async def servercount(ctx):
  await ctx.send(f"I'm in {len(client.guilds)} servers!") 

#help 
client.remove_command("help")
@client.command()
async def help(ctx):
    em = discord.Embed(title = "Help", description = "", colour = ctx.author.colour)
    em.add_field(name = "Vanity", value = "ping\nexample\nclear\nrandomint (prefix.test)\ntestdm (prefix.test)\nsnipe\ninvite\nbotservers")
    em.add_field(name = "Channels", value = "deletechannel\ncreatechannel")
    em.add_field(name = "Moderation", value = "ban\nkick\nWarn\nunban\n")
    em.add_field(name = "Contact", value = "\n```Join The Support Server! --> https://discord.gg/TAKqzHeTtn ```")
    await ctx.send(embed = em)

keep_alive()
client.run("token")

#Made By Grizz#7690 
#https://discord.gg/TAKqzHeTtn
