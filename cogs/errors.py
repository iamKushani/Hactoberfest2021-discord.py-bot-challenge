import discord
import sys
import traceback
from discord.ext import commands
import datetime
from discord.ext.commands.cooldowns import C

from discord.ext.commands.core import Command

class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog and cog._get_overridden_method(cog.cog_command_error) is not None:
            return

        ignored = (commands.CommandNotFound,commands.NotOwner)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't even have the required perms to run this command.Permissions missing : {error.missing_perms}")

        elif isinstance(error,commands.CommandOnCooldown):
            message=f"This command is on cooldown. Please try again after {datetime.timedelta(seconds=round(error.retry_after))} seconds."
            await ctx.send(message)  
                  
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(client):
    client.add_cog(CommandErrorHandler(client))