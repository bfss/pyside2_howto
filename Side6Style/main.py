# -*- coding: utf-8 -*-
import sys
# 这里导入了QStyleFactory
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 在这里设置为windowsvista样式
    app.setStyle(QStyleFactory.create('windowsvista'))
    # 输出当前系统支持的所有内置样式
    print(QStyleFactory.keys())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
