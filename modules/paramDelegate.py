from modules import *
from . dirpop import *
from . unitpop import *
from math import floor, log10

class ParamSetDelegate(QStyledItemDelegate):
    font = QFont("Calibri", 14)
    def __init__(self, parent:QMainWindow):
        super(ParamSetDelegate, self).__init__(parent)
        self.window = parent
        self.treeview = parent.ui.param_set_tree
        
    def createEditor(self, parent:QWidget, option:QStyleOptionViewItem, index:QModelIndex):
        if(index.column() == 0): return None
        if(index.siblingAtColumn(0).data() in ["Material Name","Jmol Element"]):
            self.dataType = "text"
            self.placeholder = "(name)" if(index.siblingAtColumn(0).data() == "Material Name") else "(element)"
            lineEdit = QLineEdit(parent)
            lineEdit.setObjectName("editor")
            lineEdit.setStyleSheet(Settings.LINEEDIT_STYLESHEET)
            return lineEdit
        cursor = index.siblingAtColumn(0)
        pathName = []
        while(cursor.data()!=None):
            pathName.append(cursor.data())
            cursor = cursor.parent()
        if(len(pathName) == 3):
            self.paramData = Settings.MATERIAL_SETUP[pathName[2]][pathName[1]][pathName[0]]
        elif(len(pathName) == 2):
            self.paramData = Settings.MATERIAL_SETUP[pathName[1]][pathName[0]]
        else: return None
        self.dataType = self.paramData[0]
        if(self.dataType == "combo"):
            combo = QComboBox(parent)
            combo.setObjectName("editor")
            self.dataList = self.paramData[1]
            combo.addItems(self.dataList)
            combo.setStyleSheet(Settings.COMBOBOX_STYLESHEET)
            return combo
        elif(self.dataType == "spin"):
            spin = QSpinBox(parent)
            spin.setObjectName("editor")
            spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
            spin.setFrame(False)
            spin.setStyleSheet(Settings.SPINBOX_STYLESHEET)
            return spin
        elif(self.dataType == "dspin"):
            dspin = QDoubleSpinBox(parent)
            dspin.setObjectName("editor")
            dspin.setButtonSymbols(QAbstractSpinBox.NoButtons)
            dspin.setFrame(False)
            dspin.setDecimals(3)
            dspin.setSingleStep(0.1)
            dspin.setRange(-99,99)
            dspin.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
            dspin.setStyleSheet(Settings.SPINBOX_STYLESHEET)
            return dspin
        elif(self.dataType in ["3dspin","dir-1","dir-2"]):
            dirpop = DirPopWindow(parent,self.dataType)
            dirpop.setFixedSize(450,130)
            return dirpop
        elif(self.dataType == "text"):
            self.placeholder = "(filename)"
            lineEdit = QLineEdit(parent)
            lineEdit.setObjectName("editor")
            lineEdit.setStyleSheet(Settings.LINEEDIT_STYLESHEET)
            return lineEdit
        elif(self.dataType in Settings.UNIT_LIST):
            unitpop = UnitPopWindow(parent,self.dataType,self.paramData[1])
            unitpop.setFixedSize(380,120)
            return unitpop
        return None
    
    def updateEditorGeometry(self, editor:QWidget, option:QStyleOptionViewItem, index:QModelIndex):
        if(index.column() == 0): return None
        rect = option.rect
        if(self.dataType in ["3dspin","dir-1","dir-2"] or self.dataType in Settings.UNIT_LIST):
            X_CORRECTION, Y_CORRECTION = 1, 51
            treeGPos = self.window.ui.param_set_tree.mapToGlobal(QPoint(0,0))
            editorWidth = editor.rect().width()
            editorHeight = editor.rect().height()
            wShift, hShift, xShift, yShift = Settings.SHIFT_DIRECTION["right-center"]    # changeable, might be linking to custom preference setting 
            x = treeGPos.x() + X_CORRECTION + rect.x() + int(editorWidth*wShift) + xShift
            y = treeGPos.y() + Y_CORRECTION + rect.y() + int(editorHeight*hShift) + yShift
            editor.setGeometry( x, y, editorWidth, editorHeight)
        else:
            editor.setGeometry(rect)

    def setEditorData(self, editor:QWidget, index):
        if(index.column() == 0): return None
        """transfer model data to editor"""
        modelData = index.model().data(index)
        if(self.dataType == "combo"):
            if(modelData in self.dataList):
                setIndex = self.dataList.index(modelData)
            else:
                setIndex = 0
            editor.blockSignals(True)
            editor.setCurrentIndex(setIndex)
            editor.blockSignals(False)
        elif(self.dataType == "spin"):
            editor.blockSignals(True)
            editor.setValue(int(modelData))
            editor.blockSignals(False)
        elif(self.dataType == "dspin"):
            editor.blockSignals(True)
            editor.setValue(float(modelData))
            editor.blockSignals(False)
        elif(self.dataType == "3dspin"):
            modelData = modelData[1:-1]
            dir = modelData.split(',')
            data = []
            for _ in dir:
                data.append(float(_))
            data.append(0)
            editor.blockSignals(True)
            editor.setData(data)
            editor.blockSignals(False)
        elif(self.dataType in ["dir-1","dir-2"]):
            combolist = ["random","random grain"]
            if(modelData in combolist):
                index = combolist.index(modelData)
                editor.blockSignals(True)
                editor.setData(index)
                editor.blockSignals(False)
            else:
                modelData = modelData[1:-1]
                dir = modelData.split(',')
                data = []
                for _ in dir:    data.append(float(_))
                data.append(editor.maxComboID)
                editor.blockSignals(True)
                editor.setData(data)
                editor.blockSignals(False)
        elif(self.dataType in ["text"]):
            text = ""  if(modelData == self.placeholder) else modelData
            editor.blockSignals(True)
            editor.setText(text)
            editor.blockSignals(False)
        elif(self.dataType in Settings.UNIT_LIST):
            editor.setData(modelData)
            editor.blockSignals(False)
        else: return
   
    def setModelData(self, editor, model, index):
        if(index.column() == 0): return None
        """transfer editor data to model"""
        if(self.dataType == "combo"):
            editorData = self.dataList[editor.currentIndex()]
            model.setData(index, editorData)
            if(index.parent().data() == "Anisotropy"):
                dirIndex = index.siblingAtRow(2)
                dirItem = model.itemFromIndex(dirIndex)
                dirItem.setEnabled(editorData not in ["Neel","Lattice"])

        elif(self.dataType in ["spin", "dspin"]):
            model.setData(index, editor.value())
        elif(self.dataType in ["3dspin","dir-1","dir-2"]):
            if not editor.cancel:
                model.setData(index, editor.getData())
        elif(self.dataType in ["text"]):
            data = self.placeholder if(editor.text() == "") else editor.text()
            model.setData(index, data)
        elif(self.dataType in Settings.UNIT_LIST):
            if not editor.cancel:
                model.setData(index, editor.getData())

