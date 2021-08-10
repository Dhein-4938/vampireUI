# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exp_unit_pop.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_exp_unit_pop(object):
    def setupUi(self, exp_unit_pop):
        if not exp_unit_pop.objectName():
            exp_unit_pop.setObjectName(u"exp_unit_pop")
        exp_unit_pop.resize(380, 120)
        self.gridLayout = QGridLayout(exp_unit_pop)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.outerframe = QFrame(exp_unit_pop)
        self.outerframe.setObjectName(u"outerframe")
        self.outerframe.setMinimumSize(QSize(380, 120))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        self.outerframe.setFont(font)
        self.outerframe.setAutoFillBackground(False)
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
" #sig, #exp{\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: none\n"
"}\n"
"#sig {	font: 18pt \"Calibri\";   }\n"
"#exp {	font: 16pt \"Calibri\";   }\n"
" #sig:hover, #exp:hover {\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"#outerframe{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 5px solid rgb(122, 115, 227);\n"
"	border-radius: 30px;\n"
"}\n"
"#combobox{\n"
"	font: 14pt \"Calibri\";\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;"
                        "\n"
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
        self.combobox = QComboBox(self.outerframe)
        self.combobox.setObjectName(u"combobox")
        self.combobox.setGeometry(QRect(200, 15, 140, 35))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.combobox.setFont(font1)
        self.combobox.setFocusPolicy(Qt.WheelFocus)
        self.combobox.setAutoFillBackground(False)
        self.combobox.setFrame(True)
        self.sig = QDoubleSpinBox(self.outerframe)
        self.sig.setObjectName(u"sig")
        self.sig.setEnabled(True)
        self.sig.setGeometry(QRect(30, 17, 121, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sig.sizePolicy().hasHeightForWidth())
        self.sig.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        self.sig.setFont(font2)
        self.sig.setStyleSheet(u"")
        self.sig.setWrapping(False)
        self.sig.setFrame(False)
        self.sig.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sig.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sig.setDecimals(3)
        self.sig.setMinimum(-999.000000000000000)
        self.sig.setMaximum(999.000000000000000)
        self.sig.setSingleStep(0.100000000000000)
        self.sig.setValue(0.000000000000000)
        self.exp = QSpinBox(self.outerframe)
        self.exp.setObjectName(u"exp")
        self.exp.setEnabled(True)
        self.exp.setGeometry(QRect(150, 10, 41, 22))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.exp.setFont(font3)
        self.exp.setWrapping(False)
        self.exp.setFrame(False)
        self.exp.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.exp.setProperty("showGroupSeparator", False)
        self.exp.setMinimum(-99)
        self.exp.setMaximum(99)
        self.exp.setValue(0)
        self.horizontalLayoutWidget = QWidget(self.outerframe)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 75, 381, 35))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reset_button = QPushButton(self.horizontalLayoutWidget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMinimumSize(QSize(85, 32))
        self.reset_button.setFont(font1)
        self.reset_button.setFocusPolicy(Qt.ClickFocus)
        self.reset_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.reset_button)

        self.discard_button = QPushButton(self.horizontalLayoutWidget)
        self.discard_button.setObjectName(u"discard_button")
        sizePolicy.setHeightForWidth(self.discard_button.sizePolicy().hasHeightForWidth())
        self.discard_button.setSizePolicy(sizePolicy)
        self.discard_button.setMinimumSize(QSize(85, 32))
        self.discard_button.setFont(font1)
        self.discard_button.setFocusPolicy(Qt.ClickFocus)
        self.discard_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.discard_button)

        self.confirm_button = QPushButton(self.horizontalLayoutWidget)
        self.confirm_button.setObjectName(u"confirm_button")
        sizePolicy.setHeightForWidth(self.confirm_button.sizePolicy().hasHeightForWidth())
        self.confirm_button.setSizePolicy(sizePolicy)
        self.confirm_button.setMinimumSize(QSize(85, 32))
        self.confirm_button.setFont(font1)
        self.confirm_button.setFocusPolicy(Qt.ClickFocus)
        self.confirm_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.confirm_button)


        self.gridLayout.addWidget(self.outerframe, 0, 0, 1, 1)


        self.retranslateUi(exp_unit_pop)

        QMetaObject.connectSlotsByName(exp_unit_pop)
    # setupUi

    def retranslateUi(self, exp_unit_pop):
        exp_unit_pop.setWindowTitle(QCoreApplication.translate("exp_unit_pop", u"Unit Input", None))
#if QT_CONFIG(whatsthis)
        self.combobox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.sig.setSuffix(QCoreApplication.translate("exp_unit_pop", u"x10", None))
        self.reset_button.setText(QCoreApplication.translate("exp_unit_pop", u"Reset", None))
        self.discard_button.setText(QCoreApplication.translate("exp_unit_pop", u"Discard", None))
        self.confirm_button.setText(QCoreApplication.translate("exp_unit_pop", u"Confirm", None))
    # retranslateUi

