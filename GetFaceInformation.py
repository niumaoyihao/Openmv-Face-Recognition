import sensor, image, pyb
RED_LED_PIN = 1
BLUE_LED_PIN = 3
sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.B128X128) # or sensor.QQVGA (or others)
sensor.set_windowing((92,112))
sensor.skip_frames(10) # Let new settings take affect.
sensor.skip_frames(time = 2000)
num = 2
n = 20 
while(n):
    pyb.LED(RED_LED_PIN).on()
    sensor.skip_frames(time = 1000) 
    pyb.LED(RED_LED_PIN).off()
    pyb.LED(BLUE_LED_PIN).on()
    print(n)
    sensor.snapshot().save("face/s%s/%s.pgm" % (num, n) ) 
    n -= 1
    pyb.LED(BLUE_LED_PIN).off()
    print("Done! Reset the camera to see the saved image.")
print("finished!")
