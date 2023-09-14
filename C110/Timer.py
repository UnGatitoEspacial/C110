#inportar el modulo 
import time
#define de la cuenta regresiva de la funcion timer
def countdown_timer(seconds): 
    while seconds >0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        seconds -=1
    print('se acabo el tiempo')
#input time en segundos 
seconds=input("escribe el tiempo en numeros de segundos:")

#llama a la funcion
countdown_timer(int(seconds))