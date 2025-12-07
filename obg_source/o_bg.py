##############
# code: smad bot for discord 
# version: 0.0.2
# by: obg
##############

import asyncio

async def smad(guild, msg):

    sent_ids = set()
    count = 0

    for member in guild.members:
        if member.bot:
            continue
        if member.id in sent_ids:
            continue

        try:
            await member.send(msg)
            sent_ids.add(member.id)
            count += 1
        except Exception:
            pass  

    return count
