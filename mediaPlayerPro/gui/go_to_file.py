import os
from settings import language
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class GoToFile(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("go to  file"))
        self.file=qt.QComboBox()
        self.file.setAccessibleName(_("select files"))
        self.file.addItems(p.folder_files)
        self.open=qt.QPushButton(_("open"))
        self.open.setDefault(True)
        self.open.clicked.connect(lambda:self.Oopen(p))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.file)
        layout.addWidget(self.open)
        self.setLayout(layout)
    def Oopen(self,p):
        a=p.folder_files.index(self.file.currentText())
        p.playMedia(os.path.join(p.folder_path,p.folder_files[a]))
        p.MF.setDisabled(False)
        p.folder_index=a
        self.close()