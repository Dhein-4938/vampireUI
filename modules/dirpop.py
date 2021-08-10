# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'direction_pop.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_direction_pop(object):
    def setupUi(self, direction_pop):
        if not direction_pop.objectName():
            direction_pop.setObjectName(u"direction_pop")
        direction_pop.resize(450, 130)
        direction_pop.setMinimumSize(QSize(450, 130))
        direction_pop.setSizeGripEnabled(False)
        direction_pop.setModal(False)
        self.gridLayout = QGridLayout(direction_pop)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.outerframe = QFrame(direction_pop)
        self.outerframe.setObjectName(u"outerframe")
        self.outerframe.setMinimumSize(QSize(0, 0))
        self.outerframe.setStyleSheet(u"#confirm_button, #discard_button, #reset_button{\n"
"	font: 14pt \"Calibri\";\n"
"	color: rgb(221, 221, 221);\n"
"	border: none;\n"
"	border-radius: 12px;	\n"
"	background-color: rgb(122, 115, 227);\n"
"}\n"
"#confirm_button:hover, #discard_button:hover, #reset_button:hover {\n"
"	border: 2px solid rgb(193, 193, 255);\n"
"}\n"
"#confirm_button:pressed, #discard_button:pressed, #reset_button:pressed {	\n"
"	background-color: rgb(116, 174, 212);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
" #lable, #dir_x, #dir_y, #dir_z{\n"
"	font: 16pt \"Calibri\";\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: none\n"
"}\n"
"#dir_x:hover:enabled , #dir_y:hover:enabled , #dir_z:hover:enabled {\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"#dir_x:disabled , #dir_y:disabled , #dir_z:disabled {\n"
"	color: rgb(101, 109, 125);\n"
"}\n"
"#outerframe{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 5px solid rgb(122, 115, 227);\n"
"	border-radius: 30px;\n"
"}\n"
"#combobox{\n"
"	font: 14pt"
                        " \"Calibri\";\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"}\n"
