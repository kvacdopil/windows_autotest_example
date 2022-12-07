from pywinauto import Application
from settings import get_file_name, test_folder
from dropzone.open_dropzone import drop_zone_list, open_image_btn
from notify_ms.notify import notify_file
from notify_ms.pop_up_payments import cancel_btn
from notify_ms.pop_up_payments import alert_payments
import time

app = Application(backend="uia").connect(path=r"Monosnap.exe")


class UploadEditor:
    def __init__(self):
        self.array_with_file_editor = get_file_name()[2]
        self.path_folder = test_folder

    def upload_editor(self):
        for i in self.array_with_file_editor:
            drop_zone_list.set_focus().click_input()
            open_image_btn.click_input()
            explorer_upload_file_search_test_folder.click_input()
            input_test_folder.type_keys(self.path_folder, with_spaces=True).type_keys("{ENTER}")
            input_file_name.type_keys(i).type_keys("{ENTER}")
            # open_btn.click_input()
            # wait работает через раз, поэтому этот костыль тут
            time.sleep(2)
            # часть редактора:
            # таймаут, пока он не появится
            # нажимаем "Загрузить"
            upload_btn.wait("visible", timeout=5)
            upload_btn.click_input()
            notify_file()
            alert_payments()
            # для стабильности цикла, так как из-за особенностей WIN алерт отрисовывается долго
            time.sleep(1)


upload_editor = UploadEditor()

# определяет окно загрузки и кликает на путь
explorer_upload_file_search_test_folder = app.window(
    title="Open", control_type="Window"
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
    title="Open", control_type="Window"
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

# вводит название файла для выбора в поиске
input_file_name= app.window(
    title="Open", control_type="Window"
).child_window(
    auto_id="1148", control_type="ComboBox"
).child_window(
    auto_id="1148", control_type="Edit"
)
# .type_keys(file_name)

# кнопка "Open" для открытия файла в редакторе
open_btn = app.window(
    title="Open", control_type="Window"
).child_window(
    auto_id="1", control_type="Button"
)
# .click_input()

# кнопка "Upload" в окне редактора
upload_btn = app.window(
    class_name='EditorMain'
).child_window(
        best_match="Pane31")


# бургерное меню (in progress for all service)
