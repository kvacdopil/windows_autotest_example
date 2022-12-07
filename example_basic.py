from pywinauto import Application
import pywinauto
import time
from configuration import *


def check_settings_in_list():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    drop_zone_icon = app.window(best_match="Dialog")
    drop_zone_icon.click_input()
    drop_zone_icon.child_window(title="Upload...", control_type="MenuItem").click_input()
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

    expl = app.window(title="Upload file", control_type="Window")
    edit = expl.child_window(title="Address", auto_id="41477", control_type="Edit").type_keys(r"{path}\4.18.0.39958")
    # expl.print_control_identifiers()



def open_list_service():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    # accounts_menu = ms_main_settings.child_window(
    #     title="Accounts", auto_id="Accounts", control_type="RadioButton")
    # accounts_menu.click_input()

    accounts_menu1 = ms_main_settings.child_window(
        title="Accounts", control_type="Text")
    accounts_menu1.click_input()
    add_service_btn = app.window(
        title="Monosnap Settings"
    ).child_window(
        best_match="Custom7"
    ).child_window(
        title="Add Service", control_type="Button").click_input()
    FTP_btn = ms_main_settings.child_window(
        title="Select Service", control_type="Window"
    ).child_window(best_match="SearchPane")
    # ms_main_settings.print_control_identifiers()


def select_service_in_list():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    amazon = ms_main_settings.child_window(
        title="FTP").click_input()
    # ms_main_settings.print_control_identifiers()
    # S3 = ms_main_settings.child_window(
    #     title="S3 Compatible").click_input()


def print_control_on_screen_service():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    accounts_menu1 = ms_main_settings.child_window(
        title="Interface", auto_id="Interface", control_type="RadioButton")
    accounts_menu1.click_input()
    # ms_main_settings.child_window(best_match="Google DriveButton").click_input()
    ms_main_settings.child_window(title="Add to context menu", control_type="CheckBox").click_input()
    ms_main_settings.print_control_identifiers()

# print_control_on_screen_service()


def print_control_settings_general():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    ms_main_settings.print_control_identifiers()

print_control_settings_general()

def example_get_notify():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    app.window(best_match="NotificationsFront").wait("ready", timeout=60)
    notify_window = app.window(best_match="NotificationFront")
    bucket_update = notify_window.child_window(
        title="AWS S3 buckets list was updated", control_type="Text"
    )
    if bucket_update.exists():
        return notify_window.child_window(
            auto_id="Control", control_type="Custom"
        ).child_window(
            best_match="MonosnapButton").click_input()



def get_close_btn_notify():
    # title = 'Select area and hold Alt to enable timer for 5 seconds'
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    print(app, ":Подключились к приложению")
    app.window(best_match="NotificationsFront").wait("ready", timeout=60)

    notify_window = app.window(best_match="NotificationsFront").wait("ready", timeout=10)
    notify_window.print_control_identifiers()


def notify_connection():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    app.window(best_match="NotificationsFront").wait("ready", timeout=60)
    notify_window = app.window(best_match="NotificationFront")
    notify_window.print_control_identifiers()


# notify_connection()

    # close_btn_notify = notify_window.child_window(
    #     best_match="NotificationsFront"
    # ).child_window(
    #     best_match="MonosnapButton")
    # close_btn_notify.click_input()

    # text_in_notify = notify_window.child_window(
    #     auto_id="Control", control_type="Custom"
    # ).child_window(
    #     best_match=title
    # ).texts()
    #     # child_window(
    #     #     title="Select area and hold Alt to enable timer for 5 seconds", control_type="Text").texts()
    # print(text_in_notify)
    # notify_window.print_control_identifiers()

def upload_notify():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    app.window(best_match="NotificationsFront").wait("ready", timeout=60)
    notify_window = app.window(best_match="NotificationFront")
    notify_window.wait("ready", timeout=1)
    notify_window.print_control_identifiers()


def combobox_google_drive():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    gd = ms_main_settings.child_window(
        title="GoogleDriveAccessWindow", control_type="Window")
    combox = gd.child_window(
        best_match='ComboBoxSingle folder access').click_input()
    single_list_item = gd.child_window(
        best_match='Full accessDialog').child_window(
        title="Single folder access", control_type="ListItem").click_input()
    # gd.print_control_identifiers()


def close_access_settings():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    gd = ms_main_settings.child_window(
        title="GoogleDriveAccessWindow", control_type="Window")
    close = gd.child_window(best_match='Access settingsButton').click_input()


def select_google_drive_access_settings_ok():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    ms_main_settings = app.window(title="Monosnap Settings")
    gd = ms_main_settings.child_window(
        title="GoogleDriveAccessWindow", control_type="Window")
    close = gd.child_window(
            title="Select", control_type="Button").click_input()


