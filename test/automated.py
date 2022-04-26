from discord.ext import commands, tasks
from discord.commands import slash_command

class AutomatedCogs(commands.Cog):
    
    def __init__(self):
        self.announce_events.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is running!")

    @slash_command()
    async def hello(self, ctx, name: str = None):
        name = name or ctx.author.name
        await ctx.respond(f"Hello {name}!")

    # async def run_in(self, seconds: int):
    #     # announce event
    #     pass

    @tasks.loop(seconds=5.0)
    async def announce_events(self):
        print("1")

    @slash_command()
    async def yolo(self, ctx, name: str = None):
        print(name)
        name = name or ctx.author.name
        await ctx.respond(f"yolo {name}!")