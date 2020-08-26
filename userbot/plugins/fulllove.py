"""COMMAND : .love"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 40
    

    animation_ttl = range(0, 41)

    input_str = event.pattern_match.group(1)

    if input_str == "love":

        await event.edit(input_str)

        animation_chars = [

            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
            
            "I",
            "I L",
            "I Lo",
            "I Lov",
            "I Love",
            "I Love Y",    
            "I Love Yo",
            "I Love You",
            "I Love You鉂わ笍锔�",
            "I Love You鉂ゐ煒嶏笍锔�",
         
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 41])
