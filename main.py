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

# Классы для окон
class MainWindow(Screen):
    pass

class SecondWindow(Screen):
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
