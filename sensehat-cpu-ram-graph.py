#CPU and RAM usage graph for Raspberry Pi Sense Hat
import psutil, time
from sense_hat import SenseHat
sense = SenseHat()

red = (180, 0, 0)
yellow = (180,180,50)
green = (0, 100, 0)
blank = (0, 0, 0)

sense.low_light = True

while True:
    #set ram and cpu values to variables - in percentage
    ram = int(psutil.virtual_memory()[2])
    cpu = int(psutil.cpu_percent())
    
    #set pixel values for cpu and ram - sense hat is 64 pixels, cpu and ram use 32 each
    # * 0.32 to get a value out of 32
    if cpu < 50:
        cpu_pixels = [green if i < cpu * 0.32 else blank for i in range(32)]
    elif cpu > 80:
        cpu_pixels = [red if i < cpu * 0.32 else blank for i in range(32)]
    else:
        cpu_pixels = [yellow if i < cpu * 0.32 else blank for i in range(32)]
        
    
    if ram < 50:
        ram_pixels = [green if i < ram * 0.32 else blank for i in range(32)]
    elif ram > 80:
        ram_pixels = [red if i < ram * 0.32 else blank for i in range(32)]
    else:
        ram_pixels = [yellow if i < ram * 0.32 else blank for i in range(32)]
        
        
    #join the list to make 64 items
    pixels = cpu_pixels + ram_pixels
    #display glorious pixels
    sense.set_pixels(pixels)
    print("CPU: ",cpu, "%")
    print("RAM: ",ram, "% used" "\n")
    #interval time
    time.sleep(1)
