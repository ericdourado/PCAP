from datetime import datetime
import asyncio

async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados...')
    for i in range(1, quantidade + 1):
        item = i * i
        await dados.put((item, datetime.now()))
        await asyncio.sleep(0.001) 
    print(f'{quantidade} dados gerados com sucesso...')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde o processamento de {quantidade} dados...')
    processados = 0
    while processados < quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0.001)
    print(f'Foram processados {processados} itens')

if __name__ == '__main__':
    total = 200
    dados = asyncio.Queue()
    el = asyncio.get_event_loop()
    print(f'computando {total * 2:.2f} dados.')
    el.run_until_complete(gerar_dados(total, dados))
    el.run_until_complete(gerar_dados(total, dados))
    el.run_until_complete(processar_dados(total * 2, dados))
    el.close()
