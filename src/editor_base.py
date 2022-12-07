'''Редактор без читаемых локаторов
'''

class EditorHelpers:
    def __init__(self, app):
        self.app = app
        self.editor_window = app.window(class_name="EditorMain")
        self.burger_list = app.window(title="Burger Menu Upload", control_type="Window")

    def open_burger_menu(self):
        return self.editor_window.child_window(
            best_match="Pane32"
        )

    def service_in_list_burger_menu(self, name_service=None):
        return self.burger_list.child_window(
            title=name_service, control_type="Text"
        )

    def username_storage_in_list(self):
        return self.burger_list.child_window(
            best_match="TreeItem1"
        )

    def folder_name_in_monosnap_storage(self, name_folder_storage):
        return self.burger_list.child_window(
            title=name_folder_storage, control_type="Text"
        )

    def btn_save(self):
        return self.editor_window.child_window(
            best_match="Pane31"
        )

    def btn_upload(self):
        return self.editor_window.child_window(
            best_match="Pane31"
        )

    # Pane7
    def input_edit_name_file(self):
        return self.editor_window.child_window(
            best_match="Edit"
        )

    # Pane11
    def btn_icon_monosnap(self):
        return self.editor_window.child_window(
            best_match="Pane12"
        )

    def btn_settings_image(self):
        return self.editor_window.child_window(
            best_match="Pane13"
        )

    # Pane33
    def minimize_btn(self):
        return self.editor_window.child_window(
            best_match="Pane14"
        )

    def maximize_btn(self):
        return self.editor_window.child_window(
            best_match="Pane15"
        )

    def btn_close_editor(self):
        return self.editor_window.child_window(
            best_match="Pane16"
        )

    # Pane27
    def btn_blur_tools(self):
        return self.editor_window.child_window(
            best_match="Pane17"
        )

    def btn_colors_tools(self):
        return self.editor_window.child_window(
            best_match="Pane18"
        )

    # Pane8
    def btn_undo_tools(self):
        return self.editor_window.child_window(
            best_match="Pane19"
        )

    # Pane9
    def btn_revert_tools(self):
        return self.editor_window.child_window(
            best_match="Pane20"
        )

    # Pane10
    def add_screenshot_tools(self):
        return self.editor_window.child_window(
            best_match="Pane21"
        )

    def btn_line_tools(self):
        return self.editor_window.child_window(
            best_match="Pane22"
        )

    def btn_ellipse_tools(self):
        return self.editor_window.child_window(
            best_match="Pane23"
        )

    def btn_brush_tools(self):
        return self.editor_window.child_window(
            best_match="Pane24"
        )

    def btn_text_tools(self):
        return self.editor_window.child_window(
            best_match="Pane25"
        )

    def btn_arrow_with_text_tools(self):
        return self.editor_window.child_window(
            best_match="Pane26"
        )

    # Pane30
    def btn_crop_tools(self):
        return self.editor_window.child_window(
            best_match="Pane28"
        )

    def btn_resize_tools(self):
        return self.editor_window.child_window(
            best_match="Pane29"
        )

    def type_link_for_google(self, type_link):
        return self.burger_list.child_window(
            title=type_link, control_type="Text"
        )
