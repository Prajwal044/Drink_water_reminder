import time
from plyer import notification


while True:
    # print("please sip some water!")
    notification.notify(title = "Please drink some water!", message = "you need to drink some water right now",)
    time.sleep(60*30)