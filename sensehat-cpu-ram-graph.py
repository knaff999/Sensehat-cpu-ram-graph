#CPU and RAM usage graph for Raspberry Pi Sense Hat

import psutil, time
from sense_hat import SenseHat
sense = SenseHat()

#colours for graph, change at will !
red = (240, 120, 120)
blue = (0, 191, 255)
blank = (0, 0, 0)

#too bright ? set to True, need more brighty, set to False
sense.low_light = True

while True:
    #set ram and cpu values to variables - in percentage
    ram = int(psutil.virtual_memory()[2])
    cpu = int(psutil.cpu_percent())
    
    #set pixel values for cpu and ram - sense hat is 64 pixels, cpu and ram use 32 each
    # * 0.32 to get a value out of 32 
    cpu_pixels = [red if i < cpu * 0.32 else blank for i in range(32)]
    ram_pixels = [blue if i < ram * 0.32 else blank for i in range(32)]
    
    #join the list to make 64 items or sense hat no likey
    pixels = cpu_pixels + ram_pixels
    #display glorious pixels
    sense.set_pixels(pixels)
    #coz, why not
    print("CPU: ",cpu, "%")
    print("RAM: ",ram, "% used" "\n")
    #interval time
    time.sleep(1)
