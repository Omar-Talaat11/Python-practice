import psutil



from plyer import notification
import time

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Python Notification Example',
        timeout=10  # Notification will disappear after 10 seconds
    )

battery_status = round(psutil.sensors_battery().percent,2)
title = "Battery Health"
message = f"Battery is {battery_status}%"
send_notification(title, message)

