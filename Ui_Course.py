# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Course\Course\Course.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.setEnabled(True)
        dialog.resize(837, 430)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setMinimumSize(QtCore.QSize(837, 430))
        dialog.setMaximumSize(QtCore.QSize(837, 430))
        dialog.setAcceptDrops(False)
        dialog.setSizeGripEnabled(True)
        self.lw_course = QtGui.QListWidget(dialog)
        self.lw_course.setGeometry(QtCore.QRect(10, 71, 181, 201))
        self.lw_course.setObjectName(_fromUtf8("lw_course"))
        self.rb_gxk = QtGui.QRadioButton(dialog)
        self.rb_gxk.setGeometry(QtCore.QRect(770, 41, 61, 16))
        self.rb_gxk.setObjectName(_fromUtf8("rb_gxk"))
        self.b_delete = QtGui.QPushButton(dialog)
        self.b_delete.setGeometry(QtCore.QRect(790, 340, 41, 23))
        self.b_delete.setObjectName(_fromUtf8("b_delete"))
        self.b_close = QtGui.QPushButton(dialog)
        self.b_close.setGeometry(QtCore.QRect(150, 400, 75, 23))
        self.b_close.setObjectName(_fromUtf8("b_close"))
        self.rb_bzy = QtGui.QRadioButton(dialog)
        self.rb_bzy.setGeometry(QtCore.QRect(680, 41, 89, 16))
        self.rb_bzy.setChecked(True)
        self.rb_bzy.setObjectName(_fromUtf8("rb_bzy"))
        self.b_down = QtGui.QPushButton(dialog)
        self.b_down.setGeometry(QtCore.QRect(790, 310, 41, 23))
        self.b_down.setObjectName(_fromUtf8("b_down"))
        self.lw_msg = QtGui.QListWidget(dialog)
        self.lw_msg.setGeometry(QtCore.QRect(200, 71, 631, 201))
        self.lw_msg.setObjectName(_fromUtf8("lw_msg"))
        self.lw_choose = QtGui.QListWidget(dialog)
        self.lw_choose.setGeometry(QtCore.QRect(10, 281, 771, 111))
        self.lw_choose.setDragEnabled(True)
        self.lw_choose.setObjectName(_fromUtf8("lw_choose"))
        self.b_ok = QtGui.QPushButton(dialog)
        self.b_ok.setGeometry(QtCore.QRect(740, 401, 75, 21))
        self.b_ok.setObjectName(_fromUtf8("b_ok"))
        self.b_up = QtGui.QPushButton(dialog)
        self.b_up.setGeometry(QtCore.QRect(790, 280, 41, 23))
        self.b_up.setObjectName(_fromUtf8("b_up"))
        self.b_clear = QtGui.QPushButton(dialog)
        self.b_clear.setGeometry(QtCore.QRect(790, 370, 41, 23))
        self.b_clear.setObjectName(_fromUtf8("b_clear"))
        self.lb = QtGui.QLabel(dialog)
        self.lb.setGeometry(QtCore.QRect(310, 403, 421, 16))
        self.lb.setText(_fromUtf8(""))
        self.lb.setObjectName(_fromUtf8("lb"))
        self.b_stop = QtGui.QPushButton(dialog)
        self.b_stop.setGeometry(QtCore.QRect(230, 401, 75, 21))
        self.b_stop.setObjectName(_fromUtf8("b_stop"))
        self.tb_id = QtGui.QLineEdit(dialog)
        self.tb_id.setGeometry(QtCore.QRect(40, 40, 101, 20))
        self.tb_id.setToolTip(_fromUtf8(""))
        self.tb_id.setStatusTip(_fromUtf8(""))
        self.tb_id.setWhatsThis(_fromUtf8(""))
        self.tb_id.setInputMask(_fromUtf8(""))
        self.tb_id.setText(_fromUtf8(""))
        self.tb_id.setMaxLength(8)
        self.tb_id.setObjectName(_fromUtf8("tb_id"))
        self.tb_pw = QtGui.QLineEdit(dialog)
        self.tb_pw.setGeometry(QtCore.QRect(180, 40, 171, 20))
        self.tb_pw.setText(_fromUtf8(""))
        self.tb_pw.setObjectName(_fromUtf8("tb_pw"))
        self.b_login = QtGui.QPushButton(dialog)
        self.b_login.setGeometry(QtCore.QRect(599, 40, 75, 23))
        self.b_login.setObjectName(_fromUtf8("b_login"))
        self.code = QtGui.QPushButton(dialog)
        self.code.setGeometry(QtCore.QRect(450, 40, 75, 23))
        self.code.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.code.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Shen/Anaconda2/Lib/site-packages/pytesser/1vy4.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.code.setIcon(icon)
        self.code.setIconSize(QtCore.QSize(78, 40))
        self.code.setObjectName(_fromUtf8("code"))
        self.l_zt = QtGui.QLabel(dialog)
        self.l_zt.setGeometry(QtCore.QRect(10, 403, 131, 16))
        self.l_zt.setObjectName(_fromUtf8("l_zt"))
        self.b_code = QtGui.QLineEdit(dialog)
        self.b_code.setGeometry(QtCore.QRect(530, 40, 61, 20))
        self.b_code.setMaxLength(4)
        self.b_code.setObjectName(_fromUtf8("b_code"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 14, 191, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.url = QtGui.QLineEdit(dialog)
        self.url.setGeometry(QtCore.QRect(200, 11, 631, 20))
        self.url.setText(_fromUtf8(""))
        self.url.setObjectName(_fromUtf8("url"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(11, 41, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(152, 42, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(356, 41, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tb_name = QtGui.QLineEdit(dialog)
        self.tb_name.setGeometry(QtCore.QRect(383, 40, 61, 20))
        self.tb_name.setText(_fromUtf8(""))
        self.tb_name.setObjectName(_fromUtf8("tb_name"))

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.b_close, QtCore.SIGNAL(_fromUtf8("clicked()")), dialog.close)
        QtCore.QObject.connect(self.b_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lw_choose.clear)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.url, self.tb_id)
        dialog.setTabOrder(self.tb_id, self.tb_pw)
        dialog.setTabOrder(self.tb_pw, self.tb_name)
        dialog.setTabOrder(self.tb_name, self.code)
        dialog.setTabOrder(self.code, self.b_code)
        dialog.setTabOrder(self.b_code, self.b_login)
        dialog.setTabOrder(self.b_login, self.rb_bzy)
        dialog.setTabOrder(self.rb_bzy, self.rb_gxk)
        dialog.setTabOrder(self.rb_gxk, self.lw_course)
        dialog.setTabOrder(self.lw_course, self.lw_msg)
        dialog.setTabOrder(self.lw_msg, self.lw_choose)
        dialog.setTabOrder(self.lw_choose, self.b_up)
        dialog.setTabOrder(self.b_up, self.b_down)
        dialog.setTabOrder(self.b_down, self.b_delete)
        dialog.setTabOrder(self.b_delete, self.b_clear)
        dialog.setTabOrder(self.b_clear, self.b_ok)
        dialog.setTabOrder(self.b_ok, self.b_stop)
        dialog.setTabOrder(self.b_stop, self.b_close)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "正方教务系统刷课软件 by.Syhen（喝药）", None))
        self.rb_gxk.setText(_translate("dialog", "公选课", None))
        self.b_delete.setText(_translate("dialog", "删除", None))
        self.b_close.setText(_translate("dialog", "关闭", None))
        self.rb_bzy.setText(_translate("dialog", "本专业选课", None))
        self.b_down.setText(_translate("dialog", "下移", None))
        self.lw_choose.setSortingEnabled(False)
        self.b_ok.setText(_translate("dialog", "开始刷课", None))
        self.b_up.setText(_translate("dialog", "上移", None))
        self.b_clear.setText(_translate("dialog", "清空", None))
        self.b_stop.setText(_translate("dialog", "停止", None))
        self.tb_pw.setToolTip(_translate("dialog", "<html><head/><body><p>密码</p></body></html>", None))
        self.b_login.setText(_translate("dialog", "登录", None))
        self.l_zt.setText(_translate("dialog", "状态：", None))
        self.label.setText(_translate("dialog", "请输入正方教务系统登录界面网址：", None))
        self.label_2.setText(_translate("dialog", "学号", None))
        self.label_3.setText(_translate("dialog", "密码", None))
        self.label_4.setText(_translate("dialog", "姓名", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