"#combobox:hover{\n"
"	border: 3px solid rgb(64, 71, 88);\n"
"}\n"
"#combobox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"}\n"
"#combobox::down-arrow:on {\n"
"	image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"}\n"
"#combobox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left: 3px solid rgba(40, 44, 52, 150);\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"#combobox QAbstractItemView {\n"
"	outline: none;\n"
"	color: rgb(234, 194, 237);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-color: rgb(234, 194, 237);\n"
"	selection-background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:0.8, y2:0.5, stop:0 rgba(122, 115, 227,160), stop:1 rgba(122, 115, 227, 20));\n"
"}")
        self.outerframe.setFrameShape(QFrame.Box)
        self.outerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.outerframe)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 80, 451, 37))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reset_button = QPushButton(self.horizontalLayoutWidget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMinimumSize(QSize(85, 32))
        self.reset_button.setFocusPolicy(Qt.ClickFocus)
        self.reset_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.reset_button)

        self.discard_button = QPushButton(self.horizontalLayoutWidget)
        self.discard_button.setObjectName(u"discard_button")
        sizePolicy.setHeightForWidth(self.discard_button.sizePolicy().hasHeightForWidth())
        self.discard_button.setSizePolicy(sizePolicy)
        self.discard_button.setMinimumSize(QSize(85, 32))
        self.discard_button.setFocusPolicy(Qt.ClickFocus)
        self.discard_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.discard_button)

        self.confirm_button = QPushButton(self.horizontalLayoutWidget)
        self.confirm_button.setObjectName(u"confirm_button")
        sizePolicy.setHeightForWidth(self.confirm_button.sizePolicy().hasHeightForWidth())
        self.confirm_button.setSizePolicy(sizePolicy)
        self.confirm_button.setMinimumSize(QSize(85, 32))
        self.confirm_button.setFocusPolicy(Qt.ClickFocus)
        self.confirm_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.confirm_button)

        self.horizontalLayoutWidget_2 = QWidget(self.outerframe)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(22, 10, 441, 56))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.combobox = QComboBox(self.horizontalLayoutWidget_2)
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.setObjectName(u"combobox")
        sizePolicy.setHeightForWidth(self.combobox.sizePolicy().hasHeightForWidth())
        self.combobox.setSizePolicy(sizePolicy)
        self.combobox.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_2.addWidget(self.combobox)

        self.left_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.left_horizontalSpacer)

        self.frame = QFrame(self.horizontalLayoutWidget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(230, 52))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.dir_z = QDoubleSpinBox(self.frame)
        self.dir_z.setObjectName(u"dir_z")
        self.dir_z.setEnabled(True)
        self.dir_z.setGeometry(QRect(150, 10, 65, 30))
        sizePolicy.setHeightForWidth(self.dir_z.sizePolicy().hasHeightForWidth())
        self.dir_z.setSizePolicy(sizePolicy)
        self.dir_z.setWrapping(False)
        self.dir_z.setFrame(False)
        self.dir_z.setAlignment(Qt.AlignCenter)
        self.dir_z.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dir_z.setDecimals(3)
        self.dir_z.setMinimum(-9.000000000000000)
        self.dir_z.setMaximum(9.000000000000000)
        self.dir_z.setSingleStep(0.100000000000000)
        self.dir_z.setValue(1.000000000000000)
        self.dir_x = QDoubleSpinBox(self.frame)
        self.dir_x.setObjectName(u"dir_x")
        self.dir_x.setEnabled(True)
        self.dir_x.setGeometry(QRect(10, 10, 65, 30))
        sizePolicy.setHeightForWidth(self.dir_x.sizePolicy().hasHeightForWidth())
        self.dir_x.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.dir_x.setFont(font)
        self.dir_x.setWrapping(False)
        self.dir_x.setFrame(False)
        self.dir_x.setAlignment(Qt.AlignCenter)
        self.dir_x.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dir_x.setDecimals(3)
        self.dir_x.setMinimum(-9.000000000000000)
        self.dir_x.setMaximum(9.000000000000000)
        self.dir_x.setSingleStep(0.100000000000000)
        self.dir_x.setValue(0.000000000000000)
        self.dir_y = QDoubleSpinBox(self.frame)
        self.dir_y.setObjectName(u"dir_y")
        self.dir_y.setEnabled(True)
        self.dir_y.setGeometry(QRect(80, 10, 65, 30))
        sizePolicy.setHeightForWidth(self.dir_y.sizePolicy().hasHeightForWidth())
        self.dir_y.setSizePolicy(sizePolicy)
        self.dir_y.setWrapping(False)
        self.dir_y.setFrame(False)
        self.dir_y.setAlignment(Qt.AlignCenter)
        self.dir_y.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dir_y.setDecimals(3)
        self.dir_y.setMinimum(-9.000000000000000)
        self.dir_y.setMaximum(9.000000000000000)
        self.dir_y.setSingleStep(0.100000000000000)
        self.dir_y.setValue(0.000000000000000)
        self.lable = QLabel(self.frame)
        self.lable.setObjectName(u"lable")
        self.lable.setGeometry(QRect(2, 5, 230, 41))
        self.lable.setStyleSheet(u"")
        self.lable.raise_()
        self.dir_z.raise_()
        self.dir_x.raise_()
        self.dir_y.raise_()

        self.horizontalLayout_2.addWidget(self.frame)

        self.right_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.right_horizontalSpacer)


        self.gridLayout.addWidget(self.outerframe, 0, 0, 1, 1)

        QWidget.setTabOrder(self.dir_x, self.dir_y)
        QWidget.setTabOrder(self.dir_y, self.dir_z)
        QWidget.setTabOrder(self.dir_z, self.combobox)

        self.retranslateUi(direction_pop)

        QMetaObject.connectSlotsByName(direction_pop)
    # setupUi

    def retranslateUi(self, direction_pop):
        direction_pop.setWindowTitle(QCoreApplication.translate("direction_pop", u"Direction Input", None))
        self.reset_button.setText(QCoreApplication.translate("direction_pop", u"Reset", None))
        self.discard_button.setText(QCoreApplication.translate("direction_pop", u"Discard", None))
        self.confirm_button.setText(QCoreApplication.translate("direction_pop", u"Confirm", None))
        self.combobox.setItemText(0, QCoreApplication.translate("direction_pop", u"random", None))
        self.combobox.setItemText(1, QCoreApplication.translate("direction_pop", u"random grain", None))
        self.combobox.setItemText(2, QCoreApplication.translate("direction_pop", u"specific", None))

        self.lable.setText(QCoreApplication.translate("direction_pop", u"[             ,             ,             ]", None))
    # retranslateUi

