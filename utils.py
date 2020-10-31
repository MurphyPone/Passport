# helpers for the embed
import discord 
from conf import EVENT_NAME

def std_embed():
    embed = discord.Embed(
        color=0x6666FF,
        description=f'track your participation at {EVENT_NAME}'
    )
    
    return embed

def std_footer(embed):
    embed.add_field(
        name="Links",
        value="[Report a bug](https://github.com/MurphyPone/Passport)",
        inline=False
    )