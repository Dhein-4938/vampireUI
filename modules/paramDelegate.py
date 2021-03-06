from modules import *
from . dirpop import *
from . unitpop import *
from . rangepop import *
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
        elif(self.dataType == "text"):
            self.placeholder = "(filename)"
            lineEdit = QLineEdit(parent)
            lineEdit.setObjectName("editor")
            lineEdit.setStyleSheet(Settings.LINEEDIT_STYLESHEET)
            return lineEdit
        elif(self.dataType in ["3dspin","dir-1","dir-2"]):
            return DirPopWindow(parent,self.dataType)
        elif(self.dataType in Settings.UNIT_LIST):
            return UnitPopWindow(parent,self.dataType,self.paramData[1])
        elif(self.dataType in ["angle", "temp"]):
            return RangePopWindow(parent,self.dataType,self.paramData[1])
        return None
    
    def updateEditorGeometry(self, editor:QWidget, option:QStyleOptionViewItem, index:QModelIndex):
        if(index.column() == 0): return None
        rect = option.rect
        if(self.dataType in ["3dspin","dir-1","dir-2","angle", "temp"] or self.dataType in Settings.UNIT_LIST):
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
        elif(self.dataType in ["text"]):
            text = ""  if(modelData == self.placeholder) else modelData
            editor.blockSignals(True)
            editor.setText(text)
            editor.blockSignals(False)
        elif(self.dataType in ["3dspin","dir-1","dir-2"]):
            editor.blockSignals(True)
            editor.setData(modelData)
            editor.blockSignals(False)
        elif(self.dataType in Settings.UNIT_LIST):
            editor.blockSignals(True)
            editor.setData(modelData)
            editor.blockSignals(False)
        elif(self.dataType in ["angle","temp"]):
            editor.blockSignals(True)
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
        elif(self.dataType in ["text"]):
            data = self.placeholder if(editor.text() == "") else editor.text()
            model.setData(index, data)
        elif(self.dataType in ["3dspin","dir-1","dir-2"]):
            if not editor.cancel:
                model.setData(index, editor.getData())
        elif(self.dataType in Settings.UNIT_LIST):
            if not editor.cancel:
                model.setData(index, editor.getData())
        elif(self.dataType in ["angle","temp"]):
            if not editor.cancel:
                model.setData(index, editor.getData())

class PopupWindow(QDialog):
    def __init__(self, parent:QWidget, uifile = None, dataType:str = "none", defaultData = 0):
        super().__init__(parent)
        
        self.ui = uifile
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # ---------- initialize instances ----------
        self.cancel = False
        self.dataType = dataType
        self.defaultData = defaultData
        self.data = self.defaultData[:]
        # ---------- set three dialog button click function ----------
        self.ui.confirm_button.clicked.connect(lambda: self.btnClick(False))
        self.ui.discard_button.clicked.connect(lambda: self.btnClick(True))
        self.ui.reset_button.clicked.connect(lambda : self.setData(""))
        # ---------- set default data ----------
        self.setData("")
    
    def setData(self,text):
        pass

    def btnClick(self, cancel = True):
        self.cancel = cancel
        self.close()

class DirPopWindow(PopupWindow):
    def __init__(self, parent:QWidget, dataType:str ="3dspin"):
        super().__init__(parent, Ui_direction_pop(), dataType, defaultData=[ 0.0, 0.0, 1.0, 0])
        self.init_UI()
        self.switchUI()
        self.show()
    
    def init_UI(self):
        self.maxComboID = self.ui.combobox.count()-1
        self.ui.combobox.currentIndexChanged.connect(lambda index: self.ui.frame.setEnabled((index == self.maxComboID)))

    def switchUI(self):
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

    def __textToData(self, text:str = ""):
        """ Return: True => set all data,  False => set only combobox data"""
        # ---------- set default data if text is empty ----------
        if text == "":
            self.data = self.defaultData[:]
            return True
        combolist = ["random","random grain"]
        try:
            self.data[3] = combolist.index(text)
            return False
        except ValueError:
            text = text[1:-1]
            dir = text.split(',')
            self.data = [float(dir[0]), float(dir[1]),float(dir[2]), self.maxComboID]
            return True

    def setData(self,text):
        setAll = self.__textToData(text)
        if setAll:
            self.ui.dir_x.setValue(self.data[0])
            self.ui.dir_y.setValue(self.data[1])
            self.ui.dir_z.setValue(self.data[2])
        self.ui.combobox.setCurrentIndex(self.data[3])
        
    def getData(self):
        # ---------- check the combo box index for non-specific direction ----------
        comboID = self.ui.combobox.currentIndex()
        if(self.dataType == "dir-1"):
            if(comboID == 0):    return "random"
        elif(self.dataType == "dir-2"):
            if(comboID == 0):    return "random"
            elif(comboID == 1):  return "random grain"
        # ---------- output specific direction ----------
        x = round(self.ui.dir_x.value(),3)
        y = round(self.ui.dir_y.value(),3)
        z = round(self.ui.dir_z.value(),3)
        dirStr = "["+str(x)+","+str(y)+","+str(z)+"]"
        return dirStr

