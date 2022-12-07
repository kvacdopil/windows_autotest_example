from pywinauto import Application, Desktop
from settings import get_file_name, test_folder
from dropzone.open_dropzone import drop_zone_list, upload_file_btn
from notify_ms.notify import notify_file
from dropzone.open_dropzone import Open_Settings
from ms_main_settings.interface.interface_main_settings import interface_btn, add_context
from notify_ms.pop_up_payments import alert_payments
import time

# connect to apps
app = Application(backend="uia").connect(path=r"Monosnap.exe")
ms_main_settings = app.window(title="Monosnap Settings")


class ContextMenu:
    def __init__(self):
        self.array_with_file_context = get_file_name()[0]
        self.path_folder = test_folder
        self.dsk = Desktop(backend="uia")

    def add_context_menu(self):
        Open_Settings()
        interface_btn.click_input()
        # если чекбокс меньше или равен 0 (выключен), то включаем его
        if add_context.get_toggle_state() == 0:
            add_context.toggle()
            ms_main_settings.close()
        else:
            ms_main_settings.close()

    def upload_context_menu(self, upload_service):
        drop_zone_list.set_focus().click_input()
        upload_file_btn.click_input()
        explorer_upload_file_search_test_folder.click_input()
        input_test_folder.type_keys(self.path_folder, with_spaces=True).type_keys("{ENTER}")
        # цикл для загрузки файлов с закрытием нотифы
        for i in self.array_with_file_context:
            file = file_list.get_item(i)
            time.sleep(1) # sleep из-за скорости работы нотификации
            file.set_focus().click_input(button="right")
            self.dsk.Context.child_window(
                title=upload_service, control_type="MenuItem"
            ).click_input()
            notify_file()
            alert_payments()
        close_explorer_upload()


context_menu = ContextMenu()


def close_explorer_upload():
    app.window(title="Upload file", control_type="Window"
               ).close()


explorer_upload_file_search_test_folder = app.window(
    title="Upload file", control_type="Window"
).child_window(
    auto_id="40965", control_type="Pane"
).child_window(
    auto_id="41477", control_type="Pane"
).child_window(
    best_match="Progress"
).child_window(
    best_match="Pane"
).child_window(
    auto_id="1001", control_type="ToolBar"
).child_window(
    title="All locations", control_type="SplitButton"
)
# .click_input()

# определяет поле для ввода и вводит путь до папки с тестовыми файлами
input_test_folder = app.window(
    title="Upload file", control_type="Window"
).child_window(
    auto_id="40965", control_type="Pane"
).child_window(
    auto_id="41477", control_type="Pane"
).child_window(
    best_match="Progress"
).child_window(
    auto_id="41477", control_type="ComboBox"
).child_window(
    auto_id="41477", control_type="Edit"
)
# .type_keys(goto, with_spaces=True)

# окно со списком файлов
file_list = app.window(
    title="Upload file", control_type="Window"
).child_window(
    best_match="Pane"
).child_window(
    title="Shell Folder View", auto_id="listview", control_type="Pane"
).child_window(
    title="Items View", control_type="List"
)

