import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow

from windows_ui import Ui_Form
from PyQt5 import QtWidgets, QtCore
import convert
import shutil


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.cwd = os.getcwd()
        self.toolButton.clicked.connect(self.getVidPath)
        # self.toolButton_2.clicked.connect(self.getImgPath)
        self.pushButton.clicked.connect(self.startConvert)

    def getVidPath(self):
        dir_choose = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "选取文件夹",
            self.cwd,
            options=QtWidgets.QFileDialog.DontUseNativeDialog) + '/'
        self.lineEdit.setText(dir_choose)
        self.lineEdit_2.setText("自动生成")

    def getImgPath(self):
        dir_choose = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "选取文件夹",
            self.cwd,
            options=QtWidgets.QFileDialog.DontUseNativeDialog) + '/'
        self.lineEdit_2.setText(dir_choose)

    def startConvert(self):

        videos_src = self.lineEdit.text()
        if not videos_src:
            QtWidgets.QMessageBox.warning(self, "警告", "请填视频地址！")
            return
        video_name_list = convert.get_name_by_ext(videos_src, '.mp4')

        images_src = videos_src.rsplit('/', 1)[0] + '_pic/'
        if not os.path.exists(images_src):
            os.mkdir(images_src)
        else:
            shutil.rmtree(images_src)
            os.mkdir(images_src)

        frame_per_second = self.lineEdit_3.text()
        if not frame_per_second:
            QtWidgets.QMessageBox.warning(self, "警告", "请填每秒抽帧数！")
            return

        for one_video_name in video_name_list:
            one_video_path = videos_src + one_video_name
            images_save_path = images_src + one_video_name.split(
                '.mp4')[0] + '/'
            os.mkdir(images_save_path)

            convert.video_to_images(one_video_path, images_save_path,
                                    int(frame_per_second))

        QtWidgets.QMessageBox.information(self, "提示", "视频抽帧完成！")


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec())