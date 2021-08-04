from main import MainWindow
from modules import *

TITLE_COLUMN_WIDTH = 300
PARAM_COLUMN_WIDTH = 170

PRE_ROW_SHIFT = 3
DEFAULT_MATERIAL_NAME = "(name)"
DEFAULT_JMOL_ELEMENT = "(element)"
NO_SELECT_TITLE = "----------------------"

class TreeObject:
    def __init__(self,item):
        self.item = item
        self.childList = []
    def appendChild(self, child):
        self.childList.append(child)
    def child(self,index):
        if len(self.childList) == 0: return None
        return self.childList[index]
    def children(self):
        return self.childList

def setHeader(textlist:list[str], model:QStandardItemModel, alignment="center"):
    """set header item for the treeview model"""
    for index in range(len(textlist)):
        header = ChooseItem(textlist[index], order=0)
        if (alignment == "center"):
            header.setTextAlignment(Qt.AlignCenter)
        elif(alignment == "left"):
            header.setTextAlignment(Qt.AlignLeft)
        elif(alignment == "right"):
            header.setTextAlignment(Qt.AlignRight)
        model.setHorizontalHeaderItem(index,header)

def createGroupModel(treeview:QTreeView, groupModel:QStandardItemModel):
    """creating the treeview model"""
    for catName in Settings.MATERIAL_SETUP.keys():
        catItem = ChooseItem(catName, order=1)
        for groupName in Settings.MATERIAL_SETUP[catName].keys():
            catItem.appendRow(ChooseItem(groupName, order=2))
        groupModel.invisibleRootItem().appendRow(catItem)
    treeview.setModel(groupModel)
    treeview.expandAll()

def createInputItem(itemlist:list):
        itemType = itemlist[0]
        if(itemType in ["combo","dir-1","dir-2","combo dspin"]):
            item = ParamItem(itemlist[1][0], SelectEdit=True)
        elif(itemType in ["spin","dspin","3dspin"]):
            item = ParamItem(itemlist[1], SelectEdit=True)
        elif(itemType in ["text"]):
            item = ParamItem("(filename)", SelectEdit=True)
        elif(itemType in Settings.UNIT_LIST):
            unit = Settings.UNIT_LIST[itemType][0]
            name = itemlist[1]+"    "+unit
            item = ParamItem(name, SelectEdit=True)
        elif(itemType == "none"):
            item = ParamItem("", SelectEdit=True)
            item.setCheckable(True)
            return item
        elif(itemType in ["angle","temp"]):
            item = ParamItem("0", SelectEdit=True)
        elif(itemType == "exchange"):
            item = ParamItem("Exchang Matrix", SelectEdit=True)
        else:
            item = ParamItem("ERROR")
        return item

def createColumnItems(num, titleItem, createFunction):
    itemList = [titleItem]
    for _ in range(num):
        item = createFunction()
        itemList.append(item)
    return itemList


# PAGE CUSTOM DEFINITION
# ///////////////////////////////////////////////////////////////
class Material(MainWindow):

    def initLeftTree(self):
        """initialize the left treeview"""
        treeview = self.ui.left_tree
        treeview.setHeaderHidden(False)
        setHeader(["All Parameters"],self.LgroupModel)
        createGroupModel(treeview, self.LgroupModel)
        
    def initRightTree(self):
        """initialize the right treeview"""
        treeview = self.ui.right_tree
        treeview.setHeaderHidden(False)
        setHeader(["Used Parameters"],self.RgroupModel)
        createGroupModel(treeview, self.RgroupModel)
        # hide all rows
        for _ in range(len(Settings.MATERIAL_SETUP)):
            treeview.setRowHidden(_,self.RgroupRootItem.index(),True)
    
    def displayRows(self, catID:int,groupID=-1,setBool=True):
        """
        Usage : hide or show row(s) on the treeview
        """
        treeview = self.ui.right_tree
        """collecting group state"""
        # check if the state(s) is equal to setBool
        if(groupID == -1):
            if setBool: checkState = all(self.groupState[catID])
            else      : checkState = not any(self.groupState[catID])
        else:              checkState = ( self.groupState[catID][groupID] == setBool)
        # Exit function because no change is needed
        if checkState:    return False
        """showing or hiding group(s)"""
        if(groupID == -1):    self.groupState[catID] = [setBool]*len(self.groupState[catID])
        else:                 self.groupState[catID][groupID] = setBool
        # diaplay group row as state
        catItem = self.RgroupRootItem.child(catID)
        for index, state in enumerate(self.groupState[catID]):
            treeview.setRowHidden(index,catItem.index(),not state)
        """showing or hiding category"""
        if setBool:
            self.catState[catID] = True
            treeview.setRowHidden(catID,self.RgroupRootItem.index(),False)
        elif not any(self.groupState[catID]):
            # check for empty category
            self.catState[catID] = False
            treeview.setRowHidden(catID,self.RgroupRootItem.index(),True)

    def displayItem(self, input, setBool=True):    #item = QModelIndex
        if (type(input) is list):     # input from button
            if(len(input)==0): return       # prevent no selection
            item = input[0]
        else:                         # input from double clicking
            item = input
            
        def findRootRows(node:QModelIndex):
            """
            Usage : find the rows of an item and its parent(s)
            """
            path = []
            def findParentRow(node):
                path.append(node.row())
                if(node.parent().data() != None):   findParentRow(node.parent())
            findParentRow(node)
            return path

        rootRows = findRootRows(item)
        catRow = rootRows.pop()
        if(len(rootRows) == 1):
            groupRow = rootRows.pop()
            Material.displayRows(self, catRow, groupRow, setBool=setBool)
        else:
            Material.displayRows(self, catRow,           setBool=setBool)

    def disableParam(self, index:QModelIndex):
        item = self.paramSetModel.itemFromIndex(index)
        itemColumn = index.column()
        """only consider the title double click event"""
        if(itemColumn != 0): return
        """item with no childer => with input"""
        if(not item.hasChildren()):
            maxColumn = self.paramSetModel.columnCount()
            itemFont = item.font()
            state = itemFont.strikeOut()
            itemFont.setStrikeOut(not state)
            item.setFont(itemFont)
            for column in range(1,maxColumn):
                siblingItem = self.paramSetModel.itemFromIndex(index.siblingAtColumn(column))
                siblingItem.setEnabled(state)
                siblingItemFont = siblingItem.font()
                siblingItemFont.setStrikeOut(not state)
                siblingItem.setFont(siblingItemFont)

    def initParamSetTree(self):
        treeview = self.ui.param_set_tree
        amount = self.materialAmount
        # adding ID, material name, jmol element items (rows)
        idTitle = ParamItem("ID")
        matNameTitle = ParamItem("Material Name")
        jmolNameTitle = ParamItem("Jmol Element")
        idItemList = [idTitle]
        matNameItemList = [matNameTitle]
        jmolNameItemList = [jmolNameTitle]
        for id in range(amount):
            idItem = ParamItem(str(id+1))
            idItemList.append(idItem)
            matNameItem = ParamItem(DEFAULT_MATERIAL_NAME, SelectEdit=True)
            matNameItemList.append(matNameItem)
            jmolNameItem = ParamItem(DEFAULT_JMOL_ELEMENT, SelectEdit=True)
            jmolNameItemList.append(jmolNameItem)
        self.paramRootItem.appendRow(idItemList)
        self.paramRootItem.appendRow(matNameItemList)
        self.paramRootItem.appendRow(jmolNameItemList)

        # adding parameters items (rows)
        for catName in Settings.MATERIAL_SETUP.keys():
            catItem = ParamItem(catName, order=0)
            catcolumnList = createColumnItems(amount, catItem, lambda: ParamItem(NO_SELECT_TITLE))
            for groupName in Settings.MATERIAL_SETUP[catName].keys():
                paramStructure = Settings.MATERIAL_SETUP[catName][groupName]
                if(type(paramStructure) is list):
                    groupItem = ParamItem(groupName)
                    groupItem.setSelectable(True)
                    groupcolumnList = createColumnItems(amount, groupItem,lambda: createInputItem(paramStructure))
                else:
                    groupItem = ParamItem(groupName, order=1)
                    groupcolumnList = createColumnItems(amount, groupItem, lambda: ParamItem(NO_SELECT_TITLE))
                    for paramName in paramStructure.keys():
                        paramItem = ParamItem(paramName)
                        paramItem.setSelectable(True)
                        paramcolumnList = createColumnItems(amount, paramItem, lambda: createInputItem(paramStructure[paramName]))

                        groupItem.appendRow(paramcolumnList)
                catItem.appendRow(groupcolumnList)
            self.paramRootItem.appendRow(catcolumnList)

        # set header
        for i in range(amount):
            self.paramHeader.append("Material " + str(i+1))
        setHeader(self.paramHeader,self.paramSetModel,alignment="left")
        treeview.setModel(self.paramSetModel)
        treeview.expandAll()
        # set header column width
        treeview.setColumnWidth(0, TITLE_COLUMN_WIDTH)
        # set param coulmn width
        for i in range(self.paramSetModel.columnCount()-1):
            treeview.setColumnWidth(i+1, PARAM_COLUMN_WIDTH)
        
        for catID in range(len(Settings.MATERIAL_SETUP)):
            treeview.setRowHidden(catID+PRE_ROW_SHIFT,self.paramRootItem.index(),True)
        from .paramDelegate import ParamSetDelegate
        treeview.setItemDelegate(ParamSetDelegate(self))

    def displayParamSet(self):
        """show/hide rows by states"""
        tree = self.ui.param_set_tree
        rootIndex = self.paramRootItem.index()
        for cat_id in range(len(self.catState)):
            tree.setRowHidden(cat_id+PRE_ROW_SHIFT, rootIndex, not self.catState[cat_id])
            catIndex = self.paramRootItem.child(cat_id+PRE_ROW_SHIFT).index()
            for group_id in range(len(self.groupState[cat_id])):
                tree.setRowHidden(group_id, catIndex,not self.groupState[cat_id][group_id])

    def addMaterial(self):
        if(self.currentMaterialAmount < 12):
            self.currentMaterialAmount += 1
            self.ui.total_mat_label.setText("Total Material Amount: " + str(self.currentMaterialAmount))

    def removeMaterial(self):
        if(self.currentMaterialAmount > 0):
            self.currentMaterialAmount -= 1
            self.ui.total_mat_label.setText("Total Material Amount: " + str(self.currentMaterialAmount))

    def translateToDisplay(self):
        """translate param page's data to display page"""
        maxColumn = self.currentMaterialAmount
        tree = self.ui.param_set_tree
        model = self.paramSetModel
        rootItem = self.paramRootItem
        note = self.ui.mat_display
        note.clear()
        # pre-define variable
        prefix = ""
        column = 1
        def display(selector, titleItem):
            index = titleItem.index().siblingAtColumn(column)
            item = model.itemFromIndex(index)

            # No diaplay when item is disabled
            if not item.isEnabled():    return 

            text = str(index.data())
            # ---------- checkbox items ----------
            if(len(text) == 0):
                # don't show the text when the checkbox is unchecked
                if(item.checkState() == Qt.Unchecked):
                    return 
                text = str(index.data())
            # ---------- direction items ----------
            elif(text[0] == '['):
                text = text[1:-1].replace( ',' , ' ' )
            # ---------- default input items ----------
            elif(text in ["(name)","(element)","(filename)"]):
                text = "<font color=red>Missing Input</font>"
            # ---------- unit items ----------
            elif("  " in text):
                text = text.replace("    " , " !")
            
            note.append(prefix + ": " + selector + " = " + text)

        def coulmnDisplay():
            note.append("#--------------------------------------------------------")
            note.append("#       Material "+str(column))
            note.append("#--------------------------------------------------------")
            display("material-name", rootItem.child(1))
            display("material-element", rootItem.child(2))

        def groupDisplay(catItem):
            catName = catItem.text()
            for groupID, groupName in enumerate(Settings.MATERIAL_OUTPUT[catName].keys()):
                if not self.groupState[catID][groupID]: continue
                groupItem = catItem.child(groupID)
                groupSelector = Settings.MATERIAL_OUTPUT[catName][groupName]
                if type(groupSelector) is dict:
                    paramDisplay(groupItem)
                else:
                    display(groupSelector, groupItem)

        def paramDisplay(groupItem):
            constrainedCheck = False
            groupName = groupItem.text()
            for paramID, paramName in enumerate(Settings.MATERIAL_OUTPUT[catName][groupName].keys()):
                paramSelector = Settings.MATERIAL_OUTPUT[catName][groupName][paramName]
                paramItem = groupItem.child(paramID)
                paramColumnItem = model.itemFromIndex(paramItem.index().siblingAtColumn(column))
                # ---------- Anisotropy: Type ----------
                if (groupName == "Anisotropy" and paramName == "Type"):
                    # combobox index
                    typeID = Settings.MATERIAL_SETUP["Magnetic Properties"]["Anisotropy"]["Type"][1].index(paramColumnItem.text())
                    selector = Settings.MATERIAL_OUTPUT["Magnetic Properties"]["Anisotropy"]["Type"][typeID]
                    # constant item, direction item
                    anisoTypeItem = paramColumnItem
                    anisoConstItem = groupItem.child(paramID-1)
                    anisoDirItem = groupItem.child(paramID+1)
                    # continue if type item or constant item is disabled
                    if not anisoTypeItem.isEnabled(): continue 
                    if not anisoConstItem.isEnabled(): continue
                    # display 
                    display(selector, anisoConstItem)
                    if(0<=typeID<=2): display("uniaxial-anisotropy-direction", anisoDirItem)
                    elif(3<=typeID<=4): display("cubic-anisotropy-direction", anisoDirItem)
                    else: pass # no direction needed for neel and lattice anisotropy
                # ---------- Alloy: Type ----------
                elif(groupName == "Alloy" and paramName == "Type"):
                    note.append(prefix+": alloy-host")
                    display(paramSelector, paramItem)
                # ---------- Constrained Angle ----------
                elif(groupName == "Constrained Angle" and paramName in ["Theta","Phi"]):
                    if not constrainedCheck:
                        constrainedCheck = True
                        note.append(prefix + ": constrained = true")
                    display(paramSelector, paramItem)   # //////////////NOT FINISHED///////////////
                # ---------- Temperature: Temperature ----------
                elif(groupName == "Temperature" and paramName == "Temperature"):
                    display(paramSelector, paramItem)   # //////////////NOT FINISHED///////////////
                # ---------- Exchange Properties: Exchange Matrix ----------
                elif(groupName == "Exchange Properties" and paramName == "Exchange Matrix"):
                    display(paramSelector, paramItem)   # //////////////NOT FINISHED///////////////
                # ---------- normal output ----------
                elif type(paramSelector) is str: 
                    display(paramSelector, paramItem)
                # ---------- Excluded items ----------
                elif type(paramSelector) is None:
                    pass
                else:
                    pass

        for column in range(1,maxColumn+1):
            prefix = "material[" + str(column) + "]"
            coulmnDisplay()
            for catID, catName in enumerate(Settings.MATERIAL_OUTPUT.keys()):
                if not self.catState[catID]: continue
                catItem = rootItem.child(catID+PRE_ROW_SHIFT)
                groupDisplay(catItem)
                    


