from pywinauto import Desktop
from pywinauto import Application
from configuration import *


class UploadFileHelpers:
    def __init__(self, app):
        self.app = app
        self.explorer_window = app.window(title="Upload file", control_type="Window")
        self.explorer_open_window = app.window(title="Open", control_type="Window")
        self.dsk = Desktop(backend="uia")

    """Screen explorer for upload file
    """

    def path_for_test_folder(self):
        """
        нужно сделать клик на строку пути до папки
        после клика дерево элементов меняется
        """
        return self.explorer_window.child_window(
            auto_id="40965"
        ).child_window(
            auto_id="41477"
        ).child_window(
            auto_id="1001"
        )

    def input_path_to_folder(self, path_folder=None):
        """
        1. вводит путь до папки с файлами
        2. нажимает enter для перехода в папку
        """
        self.explorer_window.child_window(
            title="Address", auto_id="41477", control_type="Edit"
        ).type_keys(
            path_folder, with_spaces=True).type_keys("{ENTER}")

    def input_name_file(self, name_file=None):
        """вводим имя файла, который будем открывать/загружать"""
        self.explorer_window.child_window(
            auto_id="1148", control_type="ComboBox"
        ).child_window(
            auto_id="1148", control_type="Edit"
        ).type_keys(name_file)

    def open_btn(self):
        """кнопка Открыть"""
        return self.explorer_window.child_window(
            title="Open", auto_id="1", control_type="Button"
        )

    def file_list(self, file):
        """список файлов в окне explorer"""
        return self.explorer_window.child_window(
            best_match="Pane"
        ).child_window(
            title="Shell Folder View", auto_id="listview", control_type="Pane"
        ).child_window(
            title="Items View", control_type="List"
        ).get_item(file)

    def upload_service(self, name_service):
        """
        подставляем имя сервиса, которое
        отображается в контекстном менюя файла
        """
        return self.dsk.Context.child_window(
            title=name_service, control_type="MenuItem"
        )

    def close_explorer_upload(self):
        return self.explorer_window.close()

    '''Окно "Открыть файл", из-за разницы названия окна дублируется часть кода'''
    def path_folder_in_open_window(self):
        return self.explorer_open_window.child_window(
            auto_id="40965"
        ).child_window(
            auto_id="41477"
        ).child_window(
            auto_id="1001"
        )

    def open_file_input_path(self, path_folder=None):
        """
        1. вводит путь до папки с файлами
        2. нажимает enter для перехода в папку
        """
        self.explorer_open_window.child_window(
            title="Address", auto_id="41477", control_type="Edit"
        ).type_keys(
            path_folder, with_spaces=True).type_keys("{ENTER}")

    def select_file_in_open_window(self, file):
        """список файлов в окне explorer, когда выбрано 'Открыть файл' """
        return self.explorer_open_window.child_window(
            best_match="Pane"
        ).child_window(
            title="Shell Folder View", auto_id="listview", control_type="Pane"
        ).child_window(
            title="Items View", control_type="List"
        ).get_item(file)

    def btn_open_in_open_window(self):
        """Кнопка 'Открыть'"""
        return self.explorer_open_window.child_window(
            title="Open", auto_id="1", control_type="Button"
        )

    def open_test_img_folder(self, file):
        explorer_test_folder = Application(backend="uia").connect(path="explorer.exe", title="Testimg")
        return explorer_test_folder.window(
            title="Testimg", control_type="Window"
        ).child_window(
            title="Testimg", control_type="Pane"
        ).child_window(
            best_match="6 itemsPane"
        ).child_window(
            title="Shell Folder View", auto_id="listview", control_type="Pane"
        ).child_window(
            title="Items View", control_type="List"
        ).get_item(file)

