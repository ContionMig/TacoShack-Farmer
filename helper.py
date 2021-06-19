import config, random, asyncio, globals
from datetime import datetime


def cmd(text):
    text = str(text)

    text = text.replace("%", str(random.choice(config.gambling_amount)))

    text = config.bot_prefix + text

    return text


def logs(client, text):
    print(client.user.name, ": ", str(datetime.now()), " - ", str(text))


async def sendmsg(client, message):
    if config.auto_rest:
        if chance_machine(globals.chances_cmd["rest_all_cmd"]):

            logs(client, "Resting all commands!")
            globals.clients_config[str(client.user.id)]["rest_cmd"] = True
            await asyncio.sleep(random.randint(1800, 2800))
            globals.clients_config[str(client.user.id)]["rest_cmd"] = False

        while globals.clients_config[str(client.user.id)]["rest_cmd"]:
            await asyncio.sleep(2)

    if random.randint(0, 20) > 18:
        globals.clients_config[str(client.user.id)]["cmd_list"].append(random.choice(globals.random_cmd))

    globals.clients_config[str(client.user.id)]["cmd_list"].append(message)

    while len(globals.clients_config[str(client.user.id)]["cmd_list"]) > 1:
        await asyncio.sleep(1)


async def processcmd(client, text):
    text = str(text)

    find_index = text.find(" Please slow down!")
    if find_index > -1:
        logs(client, "Cooldown Detected! Forcing Rest")
        await asyncio.sleep(random.randint(3, 5))
        await sendmsg(client, globals.clients_config[str(client.user.id)]["last_cmd"])
        return

    bal_str = ""
    for x in range(len(globals.processing_key["balance_key"])):
        find_index = text.find(globals.processing_key["balance_key"][x])
        if find_index > -1:
            find_index += len(str(globals.processing_key["balance_key"][x]))
            while True:
                bal_str += str(text[find_index])

                find_index += 1
                if not text[find_index].isnumeric() and not text[find_index] == ",":
                    break

            bal_str = bal_str.replace(",", "")
            globals.clients_config[str(client.user.id)]["user_balance"] = int(bal_str)
            logs(client, "New Balance: " + str(bal_str))

    for y in range(len(globals.autoupgrades)):
        find_index = text.find(globals.autoupgrades[y][0])
        if find_index > -1:
            split_id = [0]
            text_list = []
            cost_list = []

            for x in range(len(globals.autoupgrades[y][1])):
                split_id.append(text.find("ID: `" + str(globals.autoupgrades[y][1][x]) + "`"))

            split_id.append(len(text))
            for x in range(len(split_id) - 1):
                text_list.append(text[split_id[x]:split_id[x + 1]])

            for x in range(len(text_list)):
                find_index = text_list[x].find("Cost: $")
                bal_str = ""
                if find_index > -1:
                    find_index += len(str("Cost: $"))
                    while True:
                        bal_str += str(text_list[x][find_index])

                        find_index += 1
                        if text_list[x][find_index] == "\\":
                            break

                    bal_str = bal_str.replace(",", "")
                    cost_list.append(int(bal_str))
                else:
                    cost_list.append(0)

            for x in range(len(globals.autoupgrades[y][1])):

                found = False

                list_name = "prices"
                if globals.autoupgrades[y][1][x] in globals.booster_id:
                    list_name = "booster_prices"

                for z in range(len(globals.clients_config[str(client.user.id)][list_name])):

                    if z > int(len(globals.clients_config[str(client.user.id)][list_name])) - 1:
                        break

                    if globals.clients_config[str(client.user.id)][list_name][z]["name"] == globals.autoupgrades[y][1][x]:

                        if cost_list[x] < 1:
                            globals.clients_config[str(client.user.id)][list_name].pop(z)
                        else:
                            globals.clients_config[str(client.user.id)][list_name][z] = {
                                'name': globals.autoupgrades[y][1][x],
                                'price': cost_list[x],
                                'cmd': globals.autoupgrades[y][2],
                                'parent': globals.autoupgrades[y][3]
                            }
                        found = True

                if not found:
                    globals.clients_config[str(client.user.id)][list_name].append({
                        'name': globals.autoupgrades[y][1][x],
                        'price': cost_list[x],
                        'cmd': globals.autoupgrades[y][2],
                        'parent': globals.autoupgrades[y][3]
                    })

    for x in range(len(globals.processing_key["active_boost"])):
        find_index = text.find(globals.processing_key["active_boost"][x])
        if find_index > -1:
            for z in range(len(globals.booster_id)):
                if text.lower().find(globals.booster_id[z]) > -1:
                    logs(client, globals.booster_id[z] + ": Active")
                    globals.clients_config[str(client.user.id)]["booster_active"][z] = True
                else:
                    logs(client, globals.booster_id[z] + ": Inactive")
                    globals.clients_config[str(client.user.id)]["booster_active"][z] = False

    if config.auto_coupon:
        for x in range(len(globals.processing_key["coupons"])):
            find_index = text.find(globals.processing_key["coupons"][x])
            if find_index > -1:
                coupons_str = ""
                find_index += len(str(globals.processing_key["coupons"][x]))
                while True:
                    coupons_str += str(text[find_index])

                    find_index += 1
                    if not text[find_index].isnumeric() and not text[find_index] == ",":
                        break

                coupons_str = coupons_str.replace(",", "")
                logs(client, "Coupons Redeeming: " + str(coupons_str))
                for y in range(int(coupons_str)):
                    await sendmsg(client, "redeem")

    if config.auto_gift:
        for x in range(len(globals.processing_key["gift"])):
            find_index = text.find(globals.processing_key["gift"][x])
            if find_index > -1:
                gifts_str = ""
                find_index += len(str(globals.processing_key["gift"][x]))
                while True:
                    gifts_str += str(text[find_index])

                    find_index += 1
                    if not text[find_index].isnumeric() and not text[find_index] == ",":
                        break

                gifts_str = gifts_str.replace(",", "")
                logs(client, "Gift Redeeming: " + str(gifts_str))
                for y in range(int(gifts_str)):
                    await sendmsg(client, "gift <@{id}>".format(id=random.choice(config.gift_id)))

    if config.auto_claim:
        for x in range(len(globals.processing_key["claim_task"])):
            find_index = text.find(globals.processing_key["claim_task"][x])
            if find_index > -1:
                logs(client, "Completed daily task! Claiming")
                await sendmsg(client, "g claim")

    for x in range(len(globals.processing_key["franchise"])):
        find_index = text.find(globals.processing_key["franchise"][x])
        if find_index > -1:
            franchise_str = ""
            find_index += len(str(globals.processing_key["franchise"][x]))
            while True:
                franchise_str += str(text[find_index])

                find_index += 1
                if text[find_index] == "'":
                    break

            if not franchise_str == "None (`f help`)":
                globals.in_franchise = True

    for x in range(len(globals.processing_key["not_enough"])):
        find_index = text.find(globals.processing_key["not_enough"][x])
        if find_index > -1:
            globals.not_enough_money = True


def price_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j]['price'] > array[j + 1]['price']:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array


def chance_machine(chance):
    if random.randint(0, 100) < int(chance):
        return True
    return False
