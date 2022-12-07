from pywinauto import Application

try:
    app = Application(backend="uia").connect(path=r"Monosnap.exe")
except Exception:
    app = Application(backend="uia").start(r'C:\Users\Kvacd\AppData\Local\Monosnap\App\monosnap.exe', timeout=5)

