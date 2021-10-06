import discord
from discord.errors import HTTPException
from discord.ext import commands
import aiohttp
import urllib
from datetime import timedelta
import time

class General(commands.Cog):
    def __init__(self,client):
        self.client=client
        self.stopwatches={}

    @commands.group(name="qr",aliases=["qrcode"],invoke_without_command=True,help="QR code commands")
    async def qr(self,ctx):
        await ctx.send("You have 2 options, either choose read or create option, for eg: >qr read <qrcode link> will read the qr code and return its contents")
    
    @qr.command(help="To read a qr code, send a link or attach an image.")
    async def read(self,ctx,qr_link=None):
        msg=await ctx.send("Processing...")
        if qr_link is None:
            qr_link=ctx.message.attachments[0].url
        qr_l=urllib.parse.quote(qr_link)
        link="https://api.qrserver.com/v1/read-qr-code/?fileurl="+qr_l
        async with aiohttp.request("GET",link) as r:
            e=await r.read()
        data=e.decode('utf-8')
        a=data.replace('null','None')
        content=eval(a)
        qrcontent=content[0]['symbol'][0]['data']
        embed=discord.Embed(title="Your requested QR code decryption",description="I use an api to read the qr code,[their website](https://goqr.me/)")
        embed.add_field(name="Content",value=qrcontent)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        try:
            await msg.edit(embed=embed)
        except HTTPException:
            await msg.edit(content="You haven't provided a valid qr code.")


    @qr.command(help="To create a qr code.")
    async def create(self,ctx,*,qr_content:str=None):
        if qr_content is None:
            await ctx.send("You didn't give any content to embed into a qr code.(it should be either a link or a text or a combination of both)")
            return
        qr_c=urllib.parse.quote(qr_content)
        link=f"http://api.qrserver.com/v1/create-qr-code/?data={qr_c}&size=256x256"
        embed=discord.Embed(title="Your requested QR code",description="I use an api to generate the qr code,[their website](https://goqr.me/)")
        embed.set_image(url=link)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["calculate"],help="For math operations, can do +,-,*,/,//,supports paranthesis and sending numbers in scientific notation.")
    async def calc(self,ctx,expression):
        for i in expression:
            if i not in ["+","-","*","/","//","%","(",")",".","e","1","2","3","4","5","6","7","8","9","0","{","}","[","]"]:
                await ctx.send("That is not a valid mathematical expression.")
                break
        else:
            try:
                final_answer=eval(expression)
            except Exception as e:
                await ctx.send(f"An error has been raised : `{e}`")
            await ctx.send(f"Final answer `{final_answer}`")

    @commands.command(aliases=["sw"],help="A stopwatch command, run it to start the stopwatch and run it again to stop it.")
    async def stopwatch(self, ctx):
        author = ctx.author
        if str(author.id) not in self.stopwatches:
            self.stopwatches[str(author.id)] = int(time.perf_counter())
            await ctx.send(author.mention + (" Stopwatch started!"))
        else:
            tmp = abs(self.stopwatches[str(author.id)] - int(time.perf_counter()))
            tmp = str(timedelta(seconds=tmp))
            await ctx.send(author.mention + (" Stopwatch stopped! Time: **{seconds}**").format(seconds=tmp))
            self.stopwatches.pop(str(author.id), None)

    @commands.command(brief="Emojify your text",help='For when plain text just is not enough')
    async def emojify(self,ctx, *, text: str):

        author = ctx.message.author
        formatted=str()
        for c in text:
            if c.isalpha():
                formatted+=c
        if text == '':
            await ctx.send('Remember to say what you want to convert!')
        else:
            emojified = ''.join(
                '     ' if i == ' ' else ':regional_indicator_{}: '.format(i)
                for i in formatted
            )

            if len(emojified) >= 1998:
                await ctx.send('Your message in emojis exceeds 2000 characters!')
            if len(emojified) <= 25:
                await ctx.send('Your message could not be converted!')
            else:
                await ctx.send(''+emojified+'')

def setup(client):
    client.add_cog(General(client))