def connect_google_chrome_tab():
    chrome_eng_app = Application(backend="uia")
    print('Включаем бекенд')
    chrome_eng_app.connect(class_name="Chrome_WidgetWin_1", found_index=0, timeout=10)
    print('подключаемся к хрому - коннект')
    # time.sleep(3)
    print('Ждем 3 секунды на запуск клиента')
    select_login_eng = chrome_eng_app["Pane"]
    # select_login_eng = chrome_eng_app['Chrome_WidgetWin_1']
    print('Нашли таб и переходим к принтконтролу')
    select_login_eng.print_control_identifiers()
    # checkbox = select_login_eng.child_window(
    #     title="Manage your YouTube videos. Learn more", auto_id="i9", control_type="CheckBox")
    # checkbox.click_input()


# login_email547771611044304

# connect_google_chrome_tab()



    # close_tab = select_login_eng.child_window(
    #         best_match="TabItem1"
    #     ).child_window(
    #         title="Close", control_type="Button"
    #     ).click_input()

    # btn = select_login_eng.child_window(
    #     title="Open Monosnap", control_type="Button").click_input()

    # btn = select_login_eng.child_window(
    #         best_match='Document1'
    #     ).child_window(
    #         auto_id="consent_accept_button", control_type="Button"
    #     ).click_input()
    # email = select_login_eng.child_window(best_match='Document1').child_window(title="Email Address", auto_id="login", control_type="Edit")
    # email.set_edit_text(u'').type_keys("test@monosnap.com")
    # password = select_login_eng.child_window(best_match='Document1').child_window(title="Password", auto_id="password", control_type="Edit")
    # password.set_edit_text(u'').type_keys("jRYTEiUKKLaBPEGsf7ndWcDo")
    #
    # login_btn = select_login_eng.child_window(best_match='Document1').child_window(
    #         title="Authorize", control_type="Button"
    #     ).click_input()


    # r = select_login_eng.child_window(
    #     best_match='Document1').child_window(
    #     best_match="ListBox").child_window(
    #     best_match="ListItem1")
    # # r.print_control_identifiers()
    # select = r.child_window(best_match="Test Mono monotestgd@gmail.com").click_input()
    # time.sleep(2)
    # # chrome = chrome_eng_app["Pane"].print_control_identifiers()
    # select_login_eng.child_window(title="Continue", control_type="Button").click_input()

    # time.sleep(2)
    # select_login_eng.print_control_identifiers()


def close_after_login_in_gd():
    chrome_eng_app = Application(backend="uia")
    chrome_eng_app.connect(class_name="Chrome_WidgetWin_1", found_index=0, timeout=10)
    chrome = chrome_eng_app["Pane1"]
    # chrome.child_window(
    #     title="Google Chrome", control_type="Pane").child_window(
    #     best_match="Pane4"
    # ).child_window(best_match="TabControl").print_control_identifiers()
    close = chrome.child_window(
        best_match="OAuth 2.0 Authentication Token ReceivedTabItem"
    ).child_window(
        title="Close", control_type="Button").click_input()

    #     child_window(
    #     best_match="Pane5"
    # ).child_window(
    #     title="Close", control_type="Button"
    # ).click_input()


def upload_main_menu():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    drop_zone_icon = app.window(best_match="Dialog")
    drop_zone_icon.click_input()
    drop_zone_icon.child_window(best_match="Upload...").click_input()

from pywinauto import mouse

def explorer_work():
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    explorer_window = app.window(title="Open", control_type="Window")
    print(explorer_window)
    # explorer_window.print_control_identifiers()
    win = explorer_window.child_window(auto_id="40965", control_type="Pane")
    path_box = explorer_window.child_window(
        auto_id="1001", control_type="ToolBar"
    )
    path_box.click_input()
    explorer_window.child_window(
        title="Address", auto_id="41477", control_type="Edit"
    ).type_keys(
        test_folder, with_spaces=True).type_keys("{ENTER}")
    file = explorer_window.child_window(
        best_match="Pane"
    ).child_window(
        title="Shell Folder View", auto_id="listview", control_type="Pane"
    ).child_window(
        title="Items View", control_type="List"
    ).get_item("1.jpg")
    print(file)
    a = mouse.press(coords=file.rectangle().mid_point())
    print(a)

