from settings import language,settings_handler,app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class JumpToTime(qt.QDialog):
    def __init__(self,p,duration):
        super().__init__(p)
        self.setWindowTitle(_("jump to time"))
        layout=qt.QVBoxLayout()
        self.u=qt.QSpinBox()
        self.u.setAccessibleName(_("hours"))
        self.u.setValue(duration[0])
        self.u.setRange(0,duration[0])
        if duration[0]==0:
            pass
        else:
            layout.addWidget(self.u)
        self.m=qt.QSpinBox()
        self.m.setAccessibleName(_("minutes"))
        self.m.setValue(duration[1])
        self.m.setRange(0,duration[1])
        if duration[1]==0:
            pass
        else:
            layout.addWidget(self.m)
        s=qt.QSpinBox()
        s.setAccessibleName(_("Seconds"))
        s.setValue(duration[2])
        s.setRange(0,59)
        layout.addWidget(s)
        set=qt.QPushButton(_("set time"))
        set.setDefault(True)
        set.clicked.connect(lambda:self.a(p,s))
        layout.addWidget(set)
        self.setLayout(layout)
    def a(self,p,s):
        p.player.setPosition(self.u.value()*3600000+self.m.value()*60000+s.value()*1000)
        self.close()