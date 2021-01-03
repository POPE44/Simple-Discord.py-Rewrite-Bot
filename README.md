# Simple Discord Bot Written with Discord.py Rewrite!
A discord bot written in Discord.py Rewrite that has multiple features including Admin Commnands --> & most importantly DM ommands and channel limiting.

## Installation
Install the nessecary Components

```bash
pip3 install discord.py rewrite
pip3 install asyncio
```

## Usage

```python
python3 "discordbot.py"
```

## Key Blocks
Dm A member
```python
@client.command()
async def test(ctx):
    if ctx.channel.id == ("Channel Id Here"):
        await ctx.author.send("Testing your Dms, 123")
        await ctx.send("Test Dm Sent! ")
    else:
        await ctx.send("Not The right channel sorry")
```
Ban a member    
```python
@client.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason =None):
    await member.ban(reason=reason)
    await ctx.send("User " + member.display_name + " has been Banned")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact
Contact me on 
Discord: Grizz#7690

Join The Bot Server For Questions and More!! ---> https://discord.gg/Q4zX3JbGxG

Email: Grizzly43256@gmail.com

Music Bot Coming Soon!

