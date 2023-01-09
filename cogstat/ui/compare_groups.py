# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compare_groups.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 434)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.source_listWidget = QtWidgets.QListWidget(Dialog)
        self.source_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.source_listWidget.setObjectName("source_listWidget")
        self.verticalLayout_3.addWidget(self.source_listWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.addVar = QtWidgets.QToolButton(Dialog)
        self.addVar.setArrowType(QtCore.Qt.RightArrow)
        self.addVar.setObjectName("addVar")
        self.verticalLayout_2.addWidget(self.addVar)
        self.removeVar = QtWidgets.QToolButton(Dialog)
        self.removeVar.setArrowType(QtCore.Qt.LeftArrow)
        self.removeVar.setObjectName("removeVar")
        self.verticalLayout_2.addWidget(self.removeVar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.add_group_button = QtWidgets.QToolButton(Dialog)
        self.add_group_button.setArrowType(QtCore.Qt.RightArrow)
        self.add_group_button.setObjectName("add_group_button")
        self.verticalLayout_2.addWidget(self.add_group_button)
        self.remove_group_button = QtWidgets.QToolButton(Dialog)
        self.remove_group_button.setArrowType(QtCore.Qt.LeftArrow)
        self.remove_group_button.setObjectName("remove_group_button")
        self.verticalLayout_2.addWidget(self.remove_group_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.selected_listWidget = QtWidgets.QListWidget(Dialog)
        self.selected_listWidget.setEnabled(True)
        self.selected_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selected_listWidget.setObjectName("selected_listWidget")
        self.verticalLayout.addWidget(self.selected_listWidget)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.group_listWidget = QtWidgets.QListWidget(Dialog)
        self.group_listWidget.setEnabled(True)
        self.group_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.group_listWidget.setObjectName("group_listWidget")
        self.verticalLayout.addWidget(self.group_listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.label.setBuddy(self.source_listWidget)
        self.label_2.setBuddy(self.selected_listWidget)
        self.label_3.setBuddy(self.group_listWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.source_listWidget, self.addVar)
        Dialog.setTabOrder(self.addVar, self.removeVar)
        Dialog.setTabOrder(self.removeVar, self.selected_listWidget)
        Dialog.setTabOrder(self.selected_listWidget, self.add_group_button)
        Dialog.setTabOrder(self.add_group_button, self.remove_group_button)
        Dialog.setTabOrder(self.remove_group_button, self.group_listWidget)
        Dialog.setTabOrder(self.group_listWidget, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Compare groups"))
        self.label.setText(_translate("Dialog", "Available variables"))
        self.label_2.setText(_translate("Dialog", "Dependent variable(s)"))
        self.label_3.setText(_translate("Dialog", "Group(s)"))
        self.pushButton_2.setText(_translate("Dialog", "O&ptions..."))
        self.pushButton_3.setText(_translate("Dialog", "&Display groups..."))
        self.pushButton.setText(_translate("Dialog", "Single case &slope..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
