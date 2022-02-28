from discord.ext import commands
from discord.commands import Option
import discord
import logging

class CommandsCog(commands.Cog):
    set_commands = discord.SlashCommandGroup(
        'set',
        'Commands used to configure various aspects of the bot.'
    )

    get_commands = discord.SlashCommandGroup(
        'get',
        "Commands used to get various information about the bot."
    )

    start_commands = discord.SlashCommandGroup(
        'start',
        "Commands used to start some automated action of the bot."
    )

    stop_commands = discord.SlashCommandGroup(
        'stop',
        "Commands used to stop some automated action of the bot."
    )

    create_commands = discord.SlashCommandGroup(
        'create',
        "Commands used to create something."
    )



    @set_commands.command(
        name='category',
        description="Use this command to set the category in which new channels will be created in.",
        options=[
            Option(
                discord.CategoryChannel,
                name='channel',
                description="The category to create new channels in."
            )
        ]
    )

    @commands.Cog.listener()
    async def on_application_command_error(
        self,
        ctx: discord.ApplicationContext,
        error: discord.ApplicationCommandInvokeError
    ):
        if isinstance(error.original, commands.MissingPermissions):
            logger.info(
                f"{ctx.author} tried to use the /{ctx.command.qualified_name} "
                "even though they don't have permission to do so."
            )
            await ctx.respond("You do not have permission to use this command.")
        elif isinstance(error.original, commands.NoPrivateMessage):
            logger.info(
                f"{ctx.author} tried to use the /{ctx.command.qualified_name} in a DM."
            )
            await ctx.respond("This command is not available in DM messages.")
        elif isinstance(error.original, commands.BadArgument):
            # NOTE: We are assuming that if this happens the individual command will have
            # logic to handle this situation.
            pass
        else:
            # NOTE: In this case you may want to add ping_dev function like with the bdaybot
            logger.error("The following error occured with the bot:", exc_info=error)
            await ctx.respond("Uh oh! Something went wrong on our end. Please try again later!")