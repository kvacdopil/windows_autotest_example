from connector import app
from src.notification_control import NotificationHelpers

'''
Дописать тесты. Текущая реализация только для пробы корректности работы с нотификациями при старте
'''

def test_notyfication_on_start_client(mono):
    notyfication = NotificationHelpers(app)
    text_notify = notyfication.get_notify_start_client_2()
    assert text_notify == ['Draw with Brush tool and hold Alt to highlight text']
