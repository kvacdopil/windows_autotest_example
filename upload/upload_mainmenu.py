from pywinauto import Application
from settings import get_file_name, test_folder
from dropzone.open_dropzone import drop_zone_list, upload_file_btn
from notify_ms.notify import notify_file
from notify_ms.pop_up_payments import alert_payments
import time

app = Application(backend="uia").connect(path=r"Monosnap.exe")


class UploadMainMenuMS:
    def __init__(self):
        self.array_with_file_main_menu = get_file_name()[1]
        self.path_folder = test_folder

    def upload_main_menu(self):
        for i in self.array_with_file_main_menu:
            time.sleep(2)
            drop_zone_list.set_focus().click_input()
            upload_file_btn.click_input()
            app.window(
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
            ).click_input()
            input_test_folder.type_keys(self.path_folder, with_spaces=True).type_keys("{ENTER}")
            time.sleep(1)
            input_file_name.type_keys(i)
            time.sleep(1)
            input_file_name.type_keys("{ENTER}")
            # select_btn.click_input()
            notify_file()
            alert_payments()


upload_main_menu_ms = UploadMainMenuMS()

# определяет окно загрузки и кликает на путь
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

# поиск поля ввода и ввод пути к папке с тестовыми файлами
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

# указываем имя файла в поиске для загрузки
input_file_name = app.window(
    title="Upload file", control_type="Window"
).child_window(
    auto_id="1148", control_type="ComboBox"
).child_window(
    auto_id="1148", control_type="Edit"
)
# .type_keys(file_name)

# кнопка "Выбрать" для загрузки
select_btn = app.window(
    title="Upload file", control_type="Window"
).child_window(
    auto_id="1", control_type="Button"
)
# .click_input()
