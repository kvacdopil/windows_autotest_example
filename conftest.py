# import pytest
# from pywinauto import Application
# from connector import app
# from auth import setting_config
# from src.general_settings import SettingsHelpers
# from src.drop_zone import DropZoneHelpers
# from src.main_menu_list import MainMenuHelpers
# from src.alert_control import AlertHelpers
# from src.notification_control import NotificationHelpers
# from src.Services.ftp_base import FTPHelpers
# from src.Services.ftps_base import FTPSHelpers
# from src.Services.sftp_base import SFTPHelpers
# from src.Services.webdav_base import WebDavHelpers
# from src.Services.amazon_base import AmazonHelpers
# from src.Services.digital_ocean_base import DigitalOceanHelpers
# from src.Services.s3_compatible_base import S3CompatibleHelpers
# from src.Services.box_base import BoxHelpers, ChromeUtilityBox
# from src.Services.dropbox_base import DropboxHelpers, ChromeUtilityDropbox
# from src.Services.google_drive_base import GoogleDriveHelpers, ChromeUtilityGD
# from src.Services.onedrive_base import OneDriveHelpers, ChromeUtilityOneDrive
# from configuration import *

# import time


# @pytest.fixture()
# def mono():
#     setting_config()
#     yield mono
#     dropzone = DropZoneHelpers(app)
#     dropzone.drop_zone().click_input()
#     main_menu = MainMenuHelpers(app)
#     main_menu.settings_btn().click_input()
#     main_settings = SettingsHelpers(app)
#     main_settings.advanced_settings_btn().click_input()
#     main_settings.reset_btn().click_input()
#     alert = AlertHelpers(app)
#     alert.confirm_reset_settings().click_input()
#     client = Application(backend="uia").connect(path=r"Monosnap.exe")
#     client.kill()


# @pytest.fixture()
# def nothing():
#     # notify = NotificationHelpers(app)
#     # notify.get_close_btn_notify().click_input()
#     # yield
#     pass


# @pytest.fixture(scope='module')
# def open_account_screen():
#     drop_zone = DropZoneHelpers(app)
#     main_menu = MainMenuHelpers(app)
#     drop_zone.drop_zone().click_input()
#     main_menu.settings_btn().click_input()


# @pytest.fixture()
# def add_ftp(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     ftp = FTPHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_ftp().click_input()
#     ftp.host_input().set_edit_text(u'').type_keys(ftp_host)
#     ftp.port_input().set_edit_text(u'').type_keys(ftp_port)
#     ftp.login_input().set_edit_text(u'').type_keys(ftp_login)
#     ftp.password_input().set_edit_text(u'').type_keys(ftp_password)
#     ftp.path_input().set_edit_text(u'').type_keys(ftp_path)
#     ftp.web_url_input().set_edit_text(u'').type_keys(ftp_webUrl)


# @pytest.fixture(scope='module')
# def add_ftps(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     ftps = FTPSHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_ftps().click_input()
#     ftps.host_input().set_edit_text(u'').type_keys(ftps_host)
#     ftps.port_input().set_edit_text(u'').type_keys(ftps_port)
#     ftps.login_input().set_edit_text(u'').type_keys(ftps_login)
#     ftps.password_input().set_edit_text(u'').type_keys(ftps_password)
#     ftps.path_input().set_edit_text(u'').type_keys(ftps_path)
#     ftps.web_url_input().set_edit_text(u'').type_keys(ftps_webUrl)


# @pytest.fixture(scope="module")
# def add_sftp(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     sftp = SFTPHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_ftp().click_input()
#     sftp.host_input().set_edit_text(u'').type_keys(sftp_host)
#     sftp.port_input().set_edit_text(u'').type_keys(sftp_port)
#     sftp.login_input().set_edit_text(u'').type_keys(sftp_login)
#     sftp.password_input().set_edit_text(u'').type_keys(sftp_password)
#     sftp.path_input().set_edit_text(u'').type_keys(sftp_path)
#     sftp.web_url_input().set_edit_text(u'').type_keys(sftp_url)


# @pytest.fixture(scope="module")
# def add_webdav(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     webdav = WebDavHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_ftp().click_input()
#     webdav.host_input().set_edit_text(u'').type_keys(webdav_host)
#     webdav.port_input().set_edit_text(u'').type_keys(webdav_port)
#     webdav.login_input().set_edit_text(u'').type_keys(webdav_login)
#     webdav.password_input().set_edit_text(u'').type_keys(webdav_password)
#     webdav.path_input().set_edit_text(u'').type_keys(webdav_path)
#     webdav.web_url_input().set_edit_text(u'').type_keys(webdav_url)


# @pytest.fixture(scope='module')
# def add_amazon_s3(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     amazon = AmazonHelpers(app)
#     notify = NotificationHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_amazon().click_input()
#     amazon.access_key_edit().set_edit_text(u'').type_keys(amazons3_key)
#     amazon.secret_key_edit().set_edit_text(u'').type_keys(amazons3_secret_key)
#     amazon.update_bucket_btn().click_input()
#     notify.notify_window().set_focus()
#     notify.bucket_update_amazon()
#     amazon.path_edit().set_edit_text(u'').type_keys(amazons3_path)
#     amazon.web_url_edit().set_edit_text(u'').type_keys(amazons3_url)


