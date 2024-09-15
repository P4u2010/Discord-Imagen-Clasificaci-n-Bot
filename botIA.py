import discord
from discord.ext import commands
from model import get_class

intents=discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f"Se inicio el bot {bot.user}")
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url= attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./keras_model.h5", label_path="./labels.txt", image_path=f"./{file_name}"))
    else:
        await ctx.send("Olvido subir una imagen 😞")

bot.run("MTI3OTg5MzE3NjI1MzE1MzQwMg.G9X55r.p0BQEFfUCDYopRjZPBTHXF21NJi_JvHZ24yDe0")    