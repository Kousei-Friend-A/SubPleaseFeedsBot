
from requests import get
from pyrogram import Client , filters
import os
import time

bot = Client(
    ":memory:",
    api_id= 17945796,
    api_hash= "4a05481a5da2d66f801acffc4ca5ee4b"
    bot_token= "5687118765:AAGd2l-MkzzPX2-43X96i8h1D1jRAML8g3Q"
)

CHAT_ID = -1001717995680



db = {
    "latest": None
}

# fake db


kek = []




async def feeds():
    async with bot:
        while True:

            url = 'https://subsplease.org/api/?f=latest&tz=Canada/central'
            res = get(url).json()

            k = None
            for x in res:
                kek.append(x)


            anime_name = res[kek[0]]['show']
            ep = res[kek[0]]['episode']




            lnk = res[kek[0]]['downloads']
            
            last = db['latest'] or ""
            
            if last != anime_name:

            

                for x in lnk:
                    quality = x['res']
                    links = x['magnet']
                    

                    data = f"{quality}: ```{links}```\n\n"

                    if k:
                        k = f"{k}\n{data}"

                    else:
                        k = data

                db['latest'] = anime_name
                await bot.send_message(int(CHAT_ID) , f"**{anime_name}** **Ep**: {ep}:\n\n{k}" , parse_mode="markdown")
                print(db)
                time.sleep(300)

    
    
    

    
bot.run(feeds())
