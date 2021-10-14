import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO
import functools

class ImageManipulation(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    def wantedimage(self,avatar):
        path = './assets/wanted.jpg'
        with Image.open(path) as wimg:
            with Image.open(avatar) as pfp:
                pfp=pfp.resize((111,111))
                wimg.paste(pfp,(33,98))
                buffer=BytesIO()
                wimg.save(buffer,"png")
                buffer.seek(0)
                return buffer   

    @commands.command()
    async def wanted(self,ctx,member:discord.Member=None):
        user = ctx.message.author if member is None else member
        avatar = BytesIO(await user.display_avatar.read())
        partialfunc=functools.partial(self.wantedimage,avatar)
        buffer=await self.client.loop.run_in_executor(None,partialfunc)
        await ctx.send(file=discord.File(fp=buffer,filename="wanted.png"))

def setup(client):
    client.add_cog(ImageManipulation(client))