from src.drop_zone import DropZoneHelpers
import pywinauto


class SettingsHelpers:
    def __init__(self, app):
        self.app = app
        self.ms_main_settings = app.window(title="Monosnap Settings")

    def drop_zone(self):
        drop_zone_icon = self.app.window(best_match="Dialog")
        return drop_zone_icon

    def settings_btn(self):
        settings_btn = self.app.child_window(best_match="Settings...")
        return settings_btn

    def close_general_settings(self):
        return self.ms_main_settings.child_window(
            best_match="SettingsButton"
        )

    '''
    Advanced settings in window Settings client
    '''
    def reset_settings(self):
        return self.ms_main_settings.child_window(
            best_match="AdvancedCustom")

    # advanced settings btn in ms settings
    def advanced_settings_btn(self):
        advanced_settings_btn = self.ms_main_settings.child_window(
            title="Advanced", auto_id="Advanced", control_type="RadioButton")
        return advanced_settings_btn

    def reset_btn(self):
        reset_settings_btn = self.ms_main_settings.child_window(
            title="Reset settings", control_type="Button")
        return reset_settings_btn

    '''
    Interface screen and btn in list menu
    '''
    def select_interface_in_list_menu(self):
        """btn Interface in list menu General settings"""
        return self.ms_main_settings.child_window(
            title="Interface", auto_id="Interface", control_type="RadioButton"
        )

    def add_context_menu_checkbox(self):
        return self.ms_main_settings.child_window(
            title="Add to context menu", control_type="CheckBox"
        )

    '''
    feedback screen
    '''

    def email_input_field(self):
        return self.ms_main_settings.child_window(
            best_match="Edit1")

    def text_input_field(self):
        return self.ms_main_settings.child_window(
            best_match="FeedbackEdit2"
        )

    def attach_checkbox(self):
        return self.ms_main_settings.child_window(
            title="Attach logs", control_type="CheckBox"
        )

    def send_feedback_btn(self):
        return self.ms_main_settings.child_window(
            title="Send", control_type="Button"
        )

    def suggest_link(self):
        return self.ms_main_settings.child_window(
            title="Suggest feature", control_type="Hyperlink"
        )

    def how_report_bug_link(self):
        return self.ms_main_settings.child_window(
            title="How to report a bug?", control_type="Text"
        )

    '''
    account screen
    '''
    def account_btn_in_settings(self):
        account_btn_in_list = self.ms_main_settings.child_window(
            title="Accounts", control_type="Text")
        return account_btn_in_list

    def add_service_btn(self):
        add_service_btn = self.app.window(
            title="Monosnap Settings"
        ).child_window(
            best_match="Custom7"
        ).child_window(
            title="Add Service", control_type="Button")
        return add_service_btn

    '''
    screen with list service
    '''
    def select_amazon(self):
        amazon = self.ms_main_settings.child_window(
            title="Amazon S3")
        return amazon

    def select_digital_ocean(self):
        digital_ocean = self.ms_main_settings.child_window(
            title="DigitalOcean Spaces")
        return digital_ocean

    def select_box_com(self):
        box = self.ms_main_settings.child_window(
            title="Box.com")
        return box

    def select_dropbox(self):
        dropbox = self.ms_main_settings.child_window(
            title="Dropbox")
        return dropbox

    def select_ftp(self):
        ftp = self.ms_main_settings.child_window(
            title="FTP")
        return ftp

    def select_ftps(self):
        ftps = self.ms_main_settings.child_window(
            title="FTPS")
        return ftps

    def select_google_drive(self):
        win_rect = self.ms_main_settings.rectangle()
        coordinates = (int(win_rect.right / 2 + win_rect.left / 2)), (int(win_rect.bottom / 2 + win_rect.top / 2))
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        google_drive = self.ms_main_settings.child_window(
            title="Google Drive")
        return google_drive

    def select_S3(self):
        win_rect = self.ms_main_settings.rectangle()
        coordinates = (int(win_rect.right / 2 + win_rect.left / 2)), (int(win_rect.bottom / 2 + win_rect.top / 2))
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        S3 = self.ms_main_settings.child_window(
            title="S3 Compatible")
        return S3

    def select_sftp(self):
        win_rect = self.ms_main_settings.rectangle()
        coordinates = (int(win_rect.right / 2 + win_rect.left / 2)), (int(win_rect.bottom / 2 + win_rect.top / 2))
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        SFTP = self.ms_main_settings.child_window(
            title="sFTP")
        return SFTP

    def select_webdav(self):
        win_rect = self.ms_main_settings.rectangle()
        coordinates = (int(win_rect.right / 2 + win_rect.left / 2)), (int(win_rect.bottom / 2 + win_rect.top / 2))
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        WebDAV = self.ms_main_settings.child_window(
            title="WebDAV")
        return WebDAV

    def select_youtube(self):
        win_rect = self.ms_main_settings.rectangle()
        coordinates = (int(win_rect.right / 2 + win_rect.left / 2)), (int(win_rect.bottom / 2 + win_rect.top / 2))
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        YouTube = self.ms_main_settings.child_window(
            title="YouTube")
        return YouTube

    def select_onedrive(self):
        win_rect = self.ms_main_settings.rectangle()
        coordinates = (int(win_rect.right / 2 + win_rect.left / 2)), (int(win_rect.bottom / 2 + win_rect.top / 2))
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        pywinauto.mouse.scroll(coords=coordinates, wheel_dist=-1)
        OneDrive = self.ms_main_settings.child_window(
            title="OneDrive")
        return OneDrive
