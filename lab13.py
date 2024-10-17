#cst205
#minsol Cho 

#1
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

my_qt_app = QApplication([])
class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Background'
        self.palette = Qt.yellow

my_window = ColorWindow()
my_window.show()
sys.exit(my_qt_app.exec())

#2
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton)
from __feature__ import snake_case, true_property
from PySide6.QtCore import Qt

app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.palette = Qt.yellow
        
        v_layout = QVBoxLayout()
        b1 = QPushButton("1")
        b2 = QPushButton("2")
        
        v_layout.add_widget(b1)
        v_layout.add_widget(b2)

        h_layout = QHBoxLayout()
        b3 = QPushButton("3")
        b4 = QPushButton("4")
        
        h_layout.add_widget(b3)
        h_layout.add_widget(b4)
        
        main_layout = QHBoxLayout()
        main_layout.add_layout(v_layout)
        main_layout.add_layout(h_layout)
        self.set_layout(main_layout)

a = MyWindow()
a.show()
sys.exit(app.exec())

#3
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_list = ["Pick a color", "red", "yellow", "blue", "black"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.current_text
        my_index = self.my_combo_box.current_index
        self.my_label.text = f'You chose {self.my_list[my_index]}.'


app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())
