import asyncio
from time import sleep

async def espera():
    await asyncio.sleep(5)
    print('teste')
    return 1

def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(espera())
    el.close()


if __name__ == '__main__':
    main()
