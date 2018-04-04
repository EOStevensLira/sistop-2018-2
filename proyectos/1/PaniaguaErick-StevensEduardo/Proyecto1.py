#Paniagua Trejo Erick y Stevens Lira Eduardo Orlando
#Monitor de Sistema
from threading import Semaphore, Thread
from time import time
from subprocess import call
from subprocess import Popen
from subprocess import PIPE
from time import sleep
hilo=0
Semaforo = Semaphore(1)

def Monitor():
    global hilo, u, Semaforo
    t = 0
    while t == 0:
    sleep(.5)
    print ("\tMONITOR\n")
    print ("\nSistema\nArchivos\nMemoria\nProcesos\nCPU\nBorrar\nFecha\n")
    ("\tEscriba los comandos: ")
    comando = input()
    Semaforo.release()
    Monitor()

def CPU():
    global Semaforo
        Semaforo.acquire()
            print ("CPU\n")
                call('system_profiler')
                    semaforo.release()

def Procesos():
    global Semaforo
        semaforo.acquire()
            print ("Procesos actuales\n")
                call('ps')
                    Semaforo.release()

def Archivos():
    global Semaforo
        Semaforo.acquire()
            print (" Archivos del sistema\n")
                call('ls, -a')
                    semaforo.release()

def Memoria():
    global Semaforo
        Semaforo.acquire()
            print ("Memoria\n")
                call("vm_stat")
                    Semaforo.release()

def Sistema():
    global Semaforo
        Semaforo.acquire()
            print ("Arquitectura del sistema\n")
                call('arch')
                    print ("Versión del Kernel del Sistema\n")
                        call('uname, -r')
                            Semaforo.release()

def Borrar():
    global Semaforo
        semaforo.acquire()
            proceso_1 =Popen("clear")
                proceso.wait()
                    Semaforo.release()

def Fecha():
    global Semaforo
        semaforo.acquire()
            call("date")
                Semaforo.release()

def Lanzador(opcion):
    global hilo
    if (opcion == "Sistema"):
    Thread(target = Sistema, args=[]).start()
    elif (opcion == "Disco"):
    Thread(target = Archivos, args=[]).start()
    elif (opcion == "Memoria"):
    Thread(target = Memoria, args=[]).start()
    elif (opcion == "Proceso"):
    Thread(target = Procesos, args = []).start()
    elif (opcion == "CPU"):
    Thread(target = CPU, args = []).start()
    elif (opcion == "Fecha"):
    Thread(target = Fecha, args = []).start()
    elif (opcion == "Borrar"):
    Thread(target = Borrar, args = []).start()
    elif (opcion == "exit"):

print ("\nSaliendo del sistema...")
    hilo=hilo+1
    else:
    print ("\nOpcion invalida")

def hilos():
    Thread(target = Sistema, args=[]).start()
    Thread(target = Archivos, args=[]).start()
    Thread(target = Memoria, args=[]).start()
    Thread(target = Procesos, args=[]).start()
    Thread(target = CPU, args=[]).start()
    Thread(target = Borrar, args=[]).start()
    Thread(target = Fecha, args=[]).start()