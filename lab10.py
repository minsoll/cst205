import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from __feature__ import snake_case, true_property

app =QApplication([])


class LayoutOne(QWidget):
    def __init__(self):
        super().__init__()
        label11 = QLabel('Label 1')
        vbox = QVBoxLayout()
        vbox.add_widget(label11)
        self.set_layout(vbox)
        self.resize(800,800)
        self.show()

        

my_window = LayoutOne()
my_window.show()

# my_qt_app.exec_() runs the main loop
# putting it in sys.exit() allows for a graceful exit
sys.exit(QApplication.exec())