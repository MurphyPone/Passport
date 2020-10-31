import discord 
from discord.ext import commands, tasks
import pyrebase
from datetime import datetime
from utils import *
from conf import *

# initial setup   
client = commands.Bot(command_prefix='π ')
client.remove_command('help')
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()

# Debug commands
@client.event 
async def on_ready():
    await client.change_presence(activity=discord.Game("Helping Hackers"))
    print('[LOG] passport coming online')


@client.event 
async def on_member_join(member):
    print(f'{member} has joined a server')

# Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ping = {round(client.latency * 1000)} ms')


@client.command(name="info", aliases=['i'])
async def info(ctx, user=None):
    embed = std_embed()
    if user is None:  # get info about the user who typed info
        # TODO pyrebase error checking here
        target = dict(db.child("users").child(str(ctx.message.author.id)).get().val())
        embed.add_field(name=f"{target['username']}", value=f"checked in at {target['checkin-time']}", inline=True)
        print(f"[LOG] user: {target['username']}")
        print(f"[LOG] checkedinin at: {target['checkin-time']}")
        await ctx.send(embed=embed)

    
    else:               # get info about a supplied users
        print(user)
        await ctx.send(f"can only get information the current user...")
    



@client.command(name="checkin")
async def checkin(ctx):
    # TODO this doesn't work if there are no entries already
    if str(ctx.message.author.id) in list(db.child("users").shallow().get().val()):
        user = dict(db.child("users").child(str(ctx.message.author.id)).get().val())['username']
        print(user)
        print(f"[LOG] already checked in")
        await ctx.send(f"**{user}** has already checked in")

    else:

        payload = { 
            "username": f"@{ctx.message.author.name}",  
            "id": ctx.message.author.id,
            "checkin-time": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
            "events": []
            }
        db.child("users").child(payload['id']).set(payload)
        await ctx.send(f"checked in **{payload['username']}**")

@client.command(name="help", aliases=['h'])
async def help(ctx, *args):
    embed = std_embed()
    # if len(args) == 0:
    embed.add_field(name=":wave: `help`", value="help commands will go here", inline=False)
    embed.add_field(name=":white_check_mark: `checkin`", value="checkin to the event", inline=False)
    embed.add_field(name=":book: `info`", value="get info about a user", inline=False)
    # else: 

    std_footer(embed) # add the footer to the help message
    await ctx.send(embed=embed)

client.run(DISCORD_KEY)