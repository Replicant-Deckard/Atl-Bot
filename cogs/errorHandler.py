from discord.ext import commands
from discord import Member


class ErrorHandler(commands.Cog):
    """An example cog to show error handling."""

    def __init__(self, client: commands.Bot):
        self.client = client

    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = "Oh no! Something went wrong while running the command!"

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)


def setup(client: commands.Bot):
    client.add_cog(ErrorHandler(client))
    print("Succesfully loaded errorHandler module")