#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO
import time
import threading

pulsadorGPIO1 = 16
contador = 0
flag1 = 0
huecosrueda=4
pi=3.14
printResult=True
def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def comportamintoEncoder (canal):
    global flag1
    global contador
    global printResult
    StopTime = time.time()
    finaltime = 0
    if flag1 == 0:
        StopTime = time.time()
        finaltime = StopTime-StartTime
        contador = contador+1
        flag1 = 1
    else:
        flag1 = 0

    if finaltime > 30 and printResult == True:
        print("Huecos contados")
        print(contador)
        print("revoluciones por minuto = ")
        print(((contador/huecosrueda)*2*pi/finaltime)*60)
        printResult=False

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    StartTime = time.time()

    hilo1 = threading.Thread(target=GPIO.add_event_detect(pulsadorGPIO1, GPIO.BOTH,
      callback=comportamintoEncoder, bouncetime=1))
    hilo1.start()


    hilo1.join()
    signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C que limpia todos los hilos anteriores
    signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar para que no se acabe solo el principal