def drop_zone_list_folder():
    time.sleep(4)
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    list_ms_folders_in_drop_zone = app.window(best_match="FOLDERSDialog")
    print(list_ms_folders_in_drop_zone.element_info.name)
    #
    #
    # upload.path_folder_in_open_window().click_input()
    # upload.open_file_input_path(path_folder=test_folder)
    # sfile = upload.select_file_in_open_window(file=name_file)
    #
    # # mouse.press(coords=sfile.rectangle().mid_point())
    # coords_drop_zone = drop.drop_zone().wrapper_object()
    # a = mouse.press(coords=coords_drop_zone.rectangle().mid_point())
    # print(a)
    # mouse.move(coords=coords_drop_zone.rectangle().mid_point())
    # time.sleep(3)
    # mouse.release(coords=coords_drop_zone.rectangle().mid_point())

    # coord_file = upload.file_for_dragdrop().mouse.press(coords=sfile.rectangle().mid_point())
    # mouse.move(coords=drop.drop_zone().rectangle().mid_point())
    # mouse.release(coords=drop.drop_zone().rectangle().mid_point())



def work_with_editor():
    time.sleep(2)
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
    editor = app.window(class_name="EditorMain")
    # editor.print_control_identifiers()
    editor.child_window(best_match="Pane32").click_input()
    list_burger = app.window(
        title="Burger Menu Upload", control_type="Window")
    list_burger.child_window(best_match="TreeItem1").click_input()
    list_burger.print_control_identifiers()



    # path_box.print_control_identifiers()
    #     auto_id="40965", control_type="Pane"
    # ).child_window(
    #     auto_id="41477", control_type="Pane"
    # ).child_window(
    #     best_match="Progress"
    # ).child_window(
    #     best_match="Pane"
    # ).child_window(
    #     auto_id="1001", control_type="ToolBar"
    # ).click_input()



# def get_hint():
#     app = Application(backend="uia").connect(path=r"Monosnap.exe")
#     ms_main_settings = app.window(title="Monosnap Settings")
#     hotkey = ms_main_settings.child_window(title="Hotkeys", auto_id="Hotkeys", control_type="RadioButton").click_input()
#     ms_main_settings.print_control_identifiers()


# print_control_on_screen_service()

# get_hint()
# open_list_service()
# select_service_in_list()
# select_google_drive_access_settings_ok()


# connect_google_chrome_tab()
# close_after_login_in_gd()

# close_access_settings()
# combobox_google_drive()
# h()

# from pywinauto import Application
# import subprocess
# from pywinauto import Application, mouse
# from settings import test_folder
# import time
# import pywinauto
# from pywinauto import Application
# # from settings import get_google_drive
# # from dropzone.open_dropzone import Open_Settings
# import time
# from pywinauto import Desktop
#
# def test_bla():
#     print("1. старт приложения")
#     app = Application(backend="uia").start(r'C:\Users\Kvacd\AppData\Local\Monosnap\App\Monosnap.exe', timeout=10)
#
#     print("2. приложение запущено")
#     print("3. ждем нотифу")
#     app.window(best_match="NotificationsFront").wait("ready", timeout=15)
#     notify_start = app.window(best_match="NotificationFront")
#     notify_start.print_control_identifiers()
#     a = notify_start.child_window(
#         title="Navigate to Settings > Hotkeys and set up hotkey for capture frozen area and other features",
#         control_type="Text").texts()
#     print(a)
#
# from src.drop_zone import DropZoneHelpers
# from src.main_menu_list import MainMenuHelpers
# from connector import app
#
#
# def test_reset(mono):
#     dropzone = DropZoneHelpers(app)
#     dropzone.drop_zone().click_input()
#     main_menu = MainMenuHelpers(app)
#     main_menu.settings_btn().click_input()



    # srt_a = "".join(a)
    # print(srt_a)
    # assert srt_a == "Navigate to Settings > Hotkeys and set up hotkey for capture frozen area and other features"

    # title = "Draw with Brush tool and hold Alt to highlight text", control_type = "Text"

    # notify_start.print_control_identifiers()
    # print("4. нотификация появилась")
    # text_notify = notify_start.child_window(auto_id="Control", control_type="Custom"
    #                                         ).child_window(title="Monosnap", control_type="Text")
    # print(text_notify)
    # print(text_notify)
    # print(get_notify)
    # a = get_notify.class_name
    # b = get_notify.children()

    # print("Класс нейм", a)
    # print("children", b)
    # print("5. Подключаемся к нотифам")


# def test_ghh():
#     app = Application(backend="uia").connect(path=r"Monosnap.exe")
#     get_notify = app.window(best_match="NotificationControl").wait("ready", timeout=15)
#     # time.sleep(1)
#     notify = app.window(best_match="NotificationFront")
#     notify.print_control_identifiers()
#     print("1.", notify.print_control_identifiers())
#     # a = get_notify.children()
#     # print("2.", a)


    # dlg = Desktop(backend="uia").window(title="NotificationsFront")
    # dlg.wait('visible')
    # print("6. Нотифа видимая")
    # print(dlg)
    # dlg.print_control_identifiers()
    # # b = get_notify.children()
    # print(b)

