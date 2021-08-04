# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Vampire - Modern GUI"
        description = "Vampire APP - handles all vampire input files for you"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_load.clicked.connect(self.buttonClick)
        widgets.btn_input.clicked.connect(self.buttonClick)
        widgets.btn_material.clicked.connect(self.buttonClick)
        widgets.btn_tag.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        AppFunctions.setCustomStyle(self)
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # SET SELECT PAGE
        # ///////////////////////////////////////////////////////////////
        self.initHome()
        self.initLoad()
        self.initSelect()
        widgets.left_tree.doubleClicked.connect(lambda input: Material.displayItem(self, input, setBool=True))
        widgets.right_tree.doubleClicked.connect(lambda input: Material.displayItem(self, input, setBool=False))
        widgets.btn_select_next.clicked.connect(self.buttonClick)

        # SET PARAM PAGE
        # ///////////////////////////////////////////////////////////////
        self.initParam()
        widgets.param_set_tree.doubleClicked.connect(lambda index: Material.disableParam(self, index))
        widgets.btn_param_back.clicked.connect(self.buttonClick)
        widgets.btn_param_next.clicked.connect(self.buttonClick)
        widgets.btn_newmat.clicked.connect(self.buttonClick)
        widgets.btn_removemat.clicked.connect(self.buttonClick)

        # SET DISPLAY PAGE
        # ///////////////////////////////////////////////////////////////
        widgets.btn_display_back.clicked.connect(self.buttonClick)



    # BUTTONS CLICK
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # MENU BUTTONS
        # ///////////////////////////////////////////////////////////////
        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW LOAD PAGE
        if btnName == "btn_load":
            widgets.stackedWidget.setCurrentWidget(widgets.load)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW INPUT PAGE
        if btnName == "btn_input":
            #widgets.stackedWidget.setCurrentWidget(widgets.load)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW SELECT PAGE
        if btnName == "btn_material":
            widgets.stackedWidget.setCurrentWidget(widgets.select) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        # SHOW TAG PAGE
        if btnName == "btn_tag":
            #widgets.stackedWidget.setCurrentWidget(widgets.load)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW SAVE PAGE
        if btnName == "btn_save":
            #widgets.stackedWidget.setCurrentWidget(widgets.load)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # MATERIAL PAGE BUTTONS
        # ///////////////////////////////////////////////////////////////
        # CHANGE TO SELECT PAGE
        if btnName == "btn_param_back":
            widgets.stackedWidget.setCurrentWidget(widgets.select)
        # CHANGE TO PARAM PAGE
        if btnName in ["btn_select_next","btn_display_back"]:
            widgets.stackedWidget.setCurrentWidget(widgets.param)
            Material.displayParamSet(self)
        # CHANGE TO DISPLAY PAGE
        if btnName == "btn_param_next":
            widgets.stackedWidget.setCurrentWidget(widgets.display)
            Material.translateToDisplay(self)

        # MATERIAL FUNCTION PAGE
        # //////////////////////////////////////////////////////////////
        # ADD AND REMOVE MATERIAL
        if btnName == "btn_newmat":
            Material.addMaterial(self)
        if btnName == "btn_removemat":
            Material.removeMaterial(self)
        # PRINT BTN NAME
        #print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            #print('Mouse click: LEFT CLICK')
            pass
        if event.buttons() == Qt.RightButton:
            #print('Mouse click: RIGHT CLICK')
            pass

    # PAGE INITIAL
    # ///////////////////////////////////////////////////////////////
    def initHome(self):
        pass

    def initLoad(self):
        pass  

    def initSelect(self):
        # set state instances
        self.catState = [False]*len(Settings.MATERIAL_SETUP)
        self.groupState = [ [False]*len(Settings.MATERIAL_SETUP[catName]) for catName in Settings.MATERIAL_SETUP.keys() ]
        # create the model for the treeviews
        self.LgroupModel = QStandardItemModel()
        self.LgroupRootItem = self.LgroupModel.invisibleRootItem()
        self.RgroupModel = QStandardItemModel()
        self.RgroupRootItem = self.RgroupModel.invisibleRootItem()
        # call initializing functions
        Material.initLeftTree(self)
        Material.initRightTree(self)

    def initParam(self):
        # set param instances
        self.paramHeader = ["Parameters"]
        self.materialAmount = 12
        self.currentMaterialAmount = 0
        # create the model for the treeview
        self.paramSetModel = QStandardItemModel()
        self.paramRootItem = self.paramSetModel.invisibleRootItem()
        # call initializing functions
        Material.initParamSetTree(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
