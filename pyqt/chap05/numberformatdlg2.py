#!/usr/bin/env python
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class NumberFormatDlg(QDialog):

    def __init__(self, format, parent=None):
        super(NumberFormatDlg, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        punctuationRe = QRegExp(r"[ ,;:.]")

        thousandsLabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        self.thousandsEdit.setMaxLength(1)
        self.thousandsEdit.setValidator(
                QRegExpValidator(punctuationRe, self))

        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        self.decimalMarkerEdit.setMaxLength(1)
        self.decimalMarkerEdit.setValidator(
                QRegExpValidator(punctuationRe, self))
        self.decimalMarkerEdit.setInputMask("X")

        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        buttonBox = QDialogButtonBox(QDialogButtonBox.Apply|
                                     QDialogButtonBox.Close)

        self.format = format

        grid = QGridLayout()
        grid.addWidget(thousandsLabel, 0, 0)
        grid.addWidget(self.thousandsEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        #dizzy Place 1
        grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)# 3,0 is the place the latter 1,2 is the same
        grid.addWidget(buttonBox, 4, 0, 1, 2)
        self.setLayout(grid)
#dizzyPlace 2
        self.connect(buttonBox.button(QDialogButtonBox.Apply),
                     SIGNAL("clicked()"), self.apply) # apply implement by you so no ()
        self.connect(buttonBox, SIGNAL("rejected()"),
                     self, SLOT("reject()"))#reject implement not by you 
        self.setWindowTitle("Set Number Format (Modeless)")


    def apply(self):
        thousands = unicode(self.thousandsEdit.text())
        decimal = unicode(self.decimalMarkerEdit.text())
        if thousands == decimal:
            QMessageBox.warning(self, "Format Error",
                    "The thousands separator and the decimal marker "
                    "must be different.")
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
            return
        if len(decimal) == 0:
            QMessageBox.warning(self, "Format Error",
                                "The decimal marker may not be empty.")
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return

        self.format["thousandsseparator"] = thousands
        self.format["decimalmarker"] = decimal
        self.format["decimalplaces"] = \
                self.decimalPlacesSpinBox.value()
        self.format["rednegatives"] = \
                self.redNegativesCheckBox.isChecked()
        self.emit(SIGNAL("changed"))


