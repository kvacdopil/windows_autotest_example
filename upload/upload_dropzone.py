from pywinauto import Application, mouse
from notify_ms import notify
from settings import get_file_name, test_folder
from notify_ms.pop_up_payments import alert_payments
from notify_ms.notify import notify_file
import subprocess

# connect to apps
app = Application(backend="uia").connect(path=r"Monosnap.exe")


class DragDropToDropZone:
    def __init__(self):
        self.array_with_file_dropzone = get_file_name()[3]
        self.app = Application(backend="uia").connect(path=r"Monosnap.exe")

    def drag_drop_ms(self):
        path_folder = f'explorer "{test_folder}"'
        subprocess.Popen(path_folder)
        # subprocess.Popen(r'explorer', self.path_folder)
        explorer = Application(backend="uia").connect(path="explorer.exe", title="Testimg")
        list_files = explorer.window(
            title="Testimg", control_type="Window"
        ).child_window(
            title="Testimg", control_type="Pane"
        ).child_window(
            best_match="6 itemsPane"
        ).child_window(
            title="Shell Folder View", auto_id="listview", control_type="Pane"
        ).child_window(
            title="Items View", control_type="List"
        )

        for i in self.array_with_file_dropzone:
            file = list_files.get_item(i)
            destination = self.app.top_window().wrapper_object()
            mouse.press(coords=file.rectangle().mid_point())
            mouse.move(coords=destination.rectangle().mid_point())
            mouse.release(coords=destination.rectangle().mid_point())

            list_ms_folders_in_drop_zone = self.app.window(best_match="FOLDERSDialog")
            list_ms_folders_in_drop_zone.child_window(
                auto_id="flist", control_type="Custom"
            ).child_window(
                best_match="FOLDERSPane"
            ).child_window(
                auto_id="foldersListBox", control_type="List"
            ).child_window(
                title="Unsorted", control_type="ListItem"
            ).click_input()
            notify_file()
            alert_payments()

    def drag_drop_service(self):
        path_folder = f'explorer "{test_folder}"'
        subprocess.Popen(path_folder)
        explorer = Application(backend="uia").connect(path="explorer.exe", title="Testimg")
        list_files = explorer.window(
            title="Testimg", control_type="Window"
        ).child_window(
            title="Testimg", control_type="Pane"
        ).child_window(
            best_match="6 itemsPane"
        ).child_window(
            title="Shell Folder View", auto_id="listview", control_type="Pane"
        ).child_window(
            title="Items View", control_type="List"
        )

        for i in self.array_with_file_dropzone:
            file = list_files.get_item(i)
            destination = self.app.top_window().wrapper_object()
            mouse.press(coords=file.rectangle().mid_point())
            mouse.move(coords=destination.rectangle().mid_point())
            mouse.release(coords=destination.rectangle().mid_point())
            notify.notify_file()


dragdrop = DragDropToDropZone()
