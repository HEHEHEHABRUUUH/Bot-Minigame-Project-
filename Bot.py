import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

kata_list = ["python", "discord", "komputer", "internet"]
jawaban = None
terbuka = []  # huruf yang sudah terbuka

@bot.event
async def on_ready():
    print(f"Bot aktif sebagai {bot.user}")

@bot.command()
async def tebak(ctx):
    global jawaban, terbuka
    jawaban = random.choice(kata_list)
    terbuka = []

    petunjuk = " ".join(["_" for _ in jawaban])
    await ctx.send(f"Tebak kata:\n{petunjuk}")

@bot.command()
async def hint(ctx):
    global jawaban, terbuka

    if jawaban is None:
        await ctx.send("Mulai dulu dengan !tebak")
        return

    # cari huruf yang belum terbuka
    sisa = [i for i in range(len(jawaban)) if i not in terbuka]

    if not sisa:
        await ctx.send("Semua huruf sudah terbuka!")
        return

    index = random.choice(sisa)
    terbuka.append(index)

    # tampilkan petunjuk baru
    hasil = ""
    for i, huruf in enumerate(jawaban):
        if i in terbuka:
            hasil += huruf + " "
        else:
            hasil += "_ "

    await ctx.send(f"Hint:\n{hasil}")

@bot.command()
async def jawab(ctx, *, guess):
    global jawaban, terbuka

    if jawaban is None:
        await ctx.send("Mulai dulu dengan !tebak")
        return

    if guess.lower() == jawaban:
        await ctx.send("Benar!")
        jawaban = None
        terbuka = []
    else:
        await ctx.send("Salah!")

bot.run("Token Cuy")
