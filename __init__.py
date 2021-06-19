import discord, config, random, globals
import framer, asyncio, helper, bot, time
from datetime import datetime

clients = []
loop = asyncio.get_event_loop()

for x in range(len(config.token)):
    clients.append(bot.FrammerBot())
    loop.create_task(clients[x].start(config.token[x]))

loop.run_forever()
