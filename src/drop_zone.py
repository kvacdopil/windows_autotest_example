import pywinauto
from pywinauto import application
from pywinauto import Application


class DropZoneHelpers:
    def __init__(self, app):
        self.app = app
        self.drop_zone_list_folder = app.window(best_match="FOLDERSDialog")

    def drop_zone(self):
        drop_zone_icon = self.app.window(best_match="Dialog")
        return drop_zone_icon

    def folder_in_list_folder_drop_zone(self, name_folder_in_list):
        return self.drop_zone_list_folder.child_window(
            title=name_folder_in_list, control_type="ListItem"
        )
