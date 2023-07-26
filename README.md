# BloxFruits Updater Bot

This bot is a utility tool for the game BloxFruits on Roblox. It enables automatic monitoring and updating of fruit prices in the game by communicating with a server. The bot works by injecting a Lua script into an active BloxFruits game with the fruit dealer already open.

## Project Structure

This project contains three main components:

- `Fruitupdater.lua`: This is the script that interacts with the BloxFruits game. It fetches the prices of the fruits from the game and sends them to the server.

- `Bot.py`: This is a Discord bot script that retrieves the fruit prices from the server and updates them in a Discord channel. It is also capable of monitoring the fruit prices and updating them every 4 hours.

- `Server.py`: This is the server script that facilitates the communication between the Lua script and the Discord bot. It receives the fruit prices from the Lua script and serves them to the Discord bot.

## Setup

To set up the bot, follow these steps:

1. Update the `Fruitupdater.lua` script with your Roblox username and the URL of your server.

2. In `Bot.py`, update the URL from which the bot retrieves the data and the token of your Discord bot. 

3. In `Server.py`, set up the server route that will receive the POST request from the Lua script and serve the data to the Discord bot.

## Running the Bot

1. Inject the `Fruitupdater.lua` script into an active BloxFruits game with the fruit dealer open.

2. Run the `Server.py` script to start the server.

3. Run the `Bot.py` script to start the Discord bot.

## Commands

The bot supports the following commands:

- `$hello`: The bot will respond with "Hello cutie".

- `$start_monitoring`: The bot will start monitoring the fruit prices and update them in the Discord channel every 4 hours.

- `force_update`: The bot will immediately update the fruit prices in the Discord channel.

Please note that the bot will wait for 3 hours and 30 minutes before the first update after starting to monitor.

## Disclaimer

This bot is for educational purposes only. Use it responsibly and respect the terms of service of the platforms it interacts with. Always ensure that you are permitted to use scripts and bots with the services you are interacting with. The developer is not responsible for any misuse or any damages caused.
