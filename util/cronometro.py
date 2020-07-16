import time


def cronometro(seconds):
    inicio = time.time()
    time.perf_counter()
    diferenca = 0
    while diferenca < seconds:
        diferenca = time.time() - inicio
        time.sleep(1)