# @pytest.fixture(scope='module')
# def add_digital_ocean(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     do = DigitalOceanHelpers(app)
#     notify = NotificationHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_digital_ocean().click_input()
#     do.access_key_id_input().set_edit_text(u'').type_keys(do_key_id)
#     do.secret_access_key().set_edit_text(u'').type_keys(do_secret_key)
#     do.update_space_btn().click_input()
#     notify.notify_window().set_focus()
#     notify.bucket_update_amazon()


# # in progress
# @pytest.fixture(scope='module')
# def add_s3(open_account_screen):
#     general_settings = SettingsHelpers(app)
#     s3 = S3CompatibleHelpers(app)
#     # notify = NotificationHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_S3().click_input()
#     s3.host_input().set_edit_text(u'').type_keys(s3_host)
#     s3.port_input().set_edit_text(u'').type_keys(s3_port)
#     s3.access_key_id_input().set_edit_text(u'').type_keys(s3_login)
#     s3.secret_access_key().set_edit_text(u'').type_keys(s3_password)
#     s3.path_input().set_edit_text(u'').type_keys(s3_path)


# @pytest.fixture(scope='module')
# def add_box(open_account_screen):
#     general_settings = SettingsHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_box_com().click_input()
#     general_settings.close_general_settings().click_input()

#     chromebox = ChromeUtilityBox()
#     chromebox.email_input().set_edit_text(u'').type_keys(box_username)
#     chromebox.password_input().set_edit_text(u'').type_keys(box_password)
#     chromebox.login_btn().click_input()
#     # sleep allows the page to load
#     time.sleep(1.5)
#     chromebox.allow_access_btn().click_input()
#     # sleep for correct focus operation
#     time.sleep(1.5)
#     chromebox.open_client().set_focus().click_input()
#     chromebox.close_tab_after_login_in_box().click_input()


# @pytest.fixture(scope='module')
# def add_bropbox(open_account_screen):
#     general_settings = SettingsHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_dropbox().click_input()
#     general_settings.close_general_settings().click_input()

#     chromebox = ChromeUtilityDropbox()
#     chromebox.login_input().set_edit_text(u'').type_keys(dropbox_username)
#     chromebox.password_input().set_edit_text(u'').type_keys(dropbox_password)
#     chromebox.sign_in_btn().click_input()
#     # sleep allows the page to load
#     time.sleep(3.5)
#     chromebox.allow_btn().click_input()
#     # sleep for correct focus operation
#     time.sleep(1.5)
#     chromebox.open_client().set_focus().click_input()
#     chromebox.close_tab_after_login().click_input()


# @pytest.fixture(scope='module')
# def add_google_drive(open_account_screen):
#     """
#     Single access type
#     """
#     general_settings = SettingsHelpers(app)
#     google_drive = GoogleDriveHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_google_drive().click_input()
#     google_drive.select_btn().click_input()
#     general_settings.close_general_settings().click_input()

#     chrome = ChromeUtilityGD()
#     chrome.select_testing_acc().click_input()
#     # sleep allows the page to load
#     time.sleep(1.5)
#     chrome.continue_btn_on_2th_screen().click_input()
#     chrome.close_tab_after_login_in_gd().click_input()


# @pytest.fixture(scope='module')
# def add_one_drive(open_account_screen):
#     general_settings = SettingsHelpers(app)

#     general_settings.account_btn_in_settings().click_input()
#     general_settings.add_service_btn().click_input()
#     general_settings.select_onedrive().click_input()
#     general_settings.close_general_settings().click_input()

#     chrome = ChromeUtilityOneDrive()
#     chrome.login_input().set_edit_text(u'').type_keys(onedrive_username)
#     chrome.btn_next().click_input()
#     # sleep allows the page to load
#     time.sleep(1.5)
#     chrome.close_tab_after_login_btn().click_input()

# # @
# # #
# # @pytest.fixture()
# # def launch_mononsnap():
# #     start = time.time()
# #     app = application.Application()
# #
# #     # for distribution we don't want to connect to anybodies application
# #     # because we may mess up something they are working on!
# #     try:
# #         app.connect(path=r"Monosnap.exe")
# #     except application.ProcessNotFoundError:
# #         app.start(r"C:\Users\Kvacd\AppData\Local\Monosnap\App\monosnap.exe")
# #         app.connect(path=r"Monosnap.exe")
# #         time.sleep(5)
# #
# #     drop_zone_list = app.window(best_match="Dialog")
# #     drop_zone_list.click()
# #     # drop_zone = app.window(auto_id="DropZoneControl")
# #     # drop_zone.click



# # @pytest.fixture()
# # def connect_app():
# #     app = application.Application().connect(path=r"Monosnap.exe")
# #     try:
# #        app.connect(path=r"Monosnap.exe")
# #     except application.ProcessNotFoundError:
# #        app.start(r"C:\Users\Kvacd\AppData\Local\Monosnap\App\monosnap.exe")
# #
# #     yield connect_app
# #     connect_app.application.Application(backend="uia").kill(path=r"Monosnap.exe")

#        # r"C:\Users\Kvacd\AppData\Local\Monosnap\App\monosnap.exe")


#     # yield connect_app
#     # connect_app.application.Application(backend="uia").connect(path=r"Monosnap.exe").kill()