class UnitPopWindow(PopupWindow):
    def __init__(self,parent:QWidget,dataType:str="energy",initValue:str="0"):
        initSig, initExp = self.splitSigExp(float(initValue))
        super().__init__(parent, Ui_exp_unit_pop(), dataType, [initSig, initExp, 0])
        self.init_UI()
        self.show()
        
    def init_UI(self):
        self.ui.combobox.addItems(Settings.UNIT_LIST[self.dataType])

    def splitSigExp(self, value:float = 0.0):
        exp = int(floor(log10(abs(value)))) if value != 0 else 0
        sig = value/10**exp
        return sig, exp

    def __textToData(self, text:str):
        if text == "":
            self.data = self.defaultData[:]
            return
        # ---------- handeling the unit part ----------
        splitList = text.split('    ')
        number = splitList[0]
        if len(splitList) == 1:
            unit = Settings.UNIT_LIST[self.dataType][0]
        else:
            unit = splitList[1]
        try:
            comboID = Settings.UNIT_LIST[self.dataType].index(unit)
        except:
            comboID = 0
        # ---------- handeling the value part ----------
        sig, exp = self.splitSigExp(float(number))
        self.data = [sig, exp, comboID]

    def setData(self,text:str):
        self.__textToData(text)
        self.ui.sig.setValue(self.data[0])
        self.ui.exp.setValue(self.data[1])
        self.ui.combobox.setCurrentIndex(self.data[2])

    def getData(self):
        sig = self.ui.sig.value()
        exp = self.ui.exp.value()
        comboID = self.ui.combobox.currentIndex()
        value = sig*(10**exp)
        if (abs(exp) <= 4):
            valuestr = str(round(value,4)) if value!=0 else "0"
        else:
            valuestr = "{:.3e}".format(value)
        return valuestr+"    "+Settings.UNIT_LIST[self.dataType][comboID]

class RangePopWindow(PopupWindow):
    def __init__(self,parent:QWidget,dataType:str="temp",maxlimit:str="360"):
        super().__init__(parent, Ui_range_pop(), dataType, [0.0, [0.0, 0.0, 0.0]])
        self.min = 0
        self.max = int(maxlimit)
        self.init_UI()
        self.switchUI()
        self.show()
    
    def init_UI(self):
        self.pages = [self.ui.set, self.ui.range]
        # ---------- set to default page --------
        self.setPage(0)
        self.ui.combobox.currentIndexChanged.connect(lambda index: self.setPage(index))

    def setPage(self, page):
        self.ui.stackedWidget.setCurrentWidget(self.pages[page])

    def switchUI(self):
        if self.dataType == "angle":
            self.unit = "??"
            self.ui.plus_label.show()
            self.ui.incre_value.show()
            self.spinParam = [3, self.min, self.max, 0.01]
        else:
            self.unit = "T"
            self.ui.plus_label.hide()
            self.ui.incre_value.hide()
            self.spinParam = [1, self.min, self.max, 1]
        self.ui.set_unit.setText(self.unit)
        self.setdspinRange([self.ui.set_value, self.ui.min_value, self.ui.max_value, self.ui.incre_value], self.spinParam)

    @staticmethod
    def setdspinRange(dspinList,rangeList):
        decimal, minimum, maximum, step = rangeList
        for dspin in dspinList:
            dspin.setDecimals(decimal)
            dspin.setRange(minimum, maximum)
            dspin.setSingleStep(step)
            dspin.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
    
    def __textToData(self, text:str):
        """data format: 180, 45~60, 10~20  +5"""
        if text == "":
            self.data = self.defaultData[:]
        elif '+' in text:
            minmax, incre = text.split("  +")
            minValue, maxValue = minmax.split("~")
            self.data[1] = [float(minValue), float(maxValue), float(incre)]
            self.setPage(1)
            self.ui.combobox.setCurrentIndex(1)
        elif '~' in text:
            minValue, maxValue = text.split("~")
            self.data[1] = [float(minValue), float(maxValue), 0.0]
            self.setPage(1)
            self.ui.combobox.setCurrentIndex(1)
        else:
            self.data[0] = float(text)

    def setData(self,text):
        self.__textToData(text)
        self.ui.set_value.setValue(self.data[0])
        self.ui.min_value.setValue(self.data[1][0])
        self.ui.max_value.setValue(self.data[1][1])
        self.ui.incre_value.setValue(self.data[1][2])

    def getData(self):
        setValue = self.ui.set_value.value()
        minValue = self.ui.min_value.value()
        maxValue = self.ui.max_value.value()
        increValue = self.ui.incre_value.value()
        pageID = self.ui.combobox.currentIndex()
        if minValue > maxValue:
            minValue, maxValue = maxValue, minValue
        if self.dataType == "angle":
            if pageID == 0:
                return str(setValue)
            else:
                return str(minValue)+"~"+str(maxValue)+"  +"+str(increValue)
        else:
            if pageID == 0:
                return str(setValue)
            else:
                if minValue == maxValue:    return str(minValue)
                else: return str(minValue)+"~"+str(maxValue)
