# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QWidget, QApplication
from ui_signal import Ui_Form


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 将lineEdit具有的textChanged信号与update_label()槽连接
        # 这样每次当lineEdit的文本发生变化，就会执行update_label()方法
        self.ui.lineEdit.textChanged.connect(self.update_label)

    def update_label(self):
        # 获取当前lineEdit的文本内容
        text = self.ui.lineEdit.text()
        # 更新label的文本
        self.ui.label.setText(text)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
