"""Emoji
Available Commands:
.3Cube"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 31)

    input_str = event.pattern_match.group(1)

    if input_str == "3Cube":

        await event.edit(input_str)

        animation_chars = [

            "👑3Cube👑👑👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️◼️️👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️◼️◼️👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "‎◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑3Cube👑👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑3Cube👑👑3Cube👑◼️◼️\n◼️👑3Cube👑👑3Cube👑👑3Cube👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑3Cube👑👑3Cube👑◼️◼️\n◼️👑3Cube👑👑3Cube👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑3Cube👑👑3Cube👑◼️◼️\n◼️👑3Cube👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑3Cube👑👑3Cube👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑3Cube👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            
            "👑 3Cube 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
