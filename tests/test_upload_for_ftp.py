import pytest
from pywinauto import mouse
from connector import app
from src.notification_control import NotificationHelpers
from src.drop_zone import DropZoneHelpers
from src.main_menu_list import MainMenuHelpers
from src.uploading import UploadFileHelpers
from src.locators import NameServiceContext
from src.editor_base import EditorHelpers
from src.locators import NameServiceBurgerMenu, TextNotification, NameFolderInDropzoneFolderList
from src.general_settings import SettingsHelpers
from src.Services.ftp_base import FTPHelpers
from configuration import *
import subprocess
import time


@pytest.mark.parametrize('name_file',
                         [file_name_jpg, file_name_png, file_name_gif, file_name_mp4,
                          file_name_txt, file_name_zip
                          ])
class TestUploadForFtp:

    @pytest.fixture()
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

    @pytest.mark(usefixture='add_ftp')
    def test_upload_main_menu_ftp(self, name_file):
        """Upload jpg/png/gif/mp4/txt/zip file in FTP, from main menu
        :param make_default_ftp:
        :return:
        """
        drop = DropZoneHelpers(app)
        main_menu = MainMenuHelpers(app)
        upload = UploadFileHelpers(app)
        notify = NotificationHelpers(app)

        drop.drop_zone().click_input()
        main_menu.upload_btn().click_input()
        upload.path_for_test_folder().click_input()
        upload.input_path_to_folder(path_folder=test_folder)
        upload.input_name_file(name_file)
        upload.open_btn().click_input()
        success_upload = notify.get_text_in_notify_window(
            title=TextNotification.UPLOAD).element_info.name
        notify.notify_window().set_focus()
        notify.get_close_btn_notify().click_input()
        assert TextNotification.UPLOAD == success_upload, f'Error uploading {name_file} file in FTP'

    def test_upload_context_menu_ftp(self, name_file):
        """Upload jpg/png/gif/mp4/txt/zip file in FTP, from context menu
        :param:
        :return:
        """
        drop = DropZoneHelpers(app)
        main_menu = MainMenuHelpers(app)
        upload = UploadFileHelpers(app)
        notify = NotificationHelpers(app)

        drop.drop_zone().set_focus().click_input()
        main_menu.upload_btn().click_input()
        upload.path_for_test_folder().click_input()
        upload.input_path_to_folder(path_folder=test_folder)
        # work context
        upload.file_list(file=name_file).select().click_input(button="right")
        upload.upload_service(name_service=NameServiceContext.FTP).click_input()

        success_upload = notify.get_text_in_notify_window(
            title=TextNotification.UPLOAD).element_info.name
        notify.notify_window().set_focus()
        notify.get_close_btn_notify().click_input()
        assert TextNotification.UPLOAD == success_upload, f'Error uploading {name_file} file in FTP from context menu'
        upload.close_explorer_upload()


# @pytest.mark.parametrize('name_file',
#                          [file_name_jpg, file_name_png
#                           ])
# def test_upload_from_editor_after_open_burger_menu_ftp(name_file):
#     '''
#     1. Открывает файл jpg/png
#     2. Загружает через burger menu
#     :param name_file:
#     :return:
#     '''
#     drop = DropZoneHelpers(app)
#     main_menu = MainMenuHelpers(app)
#     upload = UploadFileHelpers(app)
#     notify = NotificationHelpers(app)
#     editor = EditorHelpers(app)

#     drop.drop_zone().set_focus().click_input()
#     main_menu.open_image_btn().click_input()

#     upload.path_folder_in_open_window().click_input()
#     upload.open_file_input_path(path_folder=test_folder)
#     upload.select_file_in_open_window(file=name_file).select()
#     upload.btn_open_in_open_window().click_input()
#     time.sleep(0.5)
#     editor.open_burger_menu().click_input()
#     editor.service_in_list_burger_menu(name_service=NameServiceBurgerMenu.FTP).click_input()
#     success_upload = notify.get_text_in_notify_window(
#         title=TextNotification.UPLOAD).element_info.name
#     notify.notify_window().set_focus()
#     notify.get_close_btn_notify().click_input()
#     assert TextNotification.UPLOAD == success_upload, f'Error uploading {name_file} file in FTP from editor, burger menu'


# @pytest.mark.parametrize('name_file',
#                          [file_name_jpg, file_name_png
#                           ])
# def test_upload_from_editor_after_open_ftp(name_file):
#     '''
#     1. Открывает файл jpg/png
#     2. Загружает сразу через кнопку Upload
#     :param name_file:
#     :return:
#     '''
#     drop = DropZoneHelpers(app)
#     main_menu = MainMenuHelpers(app)
#     upload = UploadFileHelpers(app)
#     notify = NotificationHelpers(app)
#     editor = EditorHelpers(app)

#     drop.drop_zone().set_focus().click_input()
#     main_menu.open_image_btn().click_input()

#     upload.path_folder_in_open_window().click_input()
#     upload.open_file_input_path(path_folder=test_folder)
#     upload.select_file_in_open_window(file=name_file).select()
#     upload.btn_open_in_open_window().click_input()
#     time.sleep(0.5)
#     editor.btn_upload().click_inpput()
#     success_upload = notify.get_text_in_notify_window(
#         title=TextNotification.UPLOAD).element_info.name
#     notify.notify_window().set_focus()
#     notify.get_close_btn_notify().click_input()
#     assert TextNotification.UPLOAD == success_upload, f'Error uploading {name_file} file in FTP from editor'


# @pytest.mark.parametrize('name_file',
#                          [file_name_jpg, file_name_png,
#                           file_name_gif, file_name_mp4,
#                           file_name_txt, file_name_zip
#                           ])
# def test_upload_drag_drop_ftp(name_file):
#     """
#     1. Открывает папку с тестовыми файлами
#     2. Перетаскивает файл с помощью drag&drop на Dropzone Monosnap
#     :param name_file:
#     :return:
#     """
#     drop = DropZoneHelpers(app)
#     upload = UploadFileHelpers(app)
#     notify = NotificationHelpers(app)

#     subprocess.Popen(f'explorer "{test_folder}')
#     coord_dropzone = drop.drop_zone().wrapper_object()
#     coords_file = upload.open_test_img_folder(file=name_file)
#     mouse.press(coords=coords_file.rectangle().mid_point())
#     mouse.move(coords=coord_dropzone.rectangle().mid_point())
#     mouse.release(coords=coord_dropzone.rectangle().mid_point())

#     drop.folder_in_list_folder_drop_zone(
#         name_folder_in_list=NameFolderInDropzoneFolderList.UNSORTED
#     ).click_input()

#     success_upload = notify.get_text_in_notify_window(
#         title=TextNotification.UPLOAD).element_info.name
#     notify.get_close_btn_notify().click_input()
#     assert TextNotification.UPLOAD == success_upload, f'Error uploading {name_file} file in FTP from editor'
