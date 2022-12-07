import pytest
from pywinauto import Application
from connector import app
from auth import setting_config
from src.general_settings import SettingsHelpers
from src.drop_zone import DropZoneHelpers
from src.main_menu_list import MainMenuHelpers
from src.alert_control import AlertHelpers
from src.notification_control import NotificationHelpers
from src.Services.ftp_base import FTPHelpers
from src.Services.ftps_base import FTPSHelpers
from src.Services.sftp_base import SFTPHelpers
from src.Services.webdav_base import WebDavHelpers
from src.Services.amazon_base import AmazonHelpers
from src.Services.digital_ocean_base import DigitalOceanHelpers
from src.Services.s3_compatible_base import S3CompatibleHelpers
from src.Services.box_base import BoxHelpers, ChromeUtilityBox
from src.Services.dropbox_base import DropboxHelpers, ChromeUtilityDropbox
from src.Services.google_drive_base import GoogleDriveHelpers, ChromeUtilityGD
from src.Services.onedrive_base import OneDriveHelpers, ChromeUtilityOneDrive
from configuration import *

import time


@pytest.fixture()
def setup_monosnap_client():
    setting_config()
    yield setup_monosnap_client
    dropzone = DropZoneHelpers(app)
    dropzone.drop_zone().click_input()
    main_menu = MainMenuHelpers(app)
    main_menu.settings_btn().click_input()
    main_settings = SettingsHelpers(app)
    main_settings.advanced_settings_btn().click_input()
    main_settings.reset_btn().click_input()
    alert = AlertHelpers(app)
    alert.confirm_reset_settings().click_input()
    client = Application(backend="uia").connect(path=r"Monosnap.exe")
    client.kill()


@pytest.fixture(scope='module')
def open_general_settings():
    drop_zone = DropZoneHelpers(app)
    main_menu = MainMenuHelpers(app)
    drop_zone.drop_zone().click_input()
    main_menu.settings_btn().click_input()


@pytest.fixture()
def add_ftp(open_general_settings):
    general_settings = SettingsHelpers(app)
    ftp = FTPHelpers(app)

    general_settings.account_btn_in_settings().click_input()
    general_settings.add_service_btn().click_input()
    general_settings.select_ftp().click_input()
    ftp.host_input().set_edit_text(u'').type_keys(ftp_host)
    ftp.port_input().set_edit_text(u'').type_keys(ftp_port)
    ftp.login_input().set_edit_text(u'').type_keys(ftp_login)
    ftp.password_input().set_edit_text(u'').type_keys(ftp_password)
    ftp.path_input().set_edit_text(u'').type_keys(ftp_path)
    ftp.web_url_input().set_edit_text(u'').type_keys(ftp_webUrl)


@pytest.fixture(scope="module")
def make_default_ftp(add_ftps):
    ftp = FTPHelpers(app)
    settings = SettingsHelpers(app)

    ftp.default_btn().click_input()
    settings.close_general_settings().click_input()
