import sys
import string
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI2.ui', self)
        self.english_alphabet = 'abcdefghijklmnopqrstuvwxyz'            #  Алфавит для генерации доп. букв
        self.russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'     #
        self.encryption_radioButton.setChecked(True)
        self.RU_radioButton.setChecked(True)
        self.label_6.setPixmap(QPixmap('123.png'))
        self.encryption_radioButton.toggled.connect(self.enableWidget_3)
        self.decryption_radioButton.toggled.connect(self.enableWidget_4)
        self.widget_3.show()
        self.widget_4.hide()
        self.pushButton.clicked.connect(self.func)
        self.pushButton.setStyleSheet(
            '''
            QPushButton:hover {
                background-color: rgb(74, 74, 74);
                border-color: green;
                border-width: 2px;
                border-style: solid;
                border-radius: 10px;
                color: green;
            }

            QPushButton {
                background-color: rgb(74, 74, 74);
                border-color: rgb(225, 225, 225);
                border-width: 2px;
                border-style: solid;
                border-radius: 10px;
                color: rgb(235, 235, 235);
            }
            '''
        )
    def enableWidget_3(self):
        self.widget_3.show()
        self.widget_4.hide()

    def enableWidget_4(self):
        self.widget_4.show()

    def change_color(self):
        self.pushButton.setStyleSheet("""
            QPushButton:hover {
                background-color: rgb(74, 74, 74);
                border-color: red;
                border-width: 2px;
                border-style: solid;
                border-radius: 10px;
                color: red;
            }

            QPushButton {
                background-color: rgb(74, 74, 74);
                border-color: rgb(225, 225, 225);
                border-width: 2px;
                border-style: solid;
                border-radius: 10px;
                color: rgb(235, 235, 235);
            }
        """)
        QTimer.singleShot(300, lambda: self.pushButton.setStyleSheet("""
        QPushButton {
            background-color: rgb(74, 74, 74);
            border-color: rgb(225, 225, 225);
            border-width: 2px;
            border-style: solid;
            border-radius: 10px;
            color: rgb(235, 235, 235);
        }
        QPushButton:hover {
                background-color: rgb(74, 74, 74);
                border-color: green;
                border-width: 2px;
                border-style: solid;
                border-radius: 10px;
                color: green;
            }
        """))

        self.label_3.setStyleSheet("""
            color: red;
            border-width: 2px;
            border-style: solid;
            border-color: red;
            background-color: rgb(74, 74, 74);
        """)
        QTimer.singleShot(300, lambda: self.label_3.setStyleSheet("""
            color:rgb(247, 247, 247);
            border-width: 2px;
            border-style: solid;
            border-color: rgb(243, 243, 243);
            background-color: rgb(74, 74, 74);
        """))

    def func(self):
        self.change_color()
        key = self.kayBox.value()
        lang = 'RU' if self.RU_radioButton.isChecked() else 'EU'
        translator = str.maketrans("", "", string.punctuation)
        if self.encryption_radioButton.isChecked():
            data = self.input_textEdit.toPlainText().strip().replace(' ', '').translate(translator).upper()
            self.encryption(key, lang, data)
        else:
            data = self.input_textEdit.toPlainText().strip().upper()
            key2 = self.kayBox_2.value()
            self.decryption(key, key2, data)

    def encryption(self, key, lang, data):   #Функция для шифрования сообщения
        if data:
            text_length = len(data)
            count = text_length % key
            if count != 0:
                needed_to_add = key - count
                if lang == 'RU':
                    random_letters = ''.join(random.choices(self.russian_alphabet, k=needed_to_add)).upper()
                else:
                    random_letters = ''.join(random.choices(self.english_alphabet, k=needed_to_add)).upper()
                data += random_letters
            text_with_spaces = ''
            for i in range(0, len(data), key):
                text_with_spaces += data[i:i + key] + ' '
            reverse_text = text_with_spaces[::-1].strip()
            self.output_textEdit.setPlainText(reverse_text)
        else:
            pass

    def decryption(self, groups_langth, count_letters, data):  #Функция для расшифрования сообщения
        if data:
            count = count_letters % groups_langth
            data = data.replace(' ', '')
            if count != 0:
                needed_to_add = groups_langth - count
                data = data[needed_to_add:]
                data = data[::-1]
                self.output_textEdit.setPlainText(data)
            else:
                self.output_textEdit.setPlainText(data[::-1])
        else:
            self.output_textEdit.setPlainText("Ошибка!!! Вы не ввели текст.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

