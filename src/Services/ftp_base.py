
class FTPHelpers:
    def __init__(self, app):
        self.app = app
        self.ms_main_settings = app.window(title="Monosnap Settings")
        self.advanced_main_settings = self.ms_main_settings.child_window(
            best_match="AdvancedCustom")
        self.ftp_screen = self.ms_main_settings.child_window(
            best_match="FTPCustom2")

    '''
        FTP screen
    '''

    def remove_btn(self):
        remove_btn = self.ftp_screen.child_window(
            title="Remove", control_type="Button")
        return remove_btn

    def clear_all_btn(self):
        clear_btn = self.ftp_screen.child_window(
            title="Clear All", control_type="Button")
        return clear_btn

    def host_input(self):
        host_input = self.ftp_screen.child_window(
            best_match="HostEdit")
        return host_input

    def port_input(self):
        port = self.ftp_screen.child_window(
            best_match="PortEdit")
        return port

    def login_input(self):
        login = self.ftp_screen.child_window(
            best_match="LoginEdit")
        return login

    def password_input(self):
        password = self.ftp_screen.child_window(
            best_match="PasswordEdit")
        return password

    def path_input(self):
        path = self.ftp_screen.child_window(
            best_match="PathEdit")
        return path

    def web_url_input(self):
        weburl = self.ftp_screen.child_window(
            best_match="Web URLEdit")
        return weburl

    def passive_mode_checkbox(self):
        mode = self.ftp_screen.child_window(
            title="Passive mode", control_type="CheckBox")
        return mode

    def replace_file_checkbox(self):
        replace = self.ftp_screen.child_window(
            title="Replace current files", control_type="CheckBox")
        return replace

    def test_connection_btn(self):
        btn = self.ftp_screen.child_window(
            title="Test connection", control_type="Button")
        return btn

    def default_btn(self):
        return self.ms_main_settings.child_window(
            best_match="FTPButton"
        )
