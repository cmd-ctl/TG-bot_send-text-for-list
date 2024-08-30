import os
from dotenv import load_dotenv
from telethon import TelegramClient
import datetime
import asyncio

load_dotenv()
# ---- APP Settings ----
api_id = int(os.environ.get("TG_API_ID"))
api_hash = os.environ.get("TG_API_HASH")
session_name = os.environ.get("SESS_HASH_NAME")
num = os.environ.get("PHONE")

print(">> Starting...")

client = TelegramClient(session_name, api_id, api_hash, system_version="4.16.30-vxCUSTOM")
client.start(phone=num)

# ---- Telegram recipients Set ----
array = list(open('list.txt'))
print("RECIPIENTS: " + str(array))

# ---- Get post data from ENV ----
sdtxt = f"""{os.environ.get("TEXT")}"""

print("TEXT: " + sdtxt)
print(">> Sending...\n")
async def main():
    global j
    j = 0
    for i in array:
        curtime = datetime.datetime.today().strftime("%H:%M:%S")
        try:
            channel_link = f"https://t.me/" + array[j].strip()
            client.parse_mode="html"
            await client.send_message(channel_link, str(sdtxt), parse_mode='html')
            print(f"[{curtime}] Message sent OK: {channel_link} ")
        except Exception as error:
            channel_link = f"https://t.me/" + array[j].strip()
            print(f"[{curtime}] Message sent ERROR: {channel_link}, reason:", error)
        j += 1

asyncio.get_event_loop().run_until_complete(main())
print(">> Complete. Press any key to exit")
input()


