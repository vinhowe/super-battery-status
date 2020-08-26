from pyfiglet import Figlet 
from time import sleep
import psutil
import atexit
from datetime import datetime

f = Figlet(font='doh')

def clean_up_term():
    print("\u001b[0J", end="")

atexit.register(clean_up_term)

try:
    while True:
        global lines_written
        percentage = f"{round(psutil.sensors_battery().percent)}%"
        display_percentage = f.renderText(percentage)
        lines_written = 1 + len(display_percentage.split('\n'))
        print("\u001b[0J", end="")
        print(display_percentage)
        print(datetime.now().strftime("%c"))
        print(f"\u001b[{lines_written}A", end="")
        sleep(1)
except KeyboardInterrupt:
    pass