# сброс настроек, поиск всплывающего окна (in progress)
# def test_settings_window():
#     app = Application(backend="uia").connect(path=r"Monosnap.exe")
#     ms_main_settings = app.window(title="Monosnap Settings")
#     advanced_main_settings = ms_main_settings.child_window(
#         best_match="AdvancedCustom")
#     advanced_settings_btn = ms_main_settings.child_window(
#         title="Advanced", auto_id="Advanced", control_type="RadioButton").click_input()
#     reset_set_btn = advanced_main_settings.child_window(
#         title="Reset settings", control_type="Button").click_input()
#     reset_window = app.window(best_match="AlertDialog")
#     # reset_window.print_control_identifiers()
#     a = reset_window.child_window(title="Are you sure you want to reset all Monosnap settings?", control_type="Text").texts()
#     # # advanced_main_settings.print_control_identifiers()
#     print(a)


# def test_add_service():
#     app = Application(backend="uia").connect(path=r"Monosnap.exe")
#     ms_main_settings = app.window(title="Monosnap Settings")
#     # accounts_menu = ms_main_settings.child_window(
#     #     title="Accounts", auto_id="Accounts", control_type="RadioButton")
#     # accounts_menu.click_input()
#
#     accounts_menu1 = ms_main_settings.child_window(
#         title="Accounts", control_type="Text")
#     accounts_menu1.click_input()
#     add_service_btn = app.window(
#         title="Monosnap Settings"
#     ).child_window(
#         best_match="Custom7"
#     ).child_window(
#         title="Add Service", control_type="Button").click_input()
#     FTP_btn = ms_main_settings.child_window(
#         title="Select Service", control_type="Window"
#     ).child_window(best_match="SearchPane").print_control_identifiers()
    # ms_main_settings.print_control_identifiers()


    # dlg = Desktop(backend="uia").window(title="NotificationsFront")
    # dlg.wait('visible')
    # print("6. Нотифа видимая")
    # print(dlg)
    # dlg.print_control_identifiers()

    # a = new_notify.child_window(title="NotificationControl")

    # print(new_notify)
    # new_notify["Control"].print_control_identifiers()

    # -8351634331930201236 >


    # print('конец')
    # a = new_notify.window.child_window(best_match="NotificationsFront")
    # print(a)
    # window_notify = new_notify.child_window(auto_id="Control")
    # print(window_notify)
    # a = new_notify.print_control_identifiers()

# Name	NotificationsFront



#
# ms_main_settings = app.window(title="Monosnap Settings")
#
# accounts_menu = ms_main_settings.child_window(
#     title="Accounts", control_type="Text")
#
# add_service_btn = app.window(
#     title="Monosnap Settings"
# ).child_window(
#     best_match="Custom7"
# ).child_window(
#     title="Add Service", control_type="Button")
#
# box_exist = ms_main_settings.child_window(
#     title="Select Service", control_type="Window"
# ).child_window(
#     best_match="Select service:Pane"
# ).child_window(
#     best_match="RadioButton3"
# ).child_window(
#     title="Box.com", control_type="Text"
# )
#
#
# def add_box():
#     Open_Settings()
#     accounts_menu.click_input()
#     ms_main_settings.print_control_identifiers()
#
# add_box()

# def print_list():
#     path_folder = f'explorer "{test_folder}"'
#     subprocess.Popen(path_folder)
#     # subprocess.Popen(r'explorer', self.path_folder)
#     explorer = Application(backend="uia").connect(path="explorer.exe", title="Testimg")
#     list_files = explorer.window(
#         title="Testimg", control_type="Window"
#     ).print_control_identifiers()
    #     child_window(
    #     title="Testimg", control_type="Pane"
    # ).child_window(
    #     best_match="6 itemsPane"
    # ).child_window(
    #     title="Shell Folder View", auto_id="listview", control_type="Pane"
    # ).child_window(
    #     title="Items View", control_type="List"
    # )

# print_list()

