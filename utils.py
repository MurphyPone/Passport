# helpers for the embed
import discord 
from conf import EVENT_NAME, LIVESITE_URL

def std_embed():
    embed = discord.Embed(
        color=0x6666FF,
        description=f'track your participation at {EVENT_NAME}'
    )
    
    return embed

def std_footer(embed):
    embed.add_field(
        name="Links",
        value=f"More information can be found at {LIVESITE_URL}",
        inline=False
    )