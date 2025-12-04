##############
# code: send_all_message bot for discord 
# version: 0.0.1
# by: obg
##############

import asyncio

async def send_message_to_verified(guild, msg, tag_bot=None, check_func=lambda m: True):

    sent_ids = set()
    count = 0

    for member in guild.members:
        if member.bot:
            continue
        if member.id in sent_ids:
            continue
        if not check_func(member):
            continue

        try:
            await member.send(msg)
            sent_ids.add(member.id)
            count += 1
        except Exception:
            pass  

    return count