# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QWidgetYwhdCR.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# MotionBuilder 2024と2025のどちらにも対応させるため、追記
try:
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
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
        QSizePolicy, QSlider, QVBoxLayout, QWidget)


class Ui_childWidget(object):
    def setupUi(self, childWidget):
        if not childWidget.objectName():
            childWidget.setObjectName(u"childWidget")
        childWidget.resize(330, 273)
        self.verticalLayout_3 = QVBoxLayout(childWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 12, -1, 12)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CreateButton = QPushButton(childWidget)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateButton.sizePolicy().hasHeightForWidth())
        self.CreateButton.setSizePolicy(sizePolicy)
        self.CreateButton.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        self.CreateButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.CreateButton)

        self.ResetButton = QPushButton(childWidget)
        self.ResetButton.setObjectName(u"ResetButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
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
        self.FitTrackerButton = QPushButton(childWidget)
        self.FitTrackerButton.setObjectName(u"FitTrackerButton")
        sizePolicy.setHeightForWidth(self.FitTrackerButton.sizePolicy().hasHeightForWidth())
        self.FitTrackerButton.setSizePolicy(sizePolicy)
        self.FitTrackerButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.FitTrackerButton)

        self.RotateButton = QPushButton(childWidget)
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
        self.label = QLabel(childWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalSlider = QSlider(childWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.BindButton = QPushButton(childWidget)
        self.BindButton.setObjectName(u"BindButton")
        sizePolicy.setHeightForWidth(self.BindButton.sizePolicy().hasHeightForWidth())
        self.BindButton.setSizePolicy(sizePolicy)
        self.BindButton.setMinimumSize(QSize(0, 0))
        self.BindButton.setFont(font)

        self.verticalLayout_2.addWidget(self.BindButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(childWidget)
        self.CreateButton.clicked.connect(childWidget.CreateActor_MarkerSet)
        self.FitTrackerButton.clicked.connect(childWidget.FitToTrackers)
        self.RotateButton.clicked.connect(childWidget.RotateYdeg)
        self.ResetButton.clicked.connect(childWidget.ResetAll)
        self.BindButton.clicked.connect(childWidget.BindMarkerModel)
        self.horizontalSlider.valueChanged.connect(childWidget.AdjustActorSize)

        QMetaObject.connectSlotsByName(childWidget)
    # setupUi

    def retranslateUi(self, childWidget):
        childWidget.setWindowTitle(QCoreApplication.translate("childWidget", u"Form", None))
        self.CreateButton.setText(QCoreApplication.translate("childWidget", u"Create Actor, MarkerSet", None))
        self.ResetButton.setText(QCoreApplication.translate("childWidget", u"Reset", None))
        self.FitTrackerButton.setText(QCoreApplication.translate("childWidget", u"Fit to Trackers", None))
        self.RotateButton.setText(QCoreApplication.translate("childWidget", u"Rotate y 180 degs.", None))
        self.label.setText(QCoreApplication.translate("childWidget", u"<html><head/><body><p>Adjust Actor Size ( small &lt;--&gt; big )</p></body></html>", None))
        self.BindButton.setText(QCoreApplication.translate("childWidget", u"Bind Trackers , Snap Actor", None))
    # retranslateUi

