

class MainMenuHelpers:
    def __init__(self, app):
        self.app = app
        self.main_menu_screen = app.window(best_match="Dialog")

    def settings_btn(self):
        return self.main_menu_screen.child_window(
            title="Settings...", control_type="MenuItem"
        ).wait("ready", timeout=5)

    def capture_area_btn(self):
        return self.main_menu_screen.child_window(
             title="Capture area", control_type="MenuItem"
         )

    def capture_fullscreen_btn(self):
        return self.main_menu_screen.child_window(
            title="Capture fullscreen", control_type="MenuItem"
        )

    def capture_previous_area_btn(self):
        return self.main_menu_screen.child_window(
            title="Capture previous area", auto_id="CaptureLastItem", control_type="MenuItem"
        )

    def record_video_btn(self):
        return self.main_menu_screen.child_window(
             title="Record video", auto_id="RecordItem", control_type="MenuItem"
         )

    def open_image_btn(self):
        return self.main_menu_screen.child_window(
            title="Open image...", control_type="MenuItem"
        )

    def open_clipboard_btn(self):
        return self.main_menu_screen.child_window(
            title="Open from clipboard", control_type="MenuItem"
        )

    def open_latest_image_btn(self):
        return self.main_menu_screen.child_window(
            title="Open latest image", auto_id="ShowItem", control_type="MenuItem"
        )

    def upload_btn(self):
        return self.main_menu_screen.child_window(
            title="Upload...", control_type="MenuItem"
        )

    def latest_upload_list_btn(self):
        return self.main_menu_screen.child_window(
            title="Latest uploads", auto_id="UploadsItem", control_type="MenuItem"
        )

    def monosnap_storage_btn(self):
        return self.main_menu_screen.child_window(
            auto_id="UploadsItem"
        ).child_window(
            title="Monosnap storage...", control_type="MenuItem"
        )

    def upgrade_plan_btn(self):
        return self.main_menu_screen.child_window(
            title="Upgrade plan", auto_id="UpgradeItem", control_type="MenuItem"
        )

    def notification_center_btn(self):
        return self.main_menu_screen.child_window(
            title="Notifications", auto_id="NotifCenterItem", control_type="MenuItem"
        )

    def buy_license_btn(self):
        return self.main_menu_screen.child_window(
            title="Buy License", auto_id="BuyItem", control_type="MenuItem"
        )

    def hide_drop_zone_btn(self):
        return self.main_menu_screen.child_window(
            title="Hide dropzone", control_type="MenuItem"
        )

    def help_list_btn(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        )

    def take_screenshot_help(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="How to take screenshots?", control_type="MenuItem"
        )

    def how_record_video_help(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="How to record videos?", control_type="MenuItem"
        )

    def setting_overview_help(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="Settings overview", control_type="MenuItem"
        )

    def help_center_in_list_help(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="Help center", control_type="MenuItem"
        )

    def how_report_bug_in_list(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="How to report a bug?", control_type="MenuItem"
        )

    def send_feedback_btn_in_list(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="Send feedback", control_type="MenuItem"
        )

    def what_new_in_list(self):
        return self.main_menu_screen.child_window(
            title="Help", control_type="MenuItem"
        ).child_window(
            title="What’s New…", control_type="MenuItem"
        )

