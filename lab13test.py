import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton)
from PySide6.QtCore import Qt 
from __feature__ import snake_case, true_property

app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        #1 Background color
        self.window_title = 'Background'
        self.palette = Qt.yellow
        
        h_layout = QHBoxLayout()
        b1 = QPushButton("A")
        b2 = QPushButton("B")

        h_layout.add_widget(b1)
        h_layout.add_widget(b2)

        v_layout = QVBoxLayout()
        b4 = QPushButton("D")
        b5 = QPushButton("E")

        v_layout.add_widget(b4)
        v_layout.add_widget(b5)

        main_layout = QHBoxLayout()

        main_layout.add_layout(h_layout)
        main_layout.add_layout(v_layout)
        self.set_layout(main_layout)

a = MyWindow()
a.show()
sys.exit(app.exec())
