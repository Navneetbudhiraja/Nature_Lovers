#created by @Mr_Hops
"""insta save: Avaible commands: .insta <link>
"""


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="insta ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@Regrambot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=274562699))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Unblock @Regrambot```")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("😐")
          else: 
             await event.delete()
             await event.client.send_file(event.chat_id, response.message)
