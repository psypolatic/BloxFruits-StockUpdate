import discord
import asyncio
import json
import requests

def parse_price(price_str):
    return int(price_str.replace("$", "").replace(",", ""))

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
emoji_dict = {}

async def update_stock(message):
    response = requests.get('Yoursite.com')
    data = response.json()

    # Filter out 'Out of Stock' items
    in_stock = {k: parse_price(v) for k, v in data.items() if v.strip() != 'Out of Stock'}

    # Sort items by price from most expensive to least expensive
    sorted_items = sorted(in_stock.items(), key=lambda x: x[1], reverse=True)

    # Create a list of strings, each representing one item and its price
    items_strings = [f"<:{item.replace('-', '')}:{emoji_dict.get(item.replace('-', ''), '')}>{item.split('-')[0]}: ${price:,}" for item, price in sorted_items]

    # Join the strings into one string with line breaks
    result = '\n'.join(items_strings)
    await message.channel.send(result)
    await message.channel.send("<@&1133244097184923688>")

async def start_monitoring(message):
    await message.channel.send(f"Monitoring will start in fruits in {message.channel.name} ")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for emoji in client.emojis:
        emoji_dict[emoji.name] = emoji.id

@client.event
async def on_message(message):
    if message.content.startswith("$hello"):
        await message.channel.send("Hello cutie")
    elif message.content.startswith("$start_monitoring"):
        await start_monitoring(message)
        await asyncio.sleep(60 * 60 * 3.5)  # wait for 3 hours and 30 minutes before the first update
        while True:
            await update_stock(message)
            await asyncio.sleep(60 * 60 * 4)  # wait 4 hours before updating again
    elif message.content.startswith("force_update"):
        await update_stock(message)



#update me
client.run('Your token')
