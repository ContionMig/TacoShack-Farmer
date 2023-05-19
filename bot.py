from multiprocessing.connection import Client
import os
import token
import discord
import config, random, globals
import framer, asyncio, helper
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
bot = commands.Bot(command_prefix=config.bot_prefix, self_bot=True)

class FrammerBot(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

        globals.clients_config[str(self.user.id)] = {
            "channel": config.channel_id[globals.total_bots],
            "cmd_list": [],
            "last_cmd": "",
            "user_balance": 0,
            "in_franchise": False,
            "rest_cmd": False,
            "not_enough_money": False,
            "booster_active": [False for i in range(len(globals.booster_id))],
            "prices": [],
            "booster_prices": []
        }

        globals.total_bots += 1

        await self.wait_until_ready()
        asyncio.create_task(framer.MessageHandler(self))

        if config.standard_module:
            helper.logs(self, "Task Created: StandardCommands")
            asyncio.create_task(framer.StandardCommands(self))
            await asyncio.sleep(random.randint(60, 90))

        if config.auto_upgrade_module:
            helper.logs(self, "Task Created: AutoUpgradeCommands")
            asyncio.create_task(framer.AutoUpgradeCommands(self))
            await asyncio.sleep(random.randint(60, 90))

        if config.boost_module:
            helper.logs(self, "Task Created: BoostCommands")
            asyncio.create_task(framer.BoostCommands(self))
            await asyncio.sleep(random.randint(60, 90))

        if config.gambling_module:
            helper.logs(self, "Task Created: GamblingCommands")
            asyncio.create_task(framer.GamblingCommands(self))
            await asyncio.sleep(random.randint(60, 90))

    async def on_message(self, message):

        if str(self.user.id) in globals.clients_config:
            if config.autosell_module and message.author.id == config.customer_bot_id:
                for x in range(len(globals.processing_key["customer_sell"])):
                    find_index = message.content.find(globals.processing_key["customer_sell"][x])
                    if find_index > 0:
                        helper.logs(self, "Customer Requested Selling!")

                        if helper.chance_machine(globals.chances_cmd["customer_sell"]):
                            if len(globals.clients_config[str(self.user.id)]["cmd_list"]) == 0:
                                helper.logs(self, "Sold!")
                                await self.get_channel(message.channel.id).send("sell")
                                helper.logs(self, "Sent Sold!")

            if message.channel.id == globals.clients_config[str(self.user.id)]["channel"] and message.author.id == config.bot_id:
                embeds = message.embeds
                for embed in embeds:
                    await helper.processcmd(self, str(embed.to_dict()))

            if config.watchdog_module and not message.channel.id == config.log_id:

                should_log = False
                text = message.content.lower()
                log_text = "```" + str(datetime.now()) + "```"

                for x in range(len(globals.watchdog["keywords"])):
                    if text.find(globals.watchdog["keywords"][x]) > -1 or text.find(str(self.user.id)) > -1:
                        should_log = True

                if isinstance(message.channel, discord.channel.DMChannel):
                    should_log = True

                if should_log:
                    log_text += "{id} (<@{id}>): {msg}".format(id=message.author.id, msg=message.content)
                    await self.get_channel(config.log_id).send(log_text)

bot.run(os.getenv('token'))