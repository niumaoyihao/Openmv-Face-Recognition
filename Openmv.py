import sensor, time, image, pyb
from pyb import UART
import json
sensor.reset() 
#sensor.set_hmirror(True)
#sensor.set_vflip(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_whitebal(False)
clock = time.clock()
sensor.set_pixformat(sensor.GRAYSCALE) 
sensor.set_framesize(sensor.B128X128) 
sensor.set_windowing((92,112))
sensor.skip_frames(10) 
sensor.skip_frames(time = 3000)
uart = UART(3, 9600)
SBUF=""
#SUB = "s1"
NUM_SUBJECTS = 2  
NUM_SUBJECTS_IMGS = 20  
img = sensor.snapshot()
#img = image.Image("singtown/%s/1.pgm"%(SUB))
d0 = img.find_lbp((0, 0, img.width(), img.height()))
img = None
pmin = 999999
num=0
def min(pmin, a, s):
    global num
    if a<pmin:
        pmin=a
        num=s
    return pmin

for s in range(1, NUM_SUBJECTS+1):
    dist = 0
    for i in range(1, NUM_SUBJECTS_IMGS+1):
        img = image.Image("face/s%s/%s.pgm"%(s, i))
        d1 = img.find_lbp((0, 0, img.width(), img.height()))
        dist += image.match_descriptor(d0, d1)
    print("Average dist for subject %d: %d"%(s, dist/NUM_SUBJECTS_IMGS))
    pmin = min(pmin, dist/NUM_SUBJECTS_IMGS, s)
    print(pmin)
if(num==1):
    SBUF=""
    output_str=json.dumps("open")
    uart.write(output_str)
else:
    SBUF=""
    output_str=json.dumps("close") 
    uart.write(output_str)
print(num)
