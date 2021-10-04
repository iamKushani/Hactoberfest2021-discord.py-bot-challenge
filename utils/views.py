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

