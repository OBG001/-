##############
# code: Improving data quality 
# version: 0.1.1
# by: obg
##############


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
            
    return success_count