class DirPopWindow(QDialog):
    def __init__(self,parent:QWidget,dataType:str ="3dspin"):
        super().__init__(parent)
        self.ui = Ui_direction_pop()
        self.ui.setupUi(self)
        self.defaultData = [ 0.0, 0.0, 1.0, 0]
        self.setData(self.defaultData)
        self.cancel = False
        self.dataType = dataType
        self.__initUI()
        self.show()

    def __initUI(self):
        if(self.dataType == "3dspin"):
            self.ui.combobox.hide()
        elif(self.dataType == "dir-1"):
            self.ui.combobox.show()
            self.ui.combobox.removeItem(1)
            self.ui.frame.setEnabled(False)
        elif(self.dataType == "dir-2"):
            self.ui.combobox.show()
            self.ui.frame.setEnabled(False)
        self.maxComboID = self.ui.combobox.count()-1
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.confirm_button.clicked.connect(self.confirmClick)
        self.ui.discard_button.clicked.connect(self.discardClick)
        self.ui.reset_button.clicked.connect(lambda : self.setData(self.defaultData))
        self.ui.combobox.currentIndexChanged.connect(self.comboChange)
    def confirmClick(self):
        self.cancel = False
        self.close()    
    def discardClick(self):
        self.cancel = True
        self.close()
    def comboChange(self, index:int):
        switch = (index == self.maxComboID)
        self.ui.frame.setEnabled(switch)
    def setData(self,data):
        if type(data) is int:
            self.data[3] = data
            self.ui.combobox.setCurrentIndex(self.data[3])
        elif type(data) is list:
            self.data = data
            self.ui.dir_x.setValue(self.data[0])
            self.ui.dir_y.setValue(self.data[1])
            self.ui.dir_z.setValue(self.data[2])
            self.ui.combobox.setCurrentIndex(self.data[3])
    def getData(self):
        x = round(self.ui.dir_x.value(),3)
        y = round(self.ui.dir_y.value(),3)
        z = round(self.ui.dir_z.value(),3)
        comboID = self.ui.combobox.currentIndex()
        if(self.dataType == "3dspin"):
            return "["+str(x)+","+str(y)+","+str(z)+"]"
        elif(self.dataType == "dir-1"):
            if(comboID == 0):    return "random"
            return "["+str(x)+","+str(y)+","+str(z)+"]"
        elif(self.dataType == "dir-2"):
            if(comboID == 0):    return "random"
            elif(comboID == 1):  return "random grain"
            return "["+str(x)+","+str(y)+","+str(z)+"]"

class UnitPopWindow(QDialog):
    def __init__(self,parent:QWidget,unitType:str="energy",defaultData:str="0"):
        super().__init__(parent)
        self.ui = Ui_exp_unit_pop()
        self.ui.setupUi(self)

        self.unitType = unitType
        self.cancel = False
        self.defaultData = defaultData
        self.setData(self.defaultData)
        self.__initUI()

    def __textToData(self, text:str):
        # handeling the unit part
        withUnit = text.split(' ')
        try:
            unit = withUnit[1]
            comboID = Settings.UNIT_LIST[self.unitType].index(unit)
        except:
            comboID = 0
        # handeling the value part
        value = float(withUnit[0])
        exp = int(floor(log10(abs(value)))) if value != 0 else 0
        sig = value/10**exp
        return [sig, exp, comboID]
    def __initUI(self):
        self.ui.combobox.addItems(Settings.UNIT_LIST[self.unitType])
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.confirm_button.clicked.connect(self.confirmClick)
        self.ui.discard_button.clicked.connect(self.discardClick)
        self.ui.reset_button.clicked.connect(lambda : self.setData(self.defaultData))
    def setData(self,text:str):
        data = self.__textToData(text)
        self.ui.sig.setValue(data[0])
        self.ui.exp.setValue(data[1])
        self.ui.combobox.setCurrentIndex(data[2])
    def getData(self):
        sig = self.ui.sig.value()
        exp = self.ui.exp.value()
        comboID = self.ui.combobox.currentIndex()
        value = sig*(10**exp)
        if (abs(exp) <= 4):
            valuestr = str(round(value,4)) if value!=0 else "0"
        else:
            valuestr = "{:.3e}".format(value)
        return valuestr+"    "+Settings.UNIT_LIST[self.unitType][comboID]
    def confirmClick(self):
        self.cancel = False
        self.close()
    def discardClick(self):
        self.cancel = True
        self.close()
