import random
import discord
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def help_me(ctx):
    help_message = (
        "📌 **Perintah Bot:**\n"
        "1. `!help_me` - Menampilkan pesan bantuan ini\n"
        "2. `!suit <pilihan>` - Main suit (batu, kertas, gunting)\n"
        "3. `!tebak <angka>` - Main tebak angka (1-100)\n"
        "4"
    )
    
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

#tebak angka
number = random.randint(1, 100)
@bot.command()
async def tebak(ctx, angka: int):
    global number
    if angka < number:
        await ctx.send("📉 Terlalu rendah! Coba lagi.")
    elif angka > number:
        await ctx.send("📈 Terlalu tinggi! Coba lagi.")
    else:
        await ctx.send("🎉 Selamat! Kamu menebak angka yang benar.")
        number = random.randint(1, 100)  # Reset angka untuk permainan berikutnya

bot.run("TOken")
