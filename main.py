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

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

import time

# Для размера окна
from kivy.core.window import Window

Window.size = (420, 800)


ciphers=[]
comments=[]
titleOfItems=['№','Дата изготовления','Месторасположение']
itemsOfDetails = [[1, '10.02.2021', 'Цех №1'], [3, '25.02.2021', 'Цех сбороки'], [5, '25.04.2021', 'Цех №5']]
#k=len(t)
#print(t[1][1])
for j in range(20):
    string_line = str(j+1) + '. Деталь ' + str(j+1)
    ciphers.append(string_line)
    string_line1= "### "+ str(j+1) + " ###"
    comments.append(string_line1)
listOfItems=True

# Классы для окон
class MainWindow(Screen):
    pass

class NeiroClassWindow(Screen):
    #Класс для создания фото, чтобы их потом загрузить в нейросеть для классификации и идентификации.
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
    # Класс для считывания QR, или загрузки изображения для считывания QR
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
    #Окно для просмотра номенклатуры деталей
    def __init__(self, *args, **kwargs):
        super(FourthWindow, self).__init__(*args, **kwargs)
        self.listOfItems=True
    def ScrollWindow(self):
        if (self.listOfItems==True):
            #self.ids.ScrollWindowid.add_widget(ScrollView(size_hint=[1, 1]))
            self.ids.Scrollbuttonid.text = "List of items received"
            leftGrid = GridLayout(cols=1, size_hint_y=None)
            #Убедимся, что высота такая, чтобы было что прокручивать.
            leftGrid.bind(minimum_height=leftGrid.setter('height'))

            self.toggle = [0 for _ in range(len(ciphers))]

            for index in range(len(ciphers)):
                self.toggle[index] = ToggleButton(
                    text=ciphers[index],  size_hint_y=None,
                    group='cipher', height=30,
                    )
                self.toggle[index].bind(on_press=self.changer)
                leftGrid.add_widget(self.toggle[index])

            self.ids.ScrollWindowid.add_widget(leftGrid)
            self.listOfItems = False
        else:
            # удаляет все виджеты, которые находяться в another_box
            for i in range(len(self.ids.ScrollWindowid.children)):
                self.ids.ScrollWindowid.remove_widget(self.ids.ScrollWindowid.children[-1])
            self.listOfItems = True

    def changer(self, *args):
        #Переход в конкретное описание детали
        self.manager.current = 'reportOfItem'
        #Переход окна вправо (текущее уходит влево)
        self.manager.transition.direction = "left"

class ReportsWindow(Screen):
    pass

class ReportsWindowDetail(Screen):
    def __init__(self, *args, **kwargs):
        super(ReportsWindowDetail, self).__init__(*args, **kwargs)
        self.listOfItems = True
    def windowDraw(self):
        if (self.listOfItems == True):
            self.ids.ButtonScrollWindowReportid.text = comments[0]
            leftGrid = GridLayout(cols=len(titleOfItems))
            # Убедимся, что высота такая, чтобы было что прокручивать.
            leftGrid.bind(minimum_height=leftGrid.setter('height'), minimum_width=leftGrid.setter('width'))
            self.toggle = []
            for i in range(len(itemsOfDetails)+1):
                nasted = []
                self.toggle.append(nasted)
                for j in range(len(itemsOfDetails[0])):
                    nasted.append(0)

            for index in range(len(titleOfItems)):
                self.toggle[0][index] = Label(
                    text=str(titleOfItems[index])
                )
                leftGrid.add_widget(self.toggle[0][index])

            for index in range(1,len(itemsOfDetails)+1):
                for index1 in range(len(itemsOfDetails[0])):
                    self.toggle[index][index1] = Label(
                        text=str(itemsOfDetails[index-1][index1])
                    )
                    leftGrid.add_widget(self.toggle[index][index1])

            self.ids.ScrollWindowReportid.add_widget(leftGrid)
            self.listOfItems = False
        else:
            # удаляет все виджеты, которые находяться в another_box
            for i in range(len(self.ids.ScrollWindowReportid.children)):
                self.ids.ScrollWindowReportid.remove_widget(self.ids.ScrollWindowReportid.children[-1])
            self.listOfItems = True
        #pass
    def dellwidget(self):
        # удаляет все виджеты, которые находяться в another_box
        for i in range(len(self.ids.ScrollWindowReportid.children)):
            self.ids.ScrollWindowReportid.remove_widget(self.ids.ScrollWindowReportid.children[-1])
        self.ids.ButtonScrollWindowReportid.text = 'Нажмите'
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

