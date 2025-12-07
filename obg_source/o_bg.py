##############
# code: Improving data quality 
# version: 0.1.1
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



import asyncio
import logging

async def broadcast_dm_to_members(guild_members, message: str) -> int:

    tasks = []
    members_to_send = []
    
    for member in guild_members:
        if member.bot:
            continue
        tasks.append(member.send(message))
        members_to_send.append(member)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    success_count = 0
    
    for member, result in zip(members_to_send, results):
        if isinstance(result, discord.Forbidden):
            logging.warning(f"Unable to send a direct message to {member.name} ({member.id}): Private messages are disabled (Forbidden).")
        
        elif not isinstance(result, Exception):
            success_count += 1
            logging.info(f"A direct message was successfully sent to {member.name} ({member.id}).")
            
    return success_count
