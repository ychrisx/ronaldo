import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
trig = machine.Pin(15, machine.Pin.OUT)
echo = machine.Pin(18, machine.Pin.IN)

def medir_distancia():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    pulse_start = 0
    pulse_end = 0
    
    while echo.value() == 0:
        pulse_start = time.ticks_us()
        
    while echo.value() == 1:
        pulse_end = time.ticks_us()
        
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distancia = (pulse_duration * 0.0343) / 2
    
    return distancia

while True:
    distancia = medir_distancia()
    print("Distância: ", distancia, "cm")
    if distancia <= 10:
        led.value(1) 
    else:
        led.value(0)
    time.sleep(1)
