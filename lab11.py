import sys
import PySide6.QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot  
from PySide6.QtWidgets import (QApplication, QWidget,QPushButton, QLabel, QVBoxLayout)
from __feature__ import snake_case, true_property

app = QApplication([])


class LayoutOne(QWidget):
    def __init__(self):
        super().__init__()
        label11 = QLabel('<h1>My name is Minsol Cho</h1>')
        vbox = QVBoxLayout()
        vbox.add_widget(label11)
        self.set_layout(vbox)
        self.resize(800,600)
        self.show()
        self.window_title = 'Background'
        self.palette = Qt.yellow

# apply_stylesheet(app, theme='dark_teak.xml')

my_win = LayoutOne()
my_win.show()
class ButtonOne(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        my_btn = QPushButton('Enter')
        self.my_lbl = QLabel('check your name and click enter')
        my_btn.clicked.connect(self.on_click)

        vbox.add_widget(self.my_lbl)
        vbox.add_widget(my_btn)

        self.set_layout(vbox)
        self.resize(400, 400)
        self.show()

    @Slot()
    def on_click(self):
        self.my_lbl.text = 'your name has been checked'

btn_win = ButtonOne()
sys.exit(app.exec())
