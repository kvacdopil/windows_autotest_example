

class AlertHelpers:
    def __init__(self, app):
        self.app = app
        self.alert_window = app.window(best_match="AlertDialog")

    def close_alert(self):
        close_btn = self.alert_window.child_window(
            auto_id="CloseButton", control_type="Button")
        return close_btn

    def confirm_reset_settings(self):
        confirm_btn = self.alert_window.child_window(
            title="Reset all settings", control_type="Button")
        return confirm_btn

    def cancel_btn(self):
        cancel_btn = self.alert_window.child_window(
            title="Cancel", control_type="Button")
        return cancel_btn

    def get_text_in_alert(self):
        text_for_reset = self.alert_window.child_window(
            title="Are you sure you want to reset all Monosnap settings?", control_type="Text")
        return text_for_reset



