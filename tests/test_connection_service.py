import pytest
from connector import app
from src.notification_control import NotificationHelpers
from src.Services.ftp_base import FTPHelpers
from src.Services.ftps_base import FTPSHelpers
from src.Services.sftp_base import SFTPHelpers
from src.Services.webdav_base import WebDavHelpers
from src.locators import TextNotification


def test_ftp_connection_success(add_ftp):
    """Success connection FTP service in client
    """
    notifications = NotificationHelpers(app)
    ftp = FTPHelpers(app)
    ftp.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_SUCCESS).element_info.name
    assert TextNotification.CONNECT_SUCCESS == success_connection, "Error test connection in FTP"
    notifications.get_close_btn_notify().click_input()


def test_ftp_connection_fail(add_ftp):
    """Fail connection FTP service in client
    """
    notifications = NotificationHelpers(app)
    ftp = FTPHelpers(app)
    ftp.login_input().set_edit_text(u'').type_keys("test")
    ftp.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_FAIL).element_info.name
    assert TextNotification.CONNECT_FAIL == success_connection, "Error test connection in FTP"
    notifications.get_close_btn_notify().click_input()


def test_ftps_connection_success(add_ftps):
    """Success connection FTPS service in client
    """
    notifications = NotificationHelpers(app)
    ftps = FTPSHelpers(app)
    ftps.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_SUCCESS).element_info.name
    assert TextNotification.CONNECT_SUCCESS == success_connection, "Error test connection in FTPS"
    notifications.get_close_btn_notify().click_input()


def test_ftps_connection_fail(add_ftps):
    """Fail connection FTPS service in client
    """
    notifications = NotificationHelpers(app)
    ftps = FTPSHelpers(app)
    ftps.login_input().set_edit_text(u'').type_keys("test")
    ftps.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_FAIL).element_info.name
    assert TextNotification.CONNECT_FAIL == success_connection, "Error test connection in FTPS"
    notifications.get_close_btn_notify().click_input()


def test_sftp_connection_success(add_sftp):
    """Success connection SFTP service in client
    """
    notifications = NotificationHelpers(app)
    sftp = SFTPHelpers(app)
    sftp.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_SUCCESS).element_info.name
    assert TextNotification.CONNECT_SUCCESS == success_connection, "Error test connection in SFTP"
    notifications.get_close_btn_notify().click_input()


def test_sftp_connection_fail(add_sftp):
    """Fail connection SFTP service in client
    """
    notifications = NotificationHelpers(app)
    sftp = SFTPHelpers(app)
    sftp.login_input().set_edit_text(u'').type_keys("test")
    sftp.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_FAIL).element_info.name
    assert TextNotification.CONNECT_FAIL == success_connection, "Error test connection in SFTP"
    notifications.get_close_btn_notify().click_input()


def test_webdav_connection_success(add_webdav):
    """Success connection WebDav service in client
    """
    notifications = NotificationHelpers(app)
    webdav = WebDavHelpers(app)
    webdav.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_SUCCESS).element_info.name
    assert TextNotification.CONNECT_SUCCESS == success_connection, "Error test connection in WebDav"
    notifications.get_close_btn_notify().click_input()


def test_webdav_connection_fail(add_webdav):
    """Fail connection WebDav service in client
    """
    notifications = NotificationHelpers(app)
    webdav = WebDavHelpers(app)
    webdav.login_input().set_edit_text(u'').type_keys("test")
    webdav.test_connection_btn().click_input()
    success_connection = notifications.get_text_in_notify_window(
        title=TextNotification.CONNECT_FAIL).element_info.name
    assert TextNotification.CONNECT_FAIL == success_connection, "Error test connection in WebDav"
    notifications.get_close_btn_notify().click_input()
