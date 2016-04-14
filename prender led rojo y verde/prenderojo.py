import RPi.GPIO as GPIO #importamos la libreria y cambiamos su nombre por "GPIO"
import time #necesario para los delays

#establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)

#configuramos el pin GPIO17 como una salida
GPIO.setup(17, GPIO.OUT)

#encendemos y apagamos el led 5 veces

GPIO.output(17, GPIO.HIGH)
time.sleep(1)
