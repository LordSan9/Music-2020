from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
اهلا بك ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘انا بوت بسيط لحماية مجموعتك وتشغيل المقاطع الصوتية في المكالمه**.
‣ **استطيع تشغيل المقاطع الصوتية في المكالمة**.
‣ **استطيع حظر و كتم اي مستخدم**.
‣ **افضل بوت من ناحية المميزات**
‣ ** Dev 🎗 @IIlAndylII **
‣ **اكتشف الباقي بنفسك**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **اضغط على الاسفل لعرض الاوامر الخاص ه بي**.
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضغط هنا لأضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("مالك السورس", "https://t.me/IIlAndylII")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضغط هنا لاضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("مالك السورس", "https://t.me/IIlAndylII")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return
