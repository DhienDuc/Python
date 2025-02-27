# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(391, 75)
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minus_button = QPushButton(Widget)
        self.minus_button.setObjectName(u"minus_button")
        icon = QIcon()
        icon.addFile(u":/prefix/images/Minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minus_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.minus_button)

        self.spin_box = QSpinBox(Widget)
        self.spin_box.setObjectName(u"spin_box")

        self.horizontalLayout.addWidget(self.spin_box)

        self.plus_button = QPushButton(Widget)
        self.plus_button.setObjectName(u"plus_button")
        icon1 = QIcon()
        icon1.addFile(u":/prefix/images/Plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.plus_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.plus_button)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.minus_button.setText(QCoreApplication.translate("Widget", u"Minus", None))
        self.plus_button.setText(QCoreApplication.translate("Widget", u"Plus", None))
    # retranslateUi

