import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/49b38ffc45115d3b5cb33.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@IIlAndylII"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/IIlAndylII")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
