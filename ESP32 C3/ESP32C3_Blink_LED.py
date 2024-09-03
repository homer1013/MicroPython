import time
from machine import Pin

p8 = Pin(8, Pin.OUT)
#p9 = Pin(9, Pin.IN)

def blink():

	for _ in range(0, 5): 
		p8.on()
		time.sleep_ms(500)
		p8.off()
		time.sleep_ms(500)
		p8.on()
		time.sleep_ms(500)
		p8.off()
		time.sleep_ms(500)
		p8.on()
		time.sleep_ms(500)

#if p9.value() == 1:
	
blink()

#else:

	#None