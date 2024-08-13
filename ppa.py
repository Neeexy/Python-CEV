def print_animado(msg,time=0.03):
    for letra in msg:
        print(letra,end='',flush=True)
        sleep(time)
from time import sleep