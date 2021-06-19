import discord, config, random, globals
import framer, asyncio, helper, bot, time
from datetime import datetime

'''
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    globals.watchdog["keywords"].append(str(client.user.id))
    await client.wait_until_ready()
    asyncio.create_task(framer.MessageHandler(client))

    if config.standard_module:
        helper.logs("Task Created: StandardCommands")
        asyncio.create_task(framer.StandardCommands(client))
        await asyncio.sleep(random.randint(60, 90))
    if config.auto_upgrade_module:
        helper.logs("Task Created: AutoUpgradeCommands")
        asyncio.create_task(framer.AutoUpgradeCommands(client))
        await asyncio.sleep(random.randint(60, 90))

    if config.boost_module:
        helper.logs("Task Created: BoostCommands")
        asyncio.create_task(framer.BoostCommands(client))
        await asyncio.sleep(random.randint(60, 90))

    if config.gambling_module:
        helper.logs("Task Created: GamblingCommands")
        asyncio.create_task(framer.GamblingCommands(client))
        await asyncio.sleep(random.randint(60, 90))

    if config.daily_module:
        helper.logs("Task Created: DailyCommands")
        asyncio.create_task(framer.DailyCommands(client))


@client.event
async def on_message(message):
    if config.autosell_module and message.author.id == config.customer_bot_id:
        for x in range(len(globals.processing_key["customer_sell"])):
            find_index = message.content.find(globals.processing_key["customer_sell"][x])
            if find_index > 0:
                helper.logs("Customer Requested Selling!")

                if helper.chance_machine(globals.chances_cmd["customer_sell"]):
                    if len(globals.cmd_list) == 0:
                        helper.logs("Sold!")
                        await client.get_channel(message.channel.id).send("sell")
                        helper.logs("Sent Sold!")

    if message.channel.id == config.channel_id and message.author.id == config.bot_id:
        embeds = message.embeds
        for embed in embeds:
            await helper.processcmd(client, str(embed.to_dict()))

    if config.watchdog_module and not message.channel.id == config.log_id:

        should_log = False
        text =  message.content.lower()
        log_text = "```" + str(datetime.now()) + "```"

        for x in range(len(globals.watchdog["keywords"])):
            if text.find(globals.watchdog["keywords"][x]) > -1:
                should_log = True
                log_text += "<#{chl}> ({chl_name}) - {id} (<@{id}>): {msg}".format(id=message.author.id,
                                                                                   msg=message.content,
                                                                                   chl=message.channel.id,
                                                                                   chl_name=message.channel.name)

        if isinstance(message.channel, discord.channel.DMChannel):
            should_log = True
            log_text += "Private DM - {id} (<@{id}>): {msg}".format(id=message.author.id, msg=message.content)

        if should_log:
            await client.get_channel(config.log_id).send(log_text)
'''

clients = []
loop = asyncio.get_event_loop()

for x in range(len(config.token)):
    clients.append(bot.FrammerBot())
    loop.create_task(clients[x].start(config.token[x]))

loop.run_forever()