# import time
#
# app_desktop = Application(backend="uia").connect(path="explorer.exe")
# app = Application(backend='uia').connect(path=r"C:\Users\Kvacd\AppData\Local\Monosnap\App\Monosnap.exe")
# drop_zone = app.window(auto_id="DropZoneControl", control_type="Window")
#
# def open_explorer_and_find_file():
#     subprocess.Popen(r'explorer "C:\Users\Kvacd\OneDrive\Desktop\Testimg\"')
#     explorer = Application(backend="uia").connect(path="explorer.exe", title="Testimg")
#     file_upload = explorer.window(title="Testimg", control_type="Window").child_window(
#         title="Testimg", control_type="Pane").child_window(
#         best_match="2 itemsPane").child_window(
#         title="Shell Folder View", auto_id="listview", control_type="Pane").child_window(
#         title="Items View", control_type="List").child_window(
#         title="1.jpg", auto_id="0", control_type="ListItem")
#     file_upload._calc_click_coords()
#     coodr_drop_zone = drop_zone._calc_click_coords()
#
#     drop_zone.drag_mouse_input(src=file_upload, dst=coodr_drop_zone, absolute=True, button="left")
#
#     list_ms_folders_in_drop_zone = app.window(best_match='Testimg')
#     list_ms_folders_in_drop_zone.wait('visible')
#
#     ms_folder_in_drop_zone_menu = list_ms_folders_in_drop_zone.child_window(
#         auto_id="flist", control_type="Custom").child_window(
#         best_match='FOLDERSPane').child_window(
#         auto_id="foldersListBox", control_type="List").child_window(
#         title="Unsorted", control_type="ListItem")
#     ms_folder_in_drop_zone_menu.click_input()

# drop_zone = app.window(auto_id="DropZoneControl", control_type="Window").get_item()

# def drop_zone():
#     drop_zone.rectangle()
#
# def grag_in_drop():


# open_explorer_and_find_file()


    # birds = first.GetItem(r'\1.jpg')
    # dogs = first.GetItem()

    #     tv_music = app_desktop.Open.TreeView.get_item("C:\\Users\\kvacd\\Desktop\\Testimg\\1.jpg")
    #     # here we drag an item between controls of the dialog
    #     tv_music.drag_mouse_input(app_desktop.Open.ListBox.wrapper_object())

        # child_window(
        # title="Testimg", control_type="Window").child_window(
        # title="Testimg", control_type="Pane").child_window(
        # best_match="2 itemsPane").child_window(
        # title="Shell Folder View", auto_id="listview", control_type="Pane").child_window(
        # title="Items View", control_type="List").child_window(
        # title="1.jpg", auto_id="0", control_type="ListItem")


    # select_file = app_desktop.window(best_match="Testimg").child_window(
    #   .child_window(
    #     title="Testimg", control_type="Pane").child_window(
    #     best_match="2 itemsPane").child_window(
    #     title="Shell Folder View", auto_id="listview", control_type="Pane").child_window(
    #     title="Items View", control_type="List").child_window(
    #     title="1.jpg", auto_id="0", control_type="ListItem")





    # Application().start('explorer.exe "C:\\Users\\kvacd\\Desktop\\Testimg"')




# Боковое меню проводника. Плохо работает, если быстрый доступ не в поле зрения
# def open_explorer_and_find_file():
    # Application().start('explorer.exe "C:\\Users\\kvacd\\Desktop\\Testimg"')
    # explorer_win = explorer.window(best_match="Documents").child_window(
    #     title="Documents", control_type="Pane").child_window(
    #     best_match="itemsPane").child_window(
    #     title="Control Host", auto_id="ProperTreeHost", control_type="Pane").child_window(
    #     title="Tree View", auto_id="100", control_type="Tree").child_window(
    #     title="Quick access", control_type="TreeItem").child_window(
    #     title="Testimg (pinned)", control_type="TreeItem")


    # explorer_documents_window = explorer(best_match='Documents')
    # explorer_window.set_focus()
    # explorer_search = explorer_window ['Edit2'] # searcheditbox
    # explorer_search.click_input()
    # explorer_search_input = explorer_window.child_window(auto_id="SearchTextBox")
    # explorer_search_input.set_text("example.JPG")
    # explorer_window.child_window(title="Host", control_type="Pane").\
    #     child_window(best_match="Pane").\
    #     child_window(title="Search", control_type="Window").\
    #     child_window(title="Execute now", auto_id="SubmitButton", control_type="Button").click_input()
    # explorer_search.wait('ready', timeout=5)
    # explorer_window.print_control_identifiers()
    # explorer_search.child_window(title="Edit").print_control_identifiers()
    # explorer_search = explorer_search_input.print_control_identifiers()
    # btn_clear.click_input()

    # # explorer_window.print_control_identifiers()

# from pywinauto import Application
#
# app = Application(backend="uia").connect(path=r"Monosnap.exe")
# ms_main_settings = app.window(title="Monosnap Settings")

# settings interface in main settings MS
# feedback_main_settings = ms_main_settings.child_window(best_match="FeedbackCustom")

