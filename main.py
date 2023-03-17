import rumps
from plyer import notification
import time


class MyNotify(rumps.App):
    def __init__(self):
        super(MyNotify, self).__init__("MyNotify")
        self.timer = rumps.Timer(self.show_notification, 10)

    def show_notification(self, sender):
        notification.notify(
            title="Mi Notificacion",
            message="Soy tu notificacion",
            app_name="My Notify",
            timeout=10,
        )


if __name__ == "__main__":
    MyNotify().run()
