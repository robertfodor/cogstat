# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pivot.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(583, 536)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.sourceListWidget = QtWidgets.QListWidget(Dialog)
        self.sourceListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.sourceListWidget.setObjectName("sourceListWidget")
        self.verticalLayout_2.addWidget(self.sourceListWidget)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 4, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.addPages = QtWidgets.QToolButton(Dialog)
        self.addPages.setArrowType(QtCore.Qt.RightArrow)
        self.addPages.setObjectName("addPages")
        self.verticalLayout.addWidget(self.addPages)
        self.removePages = QtWidgets.QToolButton(Dialog)
        self.removePages.setArrowType(QtCore.Qt.LeftArrow)
        self.removePages.setObjectName("removePages")
        self.verticalLayout.addWidget(self.removePages)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.pagesListWidget = QtWidgets.QListWidget(Dialog)
        self.pagesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pagesListWidget.setObjectName("pagesListWidget")
        self.gridLayout.addWidget(self.pagesListWidget, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.addColumns = QtWidgets.QToolButton(Dialog)
        self.addColumns.setArrowType(QtCore.Qt.RightArrow)
        self.addColumns.setObjectName("addColumns")
        self.verticalLayout_3.addWidget(self.addColumns)
        self.removeColumns = QtWidgets.QToolButton(Dialog)
        self.removeColumns.setArrowType(QtCore.Qt.LeftArrow)
        self.removeColumns.setObjectName("removeColumns")
        self.verticalLayout_3.addWidget(self.removeColumns)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.columnsListWidget = QtWidgets.QListWidget(Dialog)
        self.columnsListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.columnsListWidget.setObjectName("columnsListWidget")
        self.gridLayout_2.addWidget(self.columnsListWidget, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.addRows = QtWidgets.QToolButton(Dialog)
        self.addRows.setArrowType(QtCore.Qt.RightArrow)
        self.addRows.setObjectName("addRows")
        self.verticalLayout_6.addWidget(self.addRows)
        self.removeRows = QtWidgets.QToolButton(Dialog)
        self.removeRows.setArrowType(QtCore.Qt.LeftArrow)
        self.removeRows.setObjectName("removeRows")
        self.verticalLayout_6.addWidget(self.removeRows)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.rowsListWidget = QtWidgets.QListWidget(Dialog)
        self.rowsListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rowsListWidget.setObjectName("rowsListWidget")
        self.gridLayout_4.addWidget(self.rowsListWidget, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.addDependent = QtWidgets.QToolButton(Dialog)
        self.addDependent.setArrowType(QtCore.Qt.RightArrow)
        self.addDependent.setObjectName("addDependent")
        self.verticalLayout_5.addWidget(self.addDependent)
        self.removeDependent = QtWidgets.QToolButton(Dialog)
        self.removeDependent.setArrowType(QtCore.Qt.LeftArrow)
        self.removeDependent.setObjectName("removeDependent")
        self.verticalLayout_5.addWidget(self.removeDependent)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.dependentListWidget = QtWidgets.QListWidget(Dialog)
        self.dependentListWidget.setObjectName("dependentListWidget")
        self.gridLayout_3.addWidget(self.dependentListWidget, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)
        self.function = QtWidgets.QComboBox(Dialog)
        self.function.setObjectName("function")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.gridLayout_3.addWidget(self.function, 3, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_5.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.label.setBuddy(self.sourceListWidget)
        self.label_4.setBuddy(self.pagesListWidget)
        self.label_3.setBuddy(self.columnsListWidget)
        self.label_2.setBuddy(self.rowsListWidget)
        self.label_5.setBuddy(self.dependentListWidget)
        self.label_6.setBuddy(self.function)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pivot table"))
        self.label.setText(_translate("Dialog", "Available variables"))
        self.label_4.setText(_translate("Dialog", "Page(s)"))
        self.label_3.setText(_translate("Dialog", "Column(s)"))
        self.label_2.setText(_translate("Dialog", "Row(s)"))
        self.label_5.setText(_translate("Dialog", "Dependent variable(s)"))
        self.label_6.setText(_translate("Dialog", " &Function"))
        self.function.setItemText(0, _translate("Dialog", "N"))
        self.function.setItemText(1, _translate("Dialog", "Sum"))
        self.function.setItemText(2, _translate("Dialog", "Mean"))
        self.function.setItemText(3, _translate("Dialog", "Median"))
        self.function.setItemText(4, _translate("Dialog", "Lower quartile"))
        self.function.setItemText(5, _translate("Dialog", "Upper quartile"))
        self.function.setItemText(6, _translate("Dialog", "Standard deviation"))
        self.function.setItemText(7, _translate("Dialog", "Variance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