# feedback btn in main settings
# feedback_btn = ms_main_settings.child_window(
#         title="Feedback", auto_id="FeedBack", control_type="RadioButton")
#
#
# def link_click():
#     nolt_link = feedback_main_settings.child_window(
#         title="your own or upvote the ones you agree with: monosnap.nolt.io", control_type="Document"
#     ).child_window(
#         title="monosnap.nolt.io", control_type="Hyperlink"
#     ).click_input()

    # link_report = feedback_main_settings.child_window(
    #     title=" ", control_type="Text"
    # ).child_window(
    #     best_match="Hyperlink3"
    # ).child_window(
    #     title="How to report bugs effectively?", control_type="Text"
    # ).click

# link_click()


# from pywinauto import Application
#
# app = Application(backend='uia').connect(path=r"C:\Users\Kvacd\AppData\Local\Monosnap\App\Monosnap.exe")
# app_notify = Application(backend="uia").connect(path="ShellExperienceHost.exe")
#
# # global connect to windows
# ms_main_settings = app.window(title='Monosnap Settings')
# drop_zone = app.window(auto_id="DropZoneControl", control_type="Window")
# main_menu = app.window(best_match='Dialog')  # диалоговое окно дропзоны
#
# ftp_exist = ms_main_settings.child_window(
#     best_match="MonosnapCustom"
# ).child_window(
#     best_match="Add ServicePane"
# ).child_window(
#     best_match="Add ServiceRadioButton"
# ).child_window(
#     title="FTP", control_type="Text"
# )




import lxml.etree
import lxml.builder

# читаем файл
# tree = lxml.etree.parse("user.config")
#
# # находим элемент setting с именем Token
# token = tree.find('.//setting[@name="Token"]/value')

# if not token:
#     print("токена в конфиге нету((")


# ладно, на самом деле нам надо проверить, есть ли там целый блок
# Monosnap.Properties.Monosnap


# читаем файл (скопировал изначальный, но убрал оттуда опции с данными юзера)
# tree = lxml.etree.parse("user.config")
#
# monosnap_props = tree.find('.//Monosnap.Properties.Monosnap')
#
# # if not monosnap_props:
# #     print('его нету, значит')
#
# # ну тогда делаем
#
#
# E = lxml.builder.ElementMaker()
#
# value = E.value
# setting = E.setting
#
# user_data = E(
#     'Monosnap.Properties.Monosnap',
#     setting(
#         value('kvacdopil'), name="UserName", serializeAs="String"
#     ),
#     setting(
#         value('blablablabla'), name="Token", serializeAs="String"
#     ),
#     setting(
#         value('test@email.ru'), name="Email", serializeAs="String"
#     ),
#     setting(
#         value('blablaID'), name="UserId", serializeAs="String"
#     ),
# )
#
# print(lxml.etree.tostring(user_data, pretty_print=True).decode())
#
# # теперь, когда мы выяснили, что вроде корректно всё генерируем,
# # надо бы запихнуть это в имеющийся xml
#
#
# user_settings = tree.find('.//userSettings')
# # вставляем внутрь на первое место (перед Properties.Settings)
# user_settings.insert(0, user_data)
#
# # проверяем
#
# print("вставляем и получаем:")
# print(lxml.etree.tostring(tree, pretty_print=True).decode())
#
# with open(r"C:\Users\Kvacd\PycharmProjects\ms_autotest_win\user.config", 'wb') as f:
#     f.write(lxml.etree.tostring(tree, pretty_print=True))

