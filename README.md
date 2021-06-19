# TacoShack-Farmer
[[My Website]](https://mitsuzi.xyz/)

Selfbot framer  for the popular discord gaming bot, TacoShack. It provides many modules, which includes, auto work, auto gift, auto coupon claim, auto upgrade buys and many more

I focused on mainly on being stealthy, adding alot of random variables and timings which would make it slightly harder to detect. Everything the bot sends can be quite random as well, as i made seperate threads for each module, which would make it slightly harder to find a pattern. Other than that, the framer would also sends a random command from the list every now and than along side resting for awhile. Every rest in the framer is also random, plus the cooldown. Other than that, the bot also uses most commands from lists, this includes commands which has alternate commands, for an example, !shack is the same as !b.

# Features

### Multiple Bots

You are able to run multiple bots in the same script. But please make sure each bot has one text channel dedicated to it. As tacoshack does not list who requested most of it's command, my framer can't differentnate who the bot repied to. Therefore, please only use ONE text channel for ONE bot. 


### Secondary Channels

So i coded this mainly due to wanting to leveing up on the offical taco shack server. They have a system where if you use commands and text in their offical discord server, you get EXP which you can use to level up, therefore this feature just sends messages which my framer does not care about the reply or random commands into the secondary channel list


### Auto Upgrade

This is the most useful feature in the framer. It uses all the commands which displays all the different things you can buy and records the price than auto buys the cheapest options from the entire list. It also allows you to use different command for it, for an example, the employees list, requires you to do !hire, while everything else requires !buy. You can set indivisual commands.


### Auto Boost

This allows the framer to check what boost you have active and than buys the boosts which are inactive within your budget. You can set what boost you want to buy and leave out, in the globals python file


### Standard Commands

This creates threads for each of the different basic commands such as !work, !tips, !daily and so on. Commands with a cooldown basically, and runs the commands based on the cooldown +- some time to not make it easy to detect. This also includes the overtime command, the framer will automatically check if you are in a franchise and if so, runs the franchise only commands.


### Gambling Commands

The bot will take the list of gambling commands listed in the global file, and runs them every 30 mins or so. It will run multiple times and it will also SOMEWHAT check your balance to see if you have enough. I didnt add an feature to find out the gambling price, for commands such as !roll and !scrach, so you will have to manually change the amount.


### Auto Sell To Customers

So this one is useful as heck. The tacobot has this other bot which would request to buy tacos from users ( only in whitelisted servers ), and users has to respond with the word "sell", to sell the tacos. Whoever, sells it first gets the money. So my framer checks if there is a message from the customer bot requesting to sell, and uses the chance in the global file to send the sell message or not. 


### Watch Dog

This is a pretty useful feature if you do not want to get caught. It sends all messages it receives in DM to a logging channel listed in the config file, and also sends messages with certain words listed in the global file. This is useful if people are trying to chat with you, so you can KINDA have a chance to respond back


### Auto Coupons/Claim/Gift

The framer will check if you have any avaliable coupons and than sends the redeem commands according to how many coupons you have left. It will also check if you have any gifts left and sends the gift to a random user listed in the config file. Futhermore, it can also claim any task my framer has completed.


### Auto Rest

It basically rolls a dice and randomly rests the entire bot. This just allows the framer to not be in the top 10 leaderboards for things such as the most shifts worked and so on. 


# Config
- **Tokens** - A list of tokens you want the framer to log into and use
- **Owner ID** - The owner id, not used yet
- **Log ID** - Channel ID of the text channel you want the bot to send logs to
- **Gift ID** - User ID of the user you want to auto send gifts to, its a list and it will pick randomly from the list
- **Channel ID** - UNIQUE text channels DEDICATED to ONE BOT. So if you have 3 bots running, you will need 3 different channel ids
- **Secondary Channel ID** - Channels you want the framer to send random commands to, either to level up or to make it less suspious
- **Bot ID** - The TacoShack bot's ID. It will read this bot's messages, so make sure its right
- **Customer Bot ID** - The bot's ID of the customer's bot in the offical server or other whitelisted server
- **Bot Prefix** - The bot's prefix
- **Gambling Amount** - Just for the slots command, i dont use it personally use it, so up to you. Its a list of numbers the bot will randomly pick

# Global
- **Total Bot** - Used internally
- **Clients Config** - Used internally
- **Secondary Channel CMD** - List of commands you want to send to the second channel randomly
- **Watch Dog** - For now, there is only one key, keywords, this includes the keywords you want to log
- **Cooldown CMD** - This has all the cooldown commands you want to run. It includes, the cmd ( list ), cooldown ( int ) and franchise cmd ( bool ) if its a franchise only command.
- **Gambling CMD** - List of gambling commands you want the bot to use
- **Boost CMD** - Used internally
- **Process CMD** - List of commands you want to use for the Auto Upgrades
- **Random CMD** - List of random commands the framer will send every now and than
- **Balance CMD** - List of commands the bot will use to check your user's balance
- **Ads IDs - Boost IDs** - Used to identify the items in the list, change this if they add new items in the shops
- **AutoUpgrades** - Used internally
- **Processing Key** - The words the framer will find within the tacobot's messages for certain things. Change this if the tacobot changes some parts
- **Chances CMD** - Chance from 0 - 100 on how likely it will happen. 10 being 10% and so on.

# Setup

My framer uses a different discord.py listed in https://github.com/dolfies/discord.py-self, so please **DO NOT** use the offical package as the self bot WILL NOT work.

### Packages Used
```sh
aiohttp==3.7.4.post0
async-timeout==3.0.1
attrs==21.2.0
certifi==2021.5.30
chardet==4.0.0
discord.py-self==1.8.1
idna==2.10
multidict==5.1.0
requests==2.25.1
typing-extensions==3.10.0.0
urllib3==1.26.5
yarl==1.6.3
```

