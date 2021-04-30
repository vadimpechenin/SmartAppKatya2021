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
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
#Библиотека для всплывающих окон
from kivy.uix.popup import Popup
import io
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage

import time

# Для размера окна
from kivy.core.window import Window

koef = 1 #3

if (koef == 1):
    Window.size = (420, 800)
else:
    Window.size = (1100, 2300)



ciphers=[]
comments=[]
titleOfItems=['№','Дата изготовления','Месторасположение']
itemsOfDetails = [[1, '10.02.2021', 'Цех №1'], [3, '25.02.2021', 'Цех сбороки'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [12, '25.04.2021', 'Цех №10'], [13, '25.04.2021', 'Цех №4'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5'],
                  [8, '25.05.2021', 'Цех №1'], [10, '25.04.2021', 'Цех №3'], [11, '25.04.2021', 'Цех №5']
                 ]
#k=len(t)
#print(t[1][1])
for j in range(20):
    string_line = str(j+1) + '. Деталь ' + str(j+1)
    ciphers.append(string_line)
    string_line1= "### "+ str(j+1) + " ###"
    comments.append(string_line1)
listOfItems=True

resText = ''

triggerPhoto = 1
ifTriggerPhotio = 3


# Классы для окон
class MainWindow(Screen):
    pass

class NeiroClassWindow(Screen):
    global triggerPhoto
    #Класс для создания фото, чтобы их потом загрузить в нейросеть для классификации и идентификации.
    def __init__(self, *args, **kwargs):
        super(NeiroClassWindow, self).__init__(*args, **kwargs)
        self.fileName = None
        self.camera = None
        self.popup = None
        self.popup1 = None

    #Включение всплывающего окна
    def btn(self,*args):
        # create content and add to the popup
        PopupGrid = GridLayout(cols=2, size_hint_y=None)
        content2 = Button(text='QR', halign='left', size_hint=(0.4, 0.1), pos_hint={'x': 0.1, 'top': 0.1})
        PopupGrid.add_widget(content2)
        content3 = Button(text='Изображение', halign='left', size_hint=(0.4, 0.1), pos_hint={'x': 0.1, 'top': 0.1})
        PopupGrid.add_widget(content3)

        self.popup = Popup(title='Сделайте выбор', title_align = 'center', content=PopupGrid, auto_dismiss=False, size_hint=(None, None), size=(int(300*koef), int(200*koef)))
        # bind the on_press event of the button to the dismiss function
        #
        content2.bind(on_press=self.QRPress)#self.QRPress()
        content3.bind(on_press=self.imgPress)
        # open the popup
        self.popup.open()

    def initCamera(self):
        self.camera = self.ids.camera
        self.camera.resolution = (640, 480)
        self.camera.keep_ratio = True
        self.camera.play = False
        self.camera.allow_stretch = True

    def on_enter(self, *args):
        self.initCamera()

    def capturePhoto(self):
        global triggerPhoto, ifTriggerPhotio
        imgTime = time.strftime("%Y%m%d_%H%M%S")
        self.fileName = "IMG_{}.png".format(imgTime)
        self.camera.export_to_png(self.fileName)
        print("Выполнено фотографирование")
        triggerPhoto +=1
        if (triggerPhoto<=ifTriggerPhotio):
            PopupGrid = GridLayout(cols=1, pos_hint={'center_x': 0.6, 'center_y': 0.32})
            content4 = Button(text='Закрыть', halign='center', size=(int(200 * koef), int(50 * koef)),
                              size_hint=(None, None), pos=(int(50 * koef), int(50 * koef)),
                              pos_hint=(None, None))  # size_hint=(0.1, 0.01),pos_hint={'x': 0.1, 'top': 0.5}
            PopupGrid.add_widget(content4)
            self.popup1 = Popup(title='Сделайте фото ' + str(triggerPhoto) + ' ракурса', title_align='center', content=PopupGrid,
                                auto_dismiss=False,
                                size_hint=(None, None), pos_hint={"center_x": 0.5, "top": 0.32},
                                size=(int(300 * koef), int(120 * koef)))
            content4.bind(on_press=self.popup1.dismiss)
            self.popup1.open()
        else:
            #self.popup1.dismiss()
            triggerPhoto = 1
            self.btn()

    def QRPress(self, *args):
        global ifTriggerPhotio
        print("QR")
        self.popup.dismiss()
        ifTriggerPhotio = 1
        PopupGrid = GridLayout(cols=1, pos_hint={'center_x': 0.6, 'center_y': 0.32})
        content4 = Button(text='Закрыть', halign='center', size= (int(200 * koef), int(50 * koef)),
                          size_hint=(None, None), pos = (int(50 * koef), int(50 * koef)), pos_hint=(None, None))
        PopupGrid.add_widget(content4)
        self.popup1 = Popup(title='Считайте QR', title_align='center', content =PopupGrid, auto_dismiss=False,
                            size_hint=(None, None), pos_hint={"center_x": 0.5, "top": 0.32},
                            size=(int(300 * koef), int(120 * koef)))
        content4.bind(on_press=self.popup1.dismiss)
        self.popup1.open()


    def imgPress(self, *args):
        global ifTriggerPhotio, triggerPhoto
        print("изображение")
        self.popup.dismiss()
        ifTriggerPhotio = 3
        PopupGrid = GridLayout(cols=1, pos_hint={'center_x': 0.6, 'center_y': 0.32})
        content4 = Button(text='Закрыть', halign='center', size= (int(200 * koef), int(50 * koef)),
                          size_hint=(None, None), pos = (int(50 * koef), int(50 * koef)), pos_hint=(None, None))
        PopupGrid.add_widget(content4)
        self.popup1 = Popup(title='Сделайте фото с ' + str(triggerPhoto) + ' ракурса', title_align='center', content =PopupGrid, auto_dismiss=False,
                            size_hint=(None, None), pos_hint={"center_x": 0.5, "top": 0.32},
                            size=(int(300 * koef), int(120 * koef)))
        content4.bind(on_press=self.popup1.dismiss)
        self.popup1.open()


class QRWindow(Screen):
    # Класс для считывания QR, или загрузки изображения для считывания QR
    def __init__(self, *args, **kwargs):
        super(QRWindow, self).__init__(*args, **kwargs)

    def ImageLoad(self):
        data = io.BytesIO(open("IMAGE.jpg", "rb").read())
        im = CoreImage(data, ext="png")
        self.ids.ImageBoxId.add_widget(Image(texture=im.texture))


    def ImageDel(self):
        # удаляет все виджеты, которые находяться в another_box
        for i in range(len(self.ids.ImageBoxId.children)):
            self.ids.ImageBoxId.remove_widget(self.ids.ImageBoxId.children[-1])


class FourthWindow(Screen):
    #Окно для просмотра номенклатуры деталей
    def __init__(self, *args, **kwargs):
        super(FourthWindow, self).__init__(*args, **kwargs)
        self.listOfItems=True
    def ScrollWindow(self):
        if (self.listOfItems==True):
            #self.ids.ScrollWindowid.add_widget(ScrollView(size_hint=[1, 1]))
            self.ids.Scrollbuttonid.text = "Список номенклатуры выведен"
            leftGrid = GridLayout(cols=1, size_hint_y=None)
            #Убедимся, что высота такая, чтобы было что прокручивать.
            leftGrid.bind(minimum_height=leftGrid.setter('height'))

            self.toggle = [0 for _ in range(len(ciphers))]

            for index in range(len(ciphers)):
                self.toggle[index] = ToggleButton(
                    text=ciphers[index],  size_hint_y=None,
                    group='cipher', height=30*koef,
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
            self.ids.Scrollbuttonid.text = "Просмотреть номенклатуру"

    def changer(self, *args):
        global resText
        for i in range(len(ciphers)):
            if self.toggle[i].state == 'down':
                resText = comments[i]
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
            self.ids.ButtonScrollWindowReportid.text = resText
            leftGrid1 = GridLayout(cols=len(titleOfItems), spacing=10, size_hint_y=None)#, size_hint_y=10, size_hint_x=10)
            # Убедимся, что высота такая, чтобы было что прокручивать.
            leftGrid1.bind(minimum_height=leftGrid1.setter('height'), minimum_width=leftGrid1.setter('width'))#
            self.toggle = []
            for i in range(len(itemsOfDetails)+1):
                nasted = []
                self.toggle.append(nasted)
                for j in range(len(itemsOfDetails[0])):
                    nasted.append('')

            for index in range(len(titleOfItems)):
                if (index == 0):
                    width = 50*koef
                else:
                    width = 150*koef

                self.toggle[0][index] = Label(
                size_hint_y=None,
                size_hint_x=None,
                height=40*koef,
                width=width,
                #,
                padding=(10*koef, 10*koef),
                    text=str(titleOfItems[index]),
                    color=(1, 1, 1, 1)
                    #text_size=(self.width, None)
                )
                with self.toggle[0][index].canvas.before:
                    Color(0, 1, 0, 0.25)
                    Rectangle(pos=self.toggle[0][index].pos, size=self.toggle[0][index].size)
                leftGrid1.add_widget(self.toggle[0][index])

            for index in range(1,len(itemsOfDetails)+1):
                for index1 in range(len(itemsOfDetails[0])):
                    if (index1 == 0):
                        width = 50*koef
                    else:
                        width = 150*koef

                    self.toggle[index][index1] = Label(
                        size_hint_y=None,
                        size_hint_x=None,
                        height=40*koef,
                        width=width,
                        #text_size=(self.width, None),
                        padding=(10*koef, 10*koef),
                        text=str(itemsOfDetails[index-1][index1]),
                        #text_size=(self.width, None)
                    )
                    leftGrid1.add_widget(self.toggle[index][index1])
            # Убедимся, что высота такая, чтобы было что прокручивать.
            leftGrid1.bind(minimum_height=leftGrid1.setter('height'), minimum_width=leftGrid1.setter('width'))
            self.ids.ScrollWindowReportid.add_widget(leftGrid1)
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
        global resText
        resText = ''


# Менеджер перехода между страницами и передачи данных
class WindowManager(ScreenManager):
    pass

class P(FloatLayout):
    pass

#Функция для всплывающего окна
def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content = show, size_hint=(None,None), size=(400,400))

    popupWindow.open()


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

