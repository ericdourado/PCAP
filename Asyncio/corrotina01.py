import asyncio
async def diz_oi():
    print('Oi...')


# el = asyncio.get_event_loop()
# el.run_util_complete(diz_oi())
# el.close()

asyncio.run(diz_oi())