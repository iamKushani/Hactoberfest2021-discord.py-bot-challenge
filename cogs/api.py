import discord
from discord.ext import commands
import aiohttp
from utils.views import Save

class ApiCommands(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command(aliases=['catpics','catpic','cat'],help="This command will show a random cat picture.")
    async def kitty(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat') 
            catjson = await request.json() 
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()
            embed = discord.Embed(title="Kitty!", color=discord.Color.purple()) 
            embed.set_image(url=catjson['link']) 
            embed.set_footer(text=factjson['fact'])
            await ctx.send(embed=embed,view=Save(ctx.author)) 

    @commands.command(aliases=['dogpics','dogpic','dog'],help="This command will show a random cat picture.")
    async def doggo(self,ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog') 
            dogjson = await request.json() 
            embed = discord.Embed(title="Doggo!", color=discord.Color.purple()) 
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()           
            embed.set_image(url=dogjson['link']) 
            embed.set_footer(text=factjson['fact'])
            await ctx.send(embed=embed,view=Save(ctx.author))

    @commands.command(name="httpcat",help="Returns a http status code cat picture based on the code you send or a random one if you don't provide a code.")
    async def httpcat(self,ctx,code:int):
        url="https://http.cat/"+str(code)
        embed=discord.Embed(title="HTTP cat",description="Your requested http cat.Remember, only a part of valid status codes have http cats, others don't have.")
        embed.set_image(url=url)
        await ctx.send(embed=embed,view=Save(ctx.author))

def setup(client):
    client.add_cog(ApiCommands(client))