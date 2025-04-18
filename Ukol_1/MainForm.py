# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# IMPORTANT: LLM was used for debugging and fixing errors in the code and in helping converting own pseudocode to python
from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from Algorithms import *
import os

algorithms = Algorithms()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 695)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalyze = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        
        if not os.path.exists("images/icons"):
            os.makedirs("images/icons", exist_ok=True)
        
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        if os.path.exists("images/icons/open_file.png"):
            icon.addPixmap(QtGui.QPixmap("images/icons/open_file.png"), 
                         QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        if os.path.exists("images/icons/exit.png"):
            icon1.addPixmap(QtGui.QPixmap("images/icons/exit.png"), 
                          QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        
        self.actionClear = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        if os.path.exists("images/icons/clear_all.png"):
            icon3.addPixmap(QtGui.QPixmap("images/icons/clear_all.png"), 
                          QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon3)
        self.actionClear.setObjectName("actionClear")
        
        self.actionRay_Crossing_Algorithm = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        if os.path.exists("images/icons/ray.png"):
            icon4.addPixmap(QtGui.QPixmap("images/icons/ray.png"), 
                          QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRay_Crossing_Algorithm.setIcon(icon4)
        self.actionRay_Crossing_Algorithm.setObjectName("actionRay_Crossing_Algorithm")
        
        self.actionWinding_Number_Algorithm = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        if os.path.exists("images/icons/winding.png"):
            icon5.addPixmap(QtGui.QPixmap("images/icons/winding.png"), 
                          QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWinding_Number_Algorithm.setIcon(icon5)
        self.actionWinding_Number_Algorithm.setObjectName("actionWinding_Number_Algorithm")
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionRay_Crossing_Algorithm)
        self.menuAnalyze.addAction(self.actionWinding_Number_Algorithm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRay_Crossing_Algorithm)
        self.toolBar.addAction(self.actionWinding_Number_Algorithm)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.actionOpen.triggered.connect(self.openClick)
        self.actionClear.triggered.connect(self.clearClick)
        self.actionRay_Crossing_Algorithm.triggered.connect(self.rayCrossingClick)
        self.actionWinding_Number_Algorithm.triggered.connect(self.windingNumberClick)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openClick(self):
        if self.Canvas.loadData():
            self.statusbar.showMessage("File loaded successfully", 5000)
        else:
            self.statusbar.showMessage("Failed to load file or user cancelled", 5000)

    def resizeDisplay(self):
        self.Canvas.resizeData()
        self.Canvas.repaint()

    def clearClick(self):
        self.Canvas.clearAll()
        self.statusbar.showMessage("Data cleared", 3000)

    def _display_analysis_result(self, result_value, containing_polygon, algorithm_name):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle(f'Result of analysis ({algorithm_name})')

        if result_value == 1:
            message = ''
            status_msg = "Result: Inside"
            label = "inside"
        elif result_value == 0:
            message = 'Point lies outside all polygons'
            status_msg = "Result: Outside"
            label = None
        elif result_value == -1:
            message = 'Point is ON the edge/vertex of at least one polygon'
            status_msg = "Result: On edge/vertex"
            label = "on the edge/vertex of"
            
        if containing_polygon and label:
            message += f"\n\nThe point is {label} the following polygon:"
            
            for i, attrs in enumerate(containing_polygon):
                if not attrs:
                    continue
                    
                important_attrs = ['NAME', 'Name', 'name', 'ID', 'Id', 'id', 'LABEL', 'Label', 'label'] 
                sorted_attrs = {}
                
                for key in important_attrs:
                    if key in attrs:
                        sorted_attrs[key] = attrs[key]
                
                for key, value in attrs.items():
                    if key not in sorted_attrs:
                        sorted_attrs[key] = value
                
                attrs_added = 0
                for key, value in sorted_attrs.items():
                    if attrs_added < 5:
                        message += f"\n  {key}: {value}"
                        attrs_added += 1
                    else:
                        remaining = len(attrs) - 5
                        if remaining > 0:
                            message += f"\n  ... ({remaining} more attributes not shown)"
                        break
                    
            if len(containing_polygon) > 1:
                message += f"\n\nTotal polygons: {len(containing_polygon)}"
        
        self.statusbar.showMessage(status_msg, 5000)
        dialog.setText(message)
        dialog.exec()

    def rayCrossingClick(self):
        q = self.Canvas.getQ()
        polygons = self.Canvas.getPols()

        if not polygons:
            self.statusbar.showMessage("No polygons available - load a shapefile first", 3000)
            return

        results, containing_polygon = algorithms.ray_crossing_pols(q, polygons)

        if not results:
            self.statusbar.showMessage("Analysis failed", 3000)
            return

        self.Canvas.setResult(results[0])
        self.Canvas.setContainingPolygons(containing_polygon)
        self.Canvas.repaint()
        self._display_analysis_result(results[0], containing_polygon, "Ray Crossing")

    def windingNumberClick(self):
        q = self.Canvas.getQ()
        polygons = self.Canvas.getPols()

        if not polygons:
            self.statusbar.showMessage("No polygons available - load a shapefile first", 3000)
            return

        results, containing_polygon = algorithms.winding_number_pols(q, polygons)

        if not results:
            self.statusbar.showMessage("Analysis failed", 3000)
            return

        self.Canvas.setResult(results[0])
        self.Canvas.setContainingPolygons(containing_polygon)
        self.Canvas.repaint()
        self._display_analysis_result(results[0], containing_polygon, "Winding Number")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear data"))
        self.actionRay_Crossing_Algorithm.setText(_translate("MainWindow", "Ray Crossing Algorithm"))
        self.actionWinding_Number_Algorithm.setText(_translate("MainWindow", "Winding Number Algorithm"))


if __name__ == "__main__":#
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())