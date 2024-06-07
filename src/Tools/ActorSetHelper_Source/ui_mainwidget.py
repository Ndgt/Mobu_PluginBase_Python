# -*- coding: utf-8 -*-

# pyside6-uicによる自動生成ファイル
# 追記箇所を日本語コメントアウトにて表記

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# MotionBuilder 2024以下のバージョンにも対応させる
try:
    # Signalの追記に伴い、宣言
    from PySide6 import QtCore

    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
        QSizePolicy, QSlider, QVBoxLayout, QWidget)

except:
    from PySide2 import QtCore
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
        QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_toolWidget(object):
    def setupUi(self, toolWidget):
        if not toolWidget.objectName():
            toolWidget.setObjectName(u"toolWidget")
        toolWidget.resize(300, 275)
        self.verticalLayout_3 = QVBoxLayout(toolWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 12, -1, 12)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CreateButton = QPushButton(toolWidget)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateButton.sizePolicy().hasHeightForWidth())
        self.CreateButton.setSizePolicy(sizePolicy)
        self.CreateButton.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        self.CreateButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.CreateButton)

        self.ResetButton = QPushButton(toolWidget)
        self.ResetButton.setObjectName(u"ResetButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy1)
        self.ResetButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.ResetButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FitTrackerButton = QPushButton(toolWidget)
        self.FitTrackerButton.setObjectName(u"FitTrackerButton")
        sizePolicy.setHeightForWidth(self.FitTrackerButton.sizePolicy().hasHeightForWidth())
        self.FitTrackerButton.setSizePolicy(sizePolicy)
        self.FitTrackerButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.FitTrackerButton)

        self.RotateButton = QPushButton(toolWidget)
        self.RotateButton.setObjectName(u"RotateButton")
        sizePolicy.setHeightForWidth(self.RotateButton.sizePolicy().hasHeightForWidth())
        self.RotateButton.setSizePolicy(sizePolicy)
        self.RotateButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.RotateButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 10, 6, 10)
        self.label = QLabel(toolWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalSlider = QSlider(toolWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy3)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.BindButton = QPushButton(toolWidget)
        self.BindButton.setObjectName(u"BindButton")
        sizePolicy.setHeightForWidth(self.BindButton.sizePolicy().hasHeightForWidth())
        self.BindButton.setSizePolicy(sizePolicy)
        self.BindButton.setMinimumSize(QSize(0, 0))
        self.BindButton.setFont(font)

        self.verticalLayout_2.addWidget(self.BindButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(toolWidget)

        # QtDesignerでのSignalの設定が面倒なので手作業でSignalを追記
        self.CreateButton.connect(QtCore.SIGNAL("clicked()"), toolWidget.CreateActor_MarkerSet)
        self.FitTrackerButton.connect(QtCore.SIGNAL("clicked()"), toolWidget.FitToTrackers)
        self.RotateButton.connect(QtCore.SIGNAL("clicked()"), toolWidget.RotateYdeg)
        self.ResetButton.connect(QtCore.SIGNAL("clicked()"), toolWidget.ResetAll)
        self.horizontalSlider.connect(QtCore.SIGNAL("sliderMoved(int)"), toolWidget.AdjustActorSize)
        self.BindButton.connect(QtCore.SIGNAL("clicked()"), toolWidget.BindMarkerModel)   

        QMetaObject.connectSlotsByName(toolWidget)
    # setupUi

    def retranslateUi(self, toolWidget):
        toolWidget.setWindowTitle(QCoreApplication.translate("toolWidget", u"Form", None))
        self.CreateButton.setText(QCoreApplication.translate("toolWidget", u"Create Actor, MarkerSet", None))
        self.ResetButton.setText(QCoreApplication.translate("toolWidget", u"Reset", None))
        self.FitTrackerButton.setText(QCoreApplication.translate("toolWidget", u"Fit to Trackers", None))
        self.RotateButton.setText(QCoreApplication.translate("toolWidget", u"Rotate y 180 degs.", None))
        self.label.setText(QCoreApplication.translate("toolWidget", u"<html><head/><body><p>Adjust Actor Size ( small &lt;--&gt; big )</p></body></html>", None))
        self.BindButton.setText(QCoreApplication.translate("toolWidget", u"Bind Trackers , Snap Actor", None))
    # retranslateUi

