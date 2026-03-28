# Alert notification system

from datetime import datetime

def send_alert(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert_message = f"{timestamp} - {message}"

    # Print alert
    print(alert_message)

    # Save alert to file
    with open("alerts/alerts.log", "a") as file:
        file.write(alert_message + "\n")
