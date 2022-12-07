import time


class NotificationHelpers:
    def __init__(self, app):
        self.app = app

    def get_close_btn_notify(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        notify_window = self.app.window(best_match="NotificationFront")
        close_btn_notify = notify_window.child_window(
            auto_id="Control", control_type="Custom"
        ).child_window(
            best_match="MonosnapButton").wait("ready", timeout=10)
        return close_btn_notify

    def get_notify_start_client(self, title):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=10)
        notify_window = self.app.window(best_match="NotificationFront")
        try:
            text_in_notify = notify_window.child_window(
                title=title, control_type="Text")
            print("Метод: получаем текст нотификации:", text_in_notify.texts())
            return text_in_notify.texts()
        except:
            print("Метод: Ничего не нашли")
            return None

    def get_notify_start_client_2(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=10)
        notify_window = self.app.window(best_match="NotificationFront")
        try:
            text_in_notify = notify_window.child_window(
                title="Draw with Brush tool and hold Alt to highlight text", control_type="Text")
            return text_in_notify
        except:
            return None

    def get_notify_start_client_3(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=1.5)
        notify_window = self.app.window(best_match="NotificationFront")
        try:
            text_in_notify = notify_window.child_window(
                title="Select area and hold Alt to enable timer for 5 seconds", control_type="Text")
            return text_in_notify
        except:
            return None

    def upload_notify(self):
        pass

    def get_text_in_notify_window(self, title=None):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        notify_window = self.app.window(best_match="NotificationFront")
        return notify_window.child_window(
            title=title, control_type="Text"
        ).wait("ready", timeout=10)

    def test_connection_fail(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        notify_window = self.app.window(best_match="NotificationFront")
        return notify_window.child_window(
            title="Connection test failed", control_type="Text"
        ).wait("ready", timeout=10)

    def upload_file(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        notify_window = self.app.window(best_match="NotificationFront")
        return notify_window.child_window(
            title="File uploaded", control_type="Text"
        )

    """
    for set focus window notification, when we want close window
    """
    def notify_window(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        return self.app.window(best_match="NotificationFront")

    def bucket_update_amazon(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        notify_window = self.app.window(best_match="NotificationFront")
        bucket_update = notify_window.child_window(
            title="AWS S3 buckets list was updated", control_type="Text"
        )
        if bucket_update.exists():
            return notify_window.child_window(
                auto_id="Control", control_type="Custom"
            ).child_window(
                best_match="MonosnapButton").click_input()
        else:
            time.sleep(2)

    def bucket_update_digital_ocean(self):
        self.app.window(best_match="NotificationsFront").wait("ready", timeout=60)
        notify_window = self.app.window(best_match="NotificationFront")
        space_update = notify_window.child_window(
            title="DigitalOcean Spaces list was updated", control_type="Text"
        )
        if space_update.exists():
            return notify_window.child_window(
                auto_id="Control", control_type="Custom"
            ).child_window(
                best_match="MonosnapButton").click_input()
        else:
            time.sleep(2)
