# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_options_repeated.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 330)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.add_color_button = QtWidgets.QToolButton(Dialog)
        self.add_color_button.setArrowType(QtCore.Qt.RightArrow)
        self.add_color_button.setObjectName("add_color_button")
        self.verticalLayout_2.addWidget(self.add_color_button)
        self.remove_color_button = QtWidgets.QToolButton(Dialog)
        self.remove_color_button.setArrowType(QtCore.Qt.LeftArrow)
        self.remove_color_button.setObjectName("remove_color_button")
        self.verticalLayout_2.addWidget(self.remove_color_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.factor_x_listWidget = QtWidgets.QListWidget(Dialog)
        self.factor_x_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.factor_x_listWidget.setObjectName("factor_x_listWidget")
        self.verticalLayout_3.addWidget(self.factor_x_listWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.factor_color_listWidget = QtWidgets.QListWidget(Dialog)
        self.factor_color_listWidget.setObjectName("factor_color_listWidget")
        self.verticalLayout.addWidget(self.factor_color_listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.minimum_y = QtWidgets.QLineEdit(Dialog)
        self.minimum_y.setText("")
        self.minimum_y.setObjectName("minimum_y")
        self.verticalLayout_5.addWidget(self.minimum_y)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.maximum_y = QtWidgets.QLineEdit(Dialog)
        self.maximum_y.setText("")
        self.maximum_y.setObjectName("maximum_y")
        self.verticalLayout_4.addWidget(self.maximum_y)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 3)
        self.label.setBuddy(self.factor_x_listWidget)
        self.label_4.setBuddy(self.factor_color_listWidget)
        self.label_3.setBuddy(self.minimum_y)
        self.label_2.setBuddy(self.maximum_y)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.factor_x_listWidget, self.add_color_button)
        Dialog.setTabOrder(self.add_color_button, self.remove_color_button)
        Dialog.setTabOrder(self.remove_color_button, self.factor_color_listWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Display options"))
        self.add_color_button.setText(_translate("Dialog", "..."))
        self.remove_color_button.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "Factor(s) displayed in x-axis"))
        self.label_4.setText(_translate("Dialog", "Factor(s) displayed with colors"))
        self.label_3.setText(_translate("Dialog", "Minimum of y-axis"))
        self.label_2.setText(_translate("Dialog", "Maximum of y-axis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())