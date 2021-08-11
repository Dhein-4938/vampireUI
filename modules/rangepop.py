# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'range_pop.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from . resources_rc import *

class Ui_range_pop(object):
    def setupUi(self, range_pop):
        if not range_pop.objectName():
            range_pop.setObjectName(u"range_pop")
        range_pop.setWindowModality(Qt.NonModal)
        range_pop.resize(450, 130)
        range_pop.setMinimumSize(QSize(450, 130))
        range_pop.setSizeGripEnabled(False)
        range_pop.setModal(False)
        self.gridLayout = QGridLayout(range_pop)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.outerframe = QFrame(range_pop)
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
" #set_unit, #to_label, #plus_label, #set_value, #min_value, #max_value, #incre_value{\n"
"	font: 16pt \"Calibri\";\n"
"	color: rgb(221, 221, 221);\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: none\n"
"}\n"
"#set_value:hover ,#min_value:hover , #max_value:hover , #incre_value:hover {\n"
"	color: rgb(245, 245, 245);\n"
"}\n"
"#outerframe{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 5px solid rgb(122, 115, 227);\n"
"	border-radius: 30px;\n"
"}\n"
"#combobox{\n"
"	font: 14pt \"Calibri\";\n"
"	color: rgb(221, "
                        "221, 221);\n"
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

        self.combobox = QComboBox(self.outerframe)
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.setObjectName(u"combobox")
        self.combobox.setGeometry(QRect(30, 20, 100, 46))
        sizePolicy.setHeightForWidth(self.combobox.sizePolicy().hasHeightForWidth())
        self.combobox.setSizePolicy(sizePolicy)
        self.combobox.setMinimumSize(QSize(100, 0))
        self.combobox.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget = QStackedWidget(self.outerframe)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(140, 10, 301, 66))
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.set = QWidget()
        self.set.setObjectName(u"set")
        self.set_value = QDoubleSpinBox(self.set)
        self.set_value.setObjectName(u"set_value")
        self.set_value.setEnabled(True)
        self.set_value.setGeometry(QRect(100, 15, 65, 30))
        sizePolicy.setHeightForWidth(self.set_value.sizePolicy().hasHeightForWidth())
        self.set_value.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.set_value.setFont(font)
        self.set_value.setWrapping(False)
        self.set_value.setFrame(False)
        self.set_value.setAlignment(Qt.AlignCenter)
        self.set_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.set_value.setDecimals(3)
        self.set_value.setMinimum(-9.000000000000000)
        self.set_value.setMaximum(9.000000000000000)
        self.set_value.setSingleStep(0.100000000000000)
        self.set_value.setValue(0.000000000000000)
        self.set_unit = QLabel(self.set)
        self.set_unit.setObjectName(u"set_unit")
        self.set_unit.setGeometry(QRect(180, 15, 81, 31))
        self.stackedWidget.addWidget(self.set)
        self.range = QWidget()
        self.range.setObjectName(u"range")
        self.min_value = QDoubleSpinBox(self.range)
        self.min_value.setObjectName(u"min_value")
        self.min_value.setEnabled(True)
        self.min_value.setGeometry(QRect(0, 15, 80, 30))
        sizePolicy.setHeightForWidth(self.min_value.sizePolicy().hasHeightForWidth())
        self.min_value.setSizePolicy(sizePolicy)
        self.min_value.setFont(font)
        self.min_value.setWrapping(False)
        self.min_value.setFrame(False)
        self.min_value.setAlignment(Qt.AlignCenter)
        self.min_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.min_value.setDecimals(3)
        self.min_value.setMinimum(-9.000000000000000)
        self.min_value.setMaximum(9.000000000000000)
        self.min_value.setSingleStep(0.100000000000000)
        self.min_value.setValue(0.000000000000000)
        self.max_value = QDoubleSpinBox(self.range)
        self.max_value.setObjectName(u"max_value")
        self.max_value.setEnabled(True)
        self.max_value.setGeometry(QRect(100, 15, 80, 30))
        sizePolicy.setHeightForWidth(self.max_value.sizePolicy().hasHeightForWidth())
        self.max_value.setSizePolicy(sizePolicy)
        self.max_value.setFont(font)
        self.max_value.setWrapping(False)
        self.max_value.setFrame(False)
        self.max_value.setAlignment(Qt.AlignCenter)
        self.max_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.max_value.setDecimals(3)
        self.max_value.setMinimum(-9.000000000000000)
        self.max_value.setMaximum(9.000000000000000)
        self.max_value.setSingleStep(0.100000000000000)
        self.max_value.setValue(0.000000000000000)
        self.incre_value = QDoubleSpinBox(self.range)
        self.incre_value.setObjectName(u"incre_value")
        self.incre_value.setEnabled(True)
        self.incre_value.setGeometry(QRect(210, 15, 80, 30))
        sizePolicy.setHeightForWidth(self.incre_value.sizePolicy().hasHeightForWidth())
        self.incre_value.setSizePolicy(sizePolicy)
        self.incre_value.setFont(font)
        self.incre_value.setWrapping(False)
        self.incre_value.setFrame(False)
        self.incre_value.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.incre_value.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.incre_value.setDecimals(3)
        self.incre_value.setMinimum(-9.000000000000000)
        self.incre_value.setMaximum(9.000000000000000)
        self.incre_value.setSingleStep(0.100000000000000)
        self.incre_value.setValue(0.000000000000000)
        self.to_label = QLabel(self.range)
        self.to_label.setObjectName(u"to_label")
        self.to_label.setGeometry(QRect(80, 20, 20, 30))
        self.to_label.setAlignment(Qt.AlignCenter)
        self.plus_label = QLabel(self.range)
        self.plus_label.setObjectName(u"plus_label")
        self.plus_label.setGeometry(QRect(190, 15, 20, 30))
        self.stackedWidget.addWidget(self.range)

        self.gridLayout.addWidget(self.outerframe, 0, 0, 1, 1)


        self.retranslateUi(range_pop)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(range_pop)
    # setupUi

    def retranslateUi(self, range_pop):
        range_pop.setWindowTitle(QCoreApplication.translate("range_pop", u"Range Input", None))
        self.reset_button.setText(QCoreApplication.translate("range_pop", u"Reset", None))
        self.discard_button.setText(QCoreApplication.translate("range_pop", u"Discard", None))
        self.confirm_button.setText(QCoreApplication.translate("range_pop", u"Confirm", None))
        self.combobox.setItemText(0, QCoreApplication.translate("range_pop", u"Set", None))
        self.combobox.setItemText(1, QCoreApplication.translate("range_pop", u"Range", None))

        self.set_unit.setText(QCoreApplication.translate("range_pop", u"\u00b0", None))
        self.to_label.setText(QCoreApplication.translate("range_pop", u"~", None))
        self.plus_label.setText(QCoreApplication.translate("range_pop", u"+", None))
    # retranslateUi

