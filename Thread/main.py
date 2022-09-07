# -*- coding: utf-8 -*-
import sys
import time
from PySide2.QtWidgets import QApplication, QWidget
# 从QtCore中导入QThread、Signal和Slot
from PySide2.QtCore import QThread, Signal, Slot
from ui_ui import Ui_Form


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 注意：这里是按钮的点击事件
        # 将pushButton具有的clicked信号与button_clicked()槽连接
        # 这样每次当我们点击按钮，就会执行button()方法
        self.ui.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # 获取界面上的起始数字
        number = int(self.ui.label.text())
        # 注意：使用self将thread声明为属性
        # 避免button_clicked()方法结束，thread中止
        # 将起始数字传给thread
        self.thread = MyThread(number)
        # 将thread的自定义信号连接到接收信号的槽，这里就是update_label()方法
        self.thread.signal.connect(self.update_label)
        # 执行thread
        self.thread.start()

    # 用来接收自定义信号的方法
    # 接收的信号应为一个int变量
    @Slot(int)
    def update_label(self, number):
        # number为接收到的信号
        # 将label更新为接收到的信号，即更新后的数字
        self.ui.label.setText(str(number))
            

# 继承QThread
class MyThread(QThread):
    # 声明一个自定义信号
    # 信号是一个int变量
    signal =Signal(int)

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        # QThread启动时，将会执行这里的代码
        # 每隔一秒，将number减一，直到数字为1
        while True:
            # 判断数字是否等于1，如果为1则结束循环
            if self.number == 1:
                break
            # 数字不为1，等待一秒
            time.sleep(1)
            # 将数字减一
            self.number -= 1
            # 将更新好的数字通过信号传给界面
            # emit()方法将信号发射给建立好连接的槽
            self.signal.emit(self.number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
