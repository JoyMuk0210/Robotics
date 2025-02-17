from machine 
import Pin,ADC
import time 

buttonr = Pin(14, Pin.IN, Pin.PULL_DOWN) 
ledr = Pin(28, Pin.OUT)
buttonr_state = buttonr.value()

buttong = Pin(15, Pin.IN, Pin.PULL_DOWN) 
ledg = Pin(27, Pin.OUT)
buttong_state = buttong.value()

ldr=ADC(Pin(26))
threshold=1000

while True:
    prevr=buttonr_state
    buttonr_state=buttonr.value()
    if buttonr_state > prevr: 
        ledr.toggle()  
        time.sleep(0.5)  
    prevg=buttong_state
    buttong_state=buttong.value()
    if buttong_state > prevg: 
        ledg.toggle()  
        time.sleep(0.5)  

    ldr_value = ldr.read_u16()
    print("LDR value is ",ldr_value)
    if ldr_value > threshold:
        ledg.value(0)
    else:
        ledg.value(1)
