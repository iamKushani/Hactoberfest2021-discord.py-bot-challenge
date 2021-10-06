import discord

class Delete(discord.ui.View):

    def __init__(self,user):
        super().__init__()
        self.user=user
        self.value=None
    
    @discord.ui.button(label="❎",style=discord.ButtonStyle.red)
    async def deletethis(self,button : discord.ui.Button,interaction : discord.Interaction):
        self.value=True
        await interaction.message.delete()
        self.stop()


    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.user:
            await interaction.response.send_message("Sorry,you did not run this command", ephemeral=True)
            return False

        return True

class Save(discord.ui.View):
    def __init__(self,user):
        super().__init__()
        self.user=user

    @discord.ui.button(label="Save?",style=discord.ButtonStyle.green)
    async def save(self,button:discord.ui.Button,interaction:discord.Interaction):
        msg=interaction.message
        try:
            await self.user.send(msg.embeds[0].image.url)
        except:
            await interaction.response.send_message("Your dms are not open, so I am unable to send this to you.",ephemeral=True)
        else:
            self.stop()
        