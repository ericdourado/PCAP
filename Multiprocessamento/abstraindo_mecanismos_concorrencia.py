import time
# from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor


def processa():
    print('[', end='', flush=True)
    for n in range(1,11):
        print('#', end='', flush=True)
        time.sleep(0.2)
    print(']', end=' ', flush=True)
    return 'sucess'

if __name__ == '__main__':
    with Executor() as executor:
        future = executor.submit(processa)
    print(f'O retorno foi: {future.result()}')
