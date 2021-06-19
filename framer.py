import asyncio, config, random, globals, helper
from helper import sendmsg, cmd, logs, chance_machine


async def StandardCommandsLoop(client, cmd_list):
    while True:
        if cmd_list["franchise_cmd"] and globals.clients_config[str(client.user.id)]["in_franchise"]:
            await helper.sendmsg(client, random.choice(cmd_list["cmd"]))
        else:
            await helper.sendmsg(client, random.choice(cmd_list["cmd"]))

        await asyncio.sleep(random.randint(int(cmd_list["cooldown"] + 30), int(cmd_list["cooldown"] * 1.25 + 30)))


async def StandardCommands(client):
    for x in range(len(globals.cooldown_cmd)):
        helper.logs(client, "Command Loop Started: " + str(globals.cooldown_cmd[x]["cmd"]))
        asyncio.create_task(StandardCommandsLoop(client, globals.cooldown_cmd[x]))
        await asyncio.sleep(random.randint(3, 10))


async def GamblingCommands(client):
    while True:
        random.shuffle(globals.gambling_cmd)

        if globals.clients_config[str(client.user.id)]["user_balance"] > 30000:

            if globals.clients_config[str(client.user.id)]["not_enough_money"]:
                logs(client, "Resting ( Not Enough Money ): GamblingCommands")
                await asyncio.sleep(random.randint(1000, 2200))
                globals.not_enough_money = False

            for x in range(len(globals.gambling_cmd)):
                for y in range(random.randint(1, 10)):
                    await sendmsg(client, globals.gambling_cmd[x])
                    await asyncio.sleep(random.randint(10, 20))

            if chance_machine(globals.chances_cmd["gambling_rest"]):
                logs(client, "Resting: GamblingCommands")
                await asyncio.sleep(random.randint(1000, 2200))

            await asyncio.sleep(random.randint(5, 300))
        else:
            await asyncio.sleep(random.randint(5, 300))


async def BoostCommands(client):
    while True:
        random.shuffle(globals.boost_cmd)

        for x in range(len(globals.boost_cmd)):
            await sendmsg(client, globals.boost_cmd[x])
            await asyncio.sleep(random.randint(10, 20))

        await asyncio.sleep(random.randint(30, 60))
        for x in range(len(globals.booster_id)):
            if not globals.clients_config[str(client.user.id)]["booster_active"][x]:
                for z in range(len(globals.clients_config[str(client.user.id)]["booster_prices"])):
                    if globals.clients_config[str(client.user.id)]["booster_prices"][z]["name"] == globals.booster_id[x]:
                        if globals.clients_config[str(client.user.id)]["booster_prices"][z]['price'] < globals.clients_config[str(client.user.id)]["user_balance"]:
                            await sendmsg(client, str(globals.clients_config[str(client.user.id)]["booster_prices"][z]['cmd'] + " " + globals.clients_config[str(client.user.id)]["booster_prices"][z]['name']))
                            await sendmsg(client, random.choice(globals.balance_cmd))
                            await asyncio.sleep(random.randint(5, 20))

        logs(client, "Done: BoostCommands")
        await asyncio.sleep(random.randint(3600, 5600))


async def AutoUpgradeCommands(client):

    globals.clients_config[str(client.user.id)]["prices"] = []

    await sendmsg(client, random.choice(globals.balance_cmd))
    await asyncio.sleep(random.randint(5, 7))

    random.shuffle(globals.process_cmd)

    for x in range(len(globals.process_cmd)):
        await sendmsg(client, globals.process_cmd[x])
        await asyncio.sleep(random.randint(2, 5))

    await asyncio.sleep(random.randint(5, 15))
    logs(client, "Done Processing: AutoUpgradeCommands")

    while True:
        globals.clients_config[str(client.user.id)]["prices"] = helper.price_sort(globals.clients_config[str(client.user.id)]["prices"])
        logs(client, "Price List: " + str(globals.clients_config[str(client.user.id)]["prices"]))

        if len(globals.clients_config[str(client.user.id)]["prices"]) > 0:
            while globals.clients_config[str(client.user.id)]["prices"][0]['price'] < globals.clients_config[str(client.user.id)]["user_balance"]:
                    await sendmsg(client, str(globals.clients_config[str(client.user.id)]["prices"][0]['cmd'] + " " + globals.clients_config[str(client.user.id)]["prices"][0]['name']))
                    await sendmsg(client, globals.clients_config[str(client.user.id)]["prices"][0]['parent'])
                    await asyncio.sleep(random.randint(5, 15))

        logs(client, "Finished Ordering: AutoUpgradeCommands")
        await asyncio.sleep(random.randint(300, 1000))


async def MessageHandler(client):
    while True:
        if len(globals.clients_config[str(client.user.id)]["cmd_list"]) > 0:
            logs(client, cmd(globals.clients_config[str(client.user.id)]["cmd_list"][0]) + " | Queue: " + str(globals.clients_config[str(client.user.id)]["cmd_list"]))

            globals.clients_config[str(client.user.id)]["last_cmd"] = globals.clients_config[str(client.user.id)]["cmd_list"][0]

            if globals.clients_config[str(client.user.id)]["cmd_list"][0] in globals.secondary_channel_cmd and config.secondary_channels:
                if chance_machine(globals.chances_cmd["secondary_channel"]):
                    logs(client, "Sent to secondary channel!")
                    await client.get_channel(random.choice(config.secondary_channel_id)).send(cmd(globals.clients_config[str(client.user.id)]["cmd_list"][0]))
                else:
                    await client.get_channel(globals.clients_config[str(client.user.id)]["channel"]).send(cmd(globals.clients_config[str(client.user.id)]["cmd_list"][0]))
            else:
                await client.get_channel(globals.clients_config[str(client.user.id)]["channel"]).send(cmd(globals.clients_config[str(client.user.id)]["cmd_list"][0]))
                
            globals.clients_config[str(client.user.id)]["cmd_list"].pop(0)

        await asyncio.sleep(random.randint(2, 6))
