import random
import discord
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
#Suit
@bot.command()
async def suit(ctx, pilihan):
    pilihan = pilihan.lower()
    bot_choice = random.choice(["batu", "kertas", "gunting"])

    if pilihan not in ["batu", "kertas", "gunting"]:
        await ctx.send("❌ Pilih: batu / kertas / gunting")
        return

    if pilihan == bot_choice:
        hasil = "😐 Seri!"
    elif (
        (pilihan == "batu" and bot_choice == "gunting") or
        (pilihan == "gunting" and bot_choice == "kertas") or
        (pilihan == "kertas" and bot_choice == "batu")
    ):
        hasil = "🎉 Kamu menang!"
    else:
        hasil = "💀 Kamu kalah!"

    await ctx.send(f"Kamu: {pilihan}\nBot: {bot_choice}\n{hasil}")

bot.run("TOken")