class ChooseItem(QStandardItem):
    def __init__(self, txt=None, order:int =2, color=QColor(0,0,0)):
        super(ChooseItem,self).__init__()
        #fnt = QFont(Settings.FONT_FAMILY, Settings.CHOOSE_FONT_SIZE_ORDER[order])
        fnt = self.font()
        fnt.setPointSize(Settings.PARAM_FONT_SIZE_ORDER[order])
        fnt.setBold(Settings.BOLD_ORDER[order])
        fnt.setUnderline(Settings.UNDERLINE_OREDR[order])
        self.setFont(fnt)
        self.setForeground(color)
        self.setText(txt)
        self.setSelectable(True)
        self.setEditable(False)

class ParamItem(QStandardItem):
    def __init__(self, txt=None, order:int=2, color:QColor=QColor(0,0,0), SelectEdit:bool=False):
        super(ParamItem,self).__init__()
        #fnt = QFont(Settings.FONT_FAMILY, Settings.PARAM_FONT_SIZE_ORDER[order])
        fnt = self.font()
        fnt.setPointSize(Settings.PARAM_FONT_SIZE_ORDER[order])
        fnt.setBold(False)
        fnt.setUnderline(False)
        self.setFont(fnt)
        self.setForeground(color)
        self.setText(txt)
        self.setSelectable(SelectEdit)
        self.setEditable(SelectEdit)
