import discord

class LinkButton(discord.ui.Button):
    def __init__(self,label:str,url) -> None:
        super().__init__(label=label,style=discord.ButtonStyle.link,url=url)
    
