# P5-Encoder

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con un encoder.

### Funcionamiento del programa

Nuestro programa se encargara de ir contando cuantos huecos han atravesado el encoder durante 30 segundos, despues, simplemente dividira
la cuenta entre el numero de huecos para obtener las vueltas, multiplicara el numero de vueltas por 2*pi para obtener las revoluciones, y
dividira entre el numero de segundos trancurridos y multiplicara por 60 para obtener las revoluciones por minuto.

```python
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
```

**A destacar:**

El evento que aumenta la cuenta del contador de huecos se ejecuta cada vez que detecta un cambio en la señal del gpio. Esto se ha hecho asi
ya que hay veces que no detecta las subidas o bajadas provocando un error en la cuenta que curiosamente no ocurre realizando este cambio.
Aunque de primeras puedas pensar que entonces se va a contar 2 veces el hueco al detectar un doble cambio de la señal(rueda-hueco y hueco
-rueda(2 cambios de la señal para un solo hueco)), curiosamente, no es así.

```python
hilo1 = threading.Thread(target=GPIO.add_event_detect(pulsadorGPIO1, GPIO.BOTH,
      callback=comportamintoEncoder, bouncetime=1))
```
Para ver un video de la practica y el esquema de conexion pulsa [aqui]([aqui](https://drive.google.com/file/d/1LNC3v44mUW_4co6VeOfFKkEQ0VkQVgdz/view?usp=sharing).

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
