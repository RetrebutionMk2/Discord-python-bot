from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # empty for future features to be added
        pass

def setup(bot):
    bot.add_cog(OnMessage(bot))