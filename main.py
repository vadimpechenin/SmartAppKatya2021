# -*- coding: utf-8 -*-

"""
Мобильное приложение для умного склада. Идентификация деталей, отслеживание их жизненного цикла
"""

from kivy.app import App
#Для кодировки
import os
from kivy.lang.builder import Builder

#Библиотеки для многих страниц
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
import time

# Для размера окна
from kivy.core.window import Window

Window.size = (420, 800)


# Классы для окон
class MainWindow(Screen):
    pass

class NeiroClassWindow(Screen):

    def __init__(self, *args, **kwargs):
        super(NeiroClassWindow, self).__init__(*args, **kwargs)
        self.fileName = None
        self.camera = None

    def initCamera(self):
        self.camera = self.ids.camera
        self.camera.resolution = (640, 480)
        self.camera.keep_ratio = True
        self.camera.play = False
        self.camera.allow_stretch = True

    def on_enter(self, *args):
        self.initCamera()

    def capturePhoto(self):
        imgTime = time.strftime("%Y%m%d_%H%M%S")
        self.fileName = "IMG_{}.png".format(imgTime)
        self.camera.export_to_png(self.fileName)
        print("Выполнено фотографирование")

class QRWindow(Screen):

    def __init__(self, *args, **kwargs):
        super(QRWindow, self).__init__(*args, **kwargs)
        self.fileName = None
        self.camera = None

    def initCamera(self):
        self.camera = self.ids.camera
        self.camera.resolution = (640, 480)
        self.camera.keep_ratio = True
        self.camera.play = False
        self.camera.allow_stretch = True

    def on_enter(self, *args):
        self.initCamera()

    def capturePhoto(self):
        imgTime = time.strftime("%Y%m%d_%H%M%S")
        self.fileName = "IMG_{}.png".format(imgTime)
        self.camera.export_to_png(self.fileName)
        print("Выполнено считывание QR")

class FourthWindow(Screen):
    pass

class ReportsWindow(Screen):
    pass
# Менеджер перехода между страницами и передачи данных
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("kvfiles/my.kv")

# Класс, наследующий от App
class MyMainApp(App):
    title = 'Умный склад'

    #Метод build - обеспечивает наличие на окне приложение виджета
    #Может вернуть только один виджет
    def build(self):
        #Создание лэйаута
        #описано в файле my.kv
        return kv

    #Метод для кодировки русских символов в описании
    def load_all_kv_files(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file) and kv_file.endswith("kv"):
                with open(kv_file, encoding="utf-8") as kv:
                    Builder.load_string(kv.read())

if __name__ == '__main__':
    directory_kv_files = 'kvfiles'
    MyMainApp().load_all_kv_files(directory_kv_files)
    MyMainApp().run()

