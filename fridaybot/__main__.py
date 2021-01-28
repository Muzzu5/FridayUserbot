import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from fridaybot import bot, client2, client3
from fridaybot.Configs import Config
from fridaybot.utils import load_module, start_assistant, load_module_dclient
from var import Var

sed = logging.getLogger("Friday")

        
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
    
async def lol_s(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)
    
def multiple_client():
    if client2:
        sed.info("Starting Client 2")
        try:
            sedbruh = None
            client2.start()
            client2.loop.run_until_complete(lol_s(client2))
        except:
            sedbruh = True
            sed.info("Client 2 Failed To Load. Check Your String.")
    if client3:
        sed.info("Starting Client 3")
        try:
            lmaobruh = None
            cleint3.start
            client3.loop.run_until_complete(lol_s(client3))
        except:
            lmaobruh = True
            sed.info("Client 3 Failed To Load.")
    if not client2:
        sedbruh = None
    if not client3:
        lmaobruh = None
    return sedbruh, lmaobruh    

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        failed2, failed3 = multiple_client()
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()
        failed2, failed3 = multiple_client()


import glob

path = "fridaybot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
        if failed2 is None:
            load_module_dclient(shortname.replace(".py", ""), client2)
        if failed3 is None:
            load_module_dclient(shortname.replace(".py", ""), client3)

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "fridaybot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    sed.info("Friday And Assistant Bot Have Been Installed Successfully !")
else:
    sed.info("Friday Has Been Installed Sucessfully !")
    sed.info("You Can Visit @FridayOT For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
