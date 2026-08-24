from machine import Pin, ADC
import time


adc_pin = Pin(35)
adc = ADC(adc_pin)
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

MAX_CM = 50.0  

while True:
    valor_analogico = adc.read()
    
    tensao = (valor_analogico / 4095.0) * 3.3
    
    centimetros = (valor_analogico / 4095.0) * MAX_CM
    
    print(f"Bits: {valor_analogico} | Tensão: {tensao:.2f}V | Distância: {centimetros:.1f} cm")
    
    time.sleep(1)
    
