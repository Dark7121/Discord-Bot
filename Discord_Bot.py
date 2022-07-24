import discord
import os
import requests
import json
import random
import io
import aiohttp
import asyncio
from replit import db


client = discord.Client()

greetings = ("+hi", "+hey", "+hello", "+HI", "+HEY", "+HELLO", "+Hi", "+Hey", "+Hello")
 
if "responding" not in db.keys():
  db["responding"] = True


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
 
  msg = message.content

  if msg.startswith(greetings):
    
    await message.channel.send("Hey {0.author.mention}, I'm an anime character but in discord I'm a bot made by <@447312379131199488>. My motto is 'If I don't have to do it, I won't. If I have to do it, I'll make it quick.'".format(message))

  if msg.startswith("who r u"):
    
    await message.channel.send("{0.author.mention}, I'm a Hōtarō Oreki, I'm the protagonist of Classic Literature Club series and Hyouka. I'm a student of Kamiyama High School belonging to class 1-B at first, and later to class 2-A. Also I'm a member of the school's Classic Lit Club.".format(message))

  if msg.startswith("fb"):
    await message.channel.send("Go and Like Our FaceBook Page https://www.facebook.com/adventure2anime/?ref=page_internal",
    file=discord.File('ppm.jpg'))

  if msg.startswith("insta"):
    await message.channel.send("Go and Like Our Instagram Profile https://www.instagram.com/adventure2anime/?fbclid=IwAR0u-x7zqjLtYeu8_b9uNa4Lpa7_g-VT-E2tTCPzfHHshncYhLUGlHxAknY",
    file=discord.File('ppm.jpg'))

  if msg.startswith("+website"):
    await message.channel.send("https://phanute.com/", file=discord.File('pp.jpg'))


my_secret = os.getenv("ODgwOTM4Njc0ODI3Njg5OTk0.YSlkEw.PgYADgY-cU3f0TWC02HAVAsWcbA")
