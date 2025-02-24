import discord, random, datetime, encouraging_messages
from discord.ext import commands
from holiday_messages import holiday_messages_dict
import time

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='/', intents=intents)

last_command_time = 0
# 3 seconds cooldown
cooldown_time = 3

@bot.event
async def on_ready():
  print(f'Logged on as {bot.user}!')
  await bot.sync_commands()

def datetime_message():
  current_date = datetime.date.today()
  return holiday_messages_dict.get((current_date.month, current_date.day))

def random_message():
  return random.choice(encouraging_messages.encouraging_messages_list)
  
def get_encouraging_message():
  encouraging_message = random_message()
  holiday_message = datetime_message()

  if holiday_message:
    return f'{encouraging_message}\n\n{holiday_message}'
  return encouraging_message

@bot.slash_command(name="encat", description="Get an encouraging message from a cat")
async def encat_slash(ctx):
  global last_command_time

  current_time = time.time()
  if current_time - last_command_time < cooldown_time:
    await ctx.respond("Please wait a moment before using this cat-mand again.", ephemeral=True)
    return
  
  last_command_time = current_time
  message = get_encouraging_message()
  await ctx.respond(message)

@bot.event
async def on_message(message):
  global last_command_time

  if message.author == bot.user:
    return

  if message.content.startswith('$encat'):
    current_time = time.time()
    if current_time - last_command_time < cooldown_time:
      await message.channel.send("Please wait a moment before using this cat-mand again.")
      return

    last_command_time = current_time
    encouraging_message = get_encouraging_message()
    await message.channel.send(encouraging_message)

  await bot.process_commands(message)

bot.run('token')