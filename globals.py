total_bots = 1
clients_config = dict()


secondary_channel_cmd = ["work", "tip", "roll", "scratch", "cooldowns", "tasks", 'overtime']

watchdog = {
    "keywords": ["selfbot", "contionmig"]
}

# cmd name and alternate cmds, cooldown ( mins ), franchise cmd
cooldown_cmd = [
    {
        "cmd": ["work"],
        "cooldown": 600,
        "franchise_cmd": False
    },
    {
        "cmd": ["tips"],
        "cooldown": 300,
        "franchise_cmd": False
    },
    {
        "cmd": ["overtime"],
        "cooldown": 1800,
        "franchise_cmd": True
    },
    {
        "cmd": ["daily"],
        "cooldown": 86400,
        "franchise_cmd": False
    },
    {
        "cmd": ["clean"],
        "cooldown": 86400,
        "franchise_cmd": False
    },
    {
        "cmd": ["gift"],
        "cooldown": 86400,
        "franchise_cmd": False
    }
]

gambling_cmd = ["roll", "scratch"]
daily_cmd = ["daily", "clean"]
boost_cmd = ["boosts", "shop"]
process_cmd = ["employees", "advertisements", "decorations", "upgrades", "shack"]

random_cmd = ["cooldowns", "tasks", "coupons", "gift"]
balance_cmd = ["profile", "shack"]

ads_id = ['newspaper', 'radio', 'email', 'internet', 'tv', 'blimp']
employees_id = ['apprentice', 'cook', 'advertiser', 'greeter', 'sous', 'head', 'executive']
deco_id = ['flowers', 'ornaments', 'lights', 'mural', 'statue']
upgrade_id = ['paint', 'furniture', 'bathrooms', 'billboard', 'appliances', 'tipjar']
booster_id = ['flipper', 'karaoke', 'music', 'airplane', 'chef']

# word to find, list of shit to buy, starting cmd
autoupgrades = [["'title': 'Decorations", deco_id, "buy", "decorations"],
                ["'title': '🔹 Shack Shop  🔹'", booster_id, "buy", "shop"],
                ["'title': 'Advertisements ", ads_id, "buy", "advertisements"],
                ["'title': 'Upgrades ", upgrade_id, "buy", "upgrades"],
                ["'title': 'Employees ", employees_id, "hire", "employees"]]


processing_key = {
    "balance_key": ["💵 $", "**Balance:** $", "You now have $"],
    "active_boost": ["'title': '📈 Active Boosts'"],
    "coupons": ["'description': '🧾 **You have `"],
    "claim_task": ["You have completed a daily goal: ", "*Ready to Claim*"],
    "franchise": [", {'value': '🏢 "],
    "not_enough": ["You don't have enough money!"],
    "customer_sell": ["I'm feeling a little extra hungry today, could I buy"],
    "gift": ["'description': '🎁 You have **"]
}

chances_cmd = {
    "secondary_channel": 60,
    "customer_sell": 20,
    "gambling_rest": 40,
    "rest_all_cmd": 5,
}