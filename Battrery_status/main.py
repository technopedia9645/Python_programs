from plyer import notification
import psutil
from time import sleep
battery = psutil.sensors_battery()
while True:
   if (battery.secsleft/60) < 120 :
       notification.notify(
        title="Battery Percentage",
        message=str('You have less than an hour of battery left : '+str(battery.percent) + '%') ,
        timeout=10
        )
   sleep((60*60)/2)
