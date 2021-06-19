# TacoShack-Farmer
[[My Website]](https://mitsuzi.xyz/)

Selfbot Farmer for the popular discord gaming bot, TacoShack. It provides many modules, which includes, auto work, auto gift, auto coupon claim, auto upgrade buys and many more.

I focused mainly on being stealthy, adding a lot of random variables and timings which would make it slightly harder to detect. Everything the bot sends can be quite random as well, as I made separate threads for each module, which would make it slightly harder to find a pattern. Other than that, the farmer would also sends a random command from the list every now and then along side resting for awhile. Every rest in the farmer is also random, plus the cooldown. Other than that, the bot also uses most commands from lists, this includes commands which has alternate commands, for an example, !shack is the same as !b.

# Features

### Multiple Bots

You are able to run multiple bots in the same script, but please make sure each bot has one text channel dedicated to it. As tacoshack does not list who requested most of it's command, my farmer can't differentiate who the bot replied to. Therefore, please only use ONE text channel for ONE bot. 


### Secondary Channels

So I coded this mainly due to wanting to level up on the official taco shack server. They have a system where if you use commands and text in their official discord server, you get EXP which you can use to level up, therefore this feature just sends messages into the official server which my farmer does not care about the reply or random commands into the secondary channel list.


### Auto Upgrade

This is the most useful feature in the farmer. It uses all the commands which displays all the different things you can buy and records the price than auto buys the cheapest options from the entire list. It also allows you to use different command for it, for example, the employees list, requires you to do !hire, while everything else requires !buy. You can set individual commands.


### Auto Boost

This allows the farmer to check what boost you have active, then buys the boosts which are inactive within your budget. You can set what boost you want to buy and leave out, in the globals python file.


### Standard Commands

This creates threads for each of the different basic commands such as !work, !tips, !daily and so on. Commands with a cooldown basically, and runs the commands based on the cooldown± some time to not make it easy to detect. This also includes the overtime command, the farmer will automatically check if you are in a franchise and if so, runs the franchise only commands.


### Gambling Commands

The bot will take the list of gambling commands listed in the global file, and runs them every 30 mins or so. It will run multiple times and it will also SOMEWHAT check your balance to see if you have enough. I didn't add an feature to find out the gambling price, for commands such as !roll and !scratch, so you will have to manually change the amount.


### Auto Sell To Customers

So this one is useful as heck. The tacobot has this other bot which would request to buy tacos from users ( only in whitelisted servers ), and users has to respond with the word "sell", to sell the tacos. Whoever sells it first, gets the money. So my farmer checks if there is a message from the customer bot requesting to sell, and uses the chance in the global file to send the sell message or not. 


### Watch Dog

This is a pretty useful feature if you do not want to get caught. It sends all messages it receives in DM to a logging channel listed in the config file, and also sends messages with certain words listed in the global file. This is useful if people are trying to chat with you, so you can KINDA have a chance to respond back.


### Auto Coupons/Claim/Gift

The farmer will check if you have any available coupons and then sends the redeem commands according to how many coupons you have left. It will also check if you have any gifts left and sends the gift to a random user listed in the config file. Furthermore, it can also claim any task my farmer has completed.


### Auto Rest

It basically rolls a dice and randomly rests the entire bot. This just allows the farmer to not be in the top 10 leaderboards for things such as the most shifts worked and so on. 


# Config
- **Tokens** - A list of tokens you want the farmer to log into and use.
- **Owner ID** - The owner ID, not used yet.
- **Log ID** - Channel ID of the text channel you want the bot to send logs to.
- **Gift ID** - User ID of the user you want to auto send gifts to, it's a list and it will pick randomly from the list.
- **Channel ID** - UNIQUE text channels DEDICATED to ONE BOT. So if you have 3 bots running, you will need 3 different channel IDs.
- **Secondary Channel ID** - Channels you want the farmer to send random commands to, either to level up or to make it less suspicious.
- **Bot ID** - The TacoShack bot's ID. It will read this bot's messages, so make sure it's right.
- **Customer Bot ID** - The bot's ID of the customer's bot in the official server or other whitelisted server.
- **Bot Prefix** - The bot's prefix.
- **Gambling Amount** - Just for the slots command, I don't use it personally use it, so up to you. It's a list of numbers the bot will randomly pick.

# Global
- **Total Bot** - Used internally.
- **Clients Config** - Used internally.
- **Secondary Channel CMD** - List of commands you want to send to the second channel randomly.
- **Watch Dog** - For now, there is only one key, keywords, this includes the keywords you want to log.
- **Cooldown CMD** - This has all the cooldown commands you want to run. It includes, the cmd ( list ), cooldown ( int ) and franchise cmd ( bool ) if its a franchise only command.
- **Gambling CMD** - List of gambling commands you want the bot to use.
- **Boost CMD** - Used internally.
- **Process CMD** - List of commands you want to use for the Auto Upgrades.
- **Random CMD** - List of random commands the farmer will send every now and then.
- **Balance CMD** - List of commands the bot will use to check your user's balance.
- **Ads IDs - Boost IDs** - Used to identify the items in the list. Change this if they add new items in the shops.
- **AutoUpgrades** - Used internally.
- **Processing Key** - The words the farmer will find within the tacobot's messages for certain things. Change this if the tacobot changes some parts.
- **Chances CMD** - Chance from 0 - 100 on how likely it will happen. 10 being 10% and so on.

# Setup

My farmer uses a different discord.py listed in https://github.com/dolfies/discord.py-self, so please **DO NOT** use the official package as the self bot WILL NOT work.

### Packages Used
```sh
aiohttp==3.7.4.post0
async-timeout==3.0.1
attrs==21.2.0
certifi==2021.5.30
chardet==4.0.0
discord.py-self==1.8.1
idna==2.10
... 
