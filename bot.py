import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
  print("Hello! How can I help?")

@client.event
async def on_member_join(member):
  print(f"{member} has joined the server!")

@client.event
async def on_member_remove(member):
  print(f"{member} has left the server!")

@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

client.run("YOUR BOT TOKEN")