# commercial token:
# AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAoH/yIYfEpEaxLX7p9XszrAAAAAACAAAAAAAQZgAAAAEAACAAAADtUfsGZ6sqm8TOG7Tb5FT8Jmq0pPlriAXUw6X4My9LbAAAAAAOgAAAAAIAACAAAAANl+2foEunRPuI9rlh9P9qg7MYx3a89qDrOso+j378FDABAABqTP6lrYXLcv4H0N3YxEaFkW8Y7AzhLjxpH0L4AWt0VM0ztTk9LzQbrB4e+Ytu8Xvv3ZezMsRfKaPwJRre+6rvJ+r9OycaRclLiIOaYR/8ajRyLP9Xp9roz+io4d/SJSelJ6Xdxd+5kKNx6eCzck3dp+gOYsfTZfEPm98PZPpeAfc/S9oWFaIXQp4nCl6FoVLRqGJUDezZGZsY4otDXKms7/yLKDI8/ekAs96ACpBsbOxfQ3HzlMkFwgwNVQc+4op5yNrZ6UrffliJuQWZdYKP70kk7lyA93JOvCoD4ArnWizPX2fLutWgXlt9fIVFmnlVdUCG8qv8h8X7mUVtZva/6gUgH72fQNGjfncjrrFhpcbnaAPSItGsK1rHP871wkeayotrnqmhnZfgqzT7nIpPQAAAABFqBwT0pMivL2VTFU+QUNq1i0Sn9Mvcan3w7ran6niPt1yOWs7E6gZq1bxpj5wvUFoKxxAxGBWxfc8Oiz6BjG0=
#
# AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAoH/yIYfEpEaxLX7p9XszrAAAAAACAAAAAAAQZgAAAAEAACAAAABmV7rSj3vgyveDwiSrRjx9lWJA1O3hnODv2uFUbieb3gAAAAAOgAAAAAIAACAAAAD5tRmLqGDOENtKWPGJpc5xwd+Vz40tE0phET1Mw8bPYTABAADsX89g4Vox5bw3gMPx4kR0/WOgsWYkSmXhwIqJJmeDfAeFZ2OfidYASgOGeTYuSK2Y5bdj2BwHhLT+w1LN2u9p9sEY23oCdX9vQnmKteenqKLKFmJJTKz7VpMFLL1u1dIoMMgzx3CirD4ie8jPExu4naiHjBndRTqX2RIO4AoyNBwdOD1XFsspW3u/rpT1YX+CWpwgoXwwPHdzgoZQXS7idf174i2yweOWnrSfEop+Y6F2gADTbEclNylFKETCgI6jqly/O7qykjuFDpzF+zEQjjBX0vKN3Iq2wCaEosbaf27Ntl7ZFGw9LyLPQnGMJuXViW7C4EPR4nNB0Qh+P/ZjSj117x9+Sz7PKctCfmylVptz4fiiaQC1w5GIIkeP5LzHursOCL1RUkmWFOOaoEPCQAAAAJQwynD7OjUUVWq6mgjj58hLvteQdx45woKSAgSezx8MM9D5mCQeD5nrpy2UvJ71IYsQq2lNukKcHJPc4HNY7ws=





# def get_token_user():
#     username = user_free
#     password = password_free
#     payload = {
#         "mail": username,
#         "pass": password,
#         "device_info": {
#             "type": "Integration",
#             "model": "Postman_5",
#             "version": "7.18.0"
#         }
#     }
#     session = requests.Session()
#     response = session.post(f'{URL}/admin/login', json=payload)
#     token = response.json()['access_token']
#     return token
#
# print(get_token_user())


# [u'NotificationsFront', u'HwndWrapper[Monosnap.exe;;8b309cac-e102-4871-9e1c-5bf38017ccb5]', u'NotificationsFrontHwndWrapper[Monosnap.exe;;8b309cac-e102-4871-9e1c-5bf38017ccb5]']

# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element
# from auth import get_token_user
#
# token = get_token_user()
#
# xmlfile = "user.config"
#
# tree = ET.parse(xmlfile)
# root = tree.getroot()
#
# for elem in root.iter('Monosnap.Properties.Monosnap'):
#     new_str = int(elem.text) + 1
#     elem.text = str(new_str)
#     elem.set('updated', 'yes')
#
# tree.write('test_xml.xml')

# token_config = Element('userSettings')
# token_config.append((Element.fromstring('Monosnap.Properties.Monosnap')))

# ET.dump(tree)
# monosnap_settings = []
# for elem in root.findall(".//"):
#     newval = ET.SubElement(elem, "Monosnap.Properties.Monosnap")
#     newval.text = ""
#
# for elem in root.findall(".//"):
#     print(elem.tag)

# for elem in root.findall(".//setting[@name='Token']/"):
#     print(elem.text)



# from xml.etree import ElementTree
# tree = ElementTree.parse("")
# root = tree.getroot()
#
# settings = root[2]
# description = settings.find("Monosnap.Properties.Monosnap")




# search_input_login(username="test@ya.ru", password="123456")
#
# from pywinauto import Application
# from ms_main_settings.accounts.login import accounts_menu, ms_account_btn, email_edit, pass_edit, sign_in_btn, \
#     log_out_btn
# from dropzone.open_dropzone import drop_zone_list, settings_btn
# import time
# import unittest
#
# # connect to apps
# app = Application(backend="uia").connect(path=r"Monosnap.exe")
#
#
# class test_login_in_monosnap:
#     email = "kg@monosnap.com"
#     password = "RbyjGjbcr_6785377"
#
#     def login_in_ms(email, password):
#         drop_zone_list.click_input()
#         settings_btn.click_input()
#         accounts_menu.click_input()
#         ms_account_btn.click_input()
#
#         email_edit.set_edit_text(u'')
#         email_edit.type_keys(email)
#
#         pass_edit.set_edit_text(u'')
#         pass_edit.type_keys(password)
#
#         sign_in_btn.click_input()
#
#         time.sleep(10)
#
#         log_out_btn.click_input()
#
#


