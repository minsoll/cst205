import sys
from PySide6.QtWidgets import (QApplication, QWidget, 
                               QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox)
from __feature__ import snake_case, true_property
# from qt_material import apply_stylesheet

app = QApplication([])

class ButtonOne(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()
      my_btn = QPushButton('button 1')
      self.my_lbl = QLabel('button not yet clicked')
      my_btn.clicked.connect(self.on_click)
      vbox.add_widget(self.my_lbl)
      vbox.add_widget(my_btn)
      self.set_layout(vbox)
      self.resize(400, 400)
      self.show()
  @Slot()
  def on_click(self):
      self.my_lbl.text = 'button has been clicked!'
           
class LayoutOne(QWidget):
  def __init__(self):
      super().__init__()
      label1 = QLabel('Label 1')
      label2 = QLabel('Label 2')
      vbox = QVBoxLayout()
      vbox.add_widget(label1)
      vbox.add_widget(label2)
      self.set_layout(vbox)
      self.resize(800, 600)
      self.show()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # self.set_layout(vbox)
        # self.window_title = "CST 205 App"
        

        self.my_list = ["Pick a value", "vanilla", "chocolate", "raspberry", "coconut"]

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

# apply_stylesheet(app, theme='dark_teal.xml')
app = QApplication([])
my_win = MyWindow()
my_win.show()



my_win = LayoutOne()
sys.exit(app.exec())
