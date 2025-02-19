import time
from machine import ADC,Pin,I2C
from i2c_lcd import I2cLcd
time.sleep(0.1) # Wait for USB to become ready

i2c=I2C(0,scl=Pin(21),sda=Pin(20),freq=400000)
i2c_addr=i2c.scan()[0]
lcd1=I2cLcd(i2c,i2c_addr,2,16)
lcd1.clear()

btn1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
btn2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
light = Pin(0,Pin.OUT)
fan = Pin(2,Pin.OUT)
ldr=ADC(26)
pot=ADC(27)
buz=Pin(14,Pin.OUT)

temp_min=30

while True:

   if btn1.value():
      light.toggle()
      time.sleep(1)

   if btn2.value():
      fan.toggle()
      time.sleep(1)

   light_level=ldr.read_u16()
   #light intensity from 0 to 1000 units
   lux_value=(light_level/65535)*1000
   if lux_value<=300:
      light.on()
      lcd1.putstr("light:ON ")
   else:
      light.off()
      lcd1.putstr("light:OFF ")

   pot_value=pot.read_u16()
   #tempurature from 0 to 100 degrees
   temp=(pot_value/65535)*100
   if temp>temp_min:
      fan.on()
      lcd1.putstr("fan:ON ")
      time.sleep(1)
   else:
      fan.off()
      lcd1.putstr("fan:OFF ")
      time.sleep(1)
   if temp>35:
      buz.on()
      print("buzzing")
      time.sleep(1)
   else:
      buz.off()
      time.sleep(1)

   temp_gif=temp-temp%1
   lux_value_gif=lux_value-lux_value%1
   lcd1.putstr("light:"+str(lux_value_gif)+" ")
   if lux_value<=100:     
      lcd1.putstr("night")
   lcd1.putstr("temp:"+str(temp_gif)+" ")
   print("light:"+str(lux_value)+" ")
   print("temp:"+str(temp))
   time.sleep(0.5)

   