# # ну тогда делаем
#
#
# E = lxml.builder.ElementMaker()
#
# value = E.value
# setting = E.setting
# token = "AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAoH/yIYfEpEaxLX7p9XszrAAAAAACAAAAAAAQZgAAAAEAACAAAABmV7rSj3vgyveDwiSrRjx9lWJA1O3hnODv2uFUbieb3gAAAAAOgAAAAAIAACAAAAD5tRmLqGDOENtKWPGJpc5xwd+Vz40tE0phET1Mw8bPYTABAADsX89g4Vox5bw3gMPx4kR0/WOgsWYkSmXhwIqJJmeDfAeFZ2OfidYASgOGeTYuSK2Y5bdj2BwHhLT+w1LN2u9p9sEY23oCdX9vQnmKteenqKLKFmJJTKz7VpMFLL1u1dIoMMgzx3CirD4ie8jPExu4naiHjBndRTqX2RIO4AoyNBwdOD1XFsspW3u/rpT1YX+CWpwgoXwwPHdzgoZQXS7idf174i2yweOWnrSfEop+Y6F2gADTbEclNylFKETCgI6jqly/O7qykjuFDpzF+zEQjjBX0vKN3Iq2wCaEosbaf27Ntl7ZFGw9LyLPQnGMJuXViW7C4EPR4nNB0Qh+P/ZjSj117x9+Sz7PKctCfmylVptz4fiiaQC1w5GIIkeP5LzHursOCL1RUkmWFOOaoEPCQAAAAJQwynD7OjUUVWq6mgjj58hLvteQdx45woKSAgSezx8MM9D5mCQeD5nrpy2UvJ71IYsQq2lNukKcHJPc4HNY7ws="
#
# user_data = E(
#     'Monosnap.Properties.Monosnap',
#     # setting(
#     #     value('kvacdopil'), name="UserName", serializeAs="String"
#     # ),
#     setting(
#         value(token), name="Token", serializeAs="String"
#     ),
#     # setting(
#     #     value('test@mail.ru'), name="Email", serializeAs="String"
#     # ),
#     # setting(
#     #     value('id'), name="UserId", serializeAs="String"
#     # ),
# )
#
# print(lxml.etree.tostring(user_data, pretty_print=True).decode())
#
# # теперь, когда мы выяснили, что вроде корректно всё генерируем,
# # надо бы запихнуть это в имеющийся xml
#
#
# user_settings = tree.find('.//userSettings')
# # вставляем внутрь на первое место (перед Properties.Settings)
# user_settings.insert(0, user_data)
#
# # проверяем
#
# print("вставляем и получаем:")
# print(lxml.etree.tostring(tree, pretty_print=True).decode())
#
# with open(r"C:\Users\Kvacd\AppData\Local\Monosnap\Monosnap.exe_Url_5cxop033ggfolp0z4qv3iaxng30fde3l\4.17.2.35270\user.config", 'wb') as f:
#     f.write(lxml.etree.tostring(tree, pretty_print=True))


# def test_notifications_on_start_client_blah(nothing):
#     print("запускаем тест после фикстуры")
#     notifications = NotificationHelpers(app)
#     text_in_notify = ['Draw with Brush tool and hold Alt to highlight text'], \
#                      ['Select area and hold Alt to enable timer for 5 seconds'],\
#                      ['Navigate to Settings > Hotkeys and set up hotkey for capture frozen area and other features']
#     print("тест нотификаций получен, переходим к методу получения нотификации")
#     text_notify = notifications.get_notify_start_client(title=text_in_notify)
#     print("Получили от метода нотификации ответ")
#     print("Переходим к ассерту")
#     assert text_notify == text_in_notify
#     print("закрываем нотификацию")
#     notifications.get_close_btn_notify().click_input()
#
#
# def test_start_client(nothing):
#     dropzone = DropZoneHelpers(app)
#     settings = MainMenuHelpers(app)
#     dropzone.drop_zone().click_input()
#     btn = settings.settings_btn().element_info.visible
#     # print(btn)
#     assert btn is False
#     # print(btn.texts())
#     # assert ['Settings...'] == btn.texts()
#     # print(btn.exists())
#     # a = btn.exists()
#     # assert a is True
#
#
# def test_blah():
#     one = "Navigate to Settings > Hotkeys and set up hotkey for capture frozen area and other features"
#     two = "Draw with Brush tool and hold Alt to highlight text"
#     three = "Select area and hold Alt to enable timer for 5 seconds"

    # btn = notifications.get_close_btn_notify()
    # if a == three:
    #     btn.click_input()
    # elif b == two:
    #     btn.click_input()
    # elif c == one:
    #     btn.click_input()
    # else:
    #     print("Notification not exists")