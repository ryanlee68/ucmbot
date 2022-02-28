import logging
from .bot import bot

logger = logging.getLogger(__name__)

@bot.event
async def on_ready():
    logger.info(f"{bot.user} is ready!")

@bot.event
async def on_guild_join(guild: discord.Guild):
    if not guild.me.guild_permissions.administrator:
        message = f"The bot immediately left the '{guild}' server due to a lack of permissions."
        if guild.owner:
            await guild.owner.send(
                "Thank you for inviting me but my stay was short lived "
                "due to a lack of permissions. In order to function properly "
                "I need the admin permission. Please invite me back using this "
                "link which will give me the admin permissions: "
                + discord.utils.oauth_url(
                    bot.user.id,
                    permissions=discord.Permissions(administrator=True),
                    scopes=('bot', 'applications.commands')
                )
            )
            message += " And messaged the owner about the issue."
        await guild.leave()
        logger.info(message)
    else:
        if guild.owner:
            message = 
                "The ucm bot has joined the server, make sure the "
                "server is a community server and has an announcements channel"
            await guild.owner.send(message)
            logger.info('The owner was notified about the bot joining.')

@bot.event
async def on_error(event: str, *args, **kwargs):
    logger.error(f"The following error occured with the {event} event:", exc_info=sys.exc_info())