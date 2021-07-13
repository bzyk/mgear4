import mgear.core.pyqt as gqt
from mgear.vendor.Qt import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 491)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_8 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ctl_name_rule_lineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.ctl_name_rule_lineEdit.setObjectName("ctl_name_rule_lineEdit")
        self.horizontalLayout.addWidget(self.ctl_name_rule_lineEdit)
        self.reset_ctl_name_rule_pushButton = QtWidgets.QPushButton(self.groupBox_8)
        self.reset_ctl_name_rule_pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.reset_ctl_name_rule_pushButton.setObjectName("reset_ctl_name_rule_pushButton")
        self.horizontalLayout.addWidget(self.reset_ctl_name_rule_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ctl_des_letter_case_comboBox = QtWidgets.QComboBox(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctl_des_letter_case_comboBox.sizePolicy().hasHeightForWidth())
        self.ctl_des_letter_case_comboBox.setSizePolicy(sizePolicy)
        self.ctl_des_letter_case_comboBox.setObjectName("ctl_des_letter_case_comboBox")
        self.ctl_des_letter_case_comboBox.addItem("")
        self.ctl_des_letter_case_comboBox.addItem("")
        self.ctl_des_letter_case_comboBox.addItem("")
        self.ctl_des_letter_case_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.ctl_des_letter_case_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.joint_name_rule_lineEdit = QtWidgets.QLineEdit(self.groupBox_9)
        self.joint_name_rule_lineEdit.setObjectName("joint_name_rule_lineEdit")
        self.horizontalLayout_2.addWidget(self.joint_name_rule_lineEdit)
        self.reset_joint_name_rule_pushButton = QtWidgets.QPushButton(self.groupBox_9)
        self.reset_joint_name_rule_pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.reset_joint_name_rule_pushButton.setObjectName("reset_joint_name_rule_pushButton")
        self.horizontalLayout_2.addWidget(self.reset_joint_name_rule_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.joint_des_letter_case_comboBox = QtWidgets.QComboBox(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joint_des_letter_case_comboBox.sizePolicy().hasHeightForWidth())
        self.joint_des_letter_case_comboBox.setSizePolicy(sizePolicy)
        self.joint_des_letter_case_comboBox.setObjectName("joint_des_letter_case_comboBox")
        self.joint_des_letter_case_comboBox.addItem("")
        self.joint_des_letter_case_comboBox.addItem("")
        self.joint_des_letter_case_comboBox.addItem("")
        self.joint_des_letter_case_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.joint_des_letter_case_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_10 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setObjectName("groupBox_10")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_10)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.side_left_name_lineEdit = QtWidgets.QLineEdit(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_left_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.side_left_name_lineEdit.setSizePolicy(sizePolicy)
        self.side_left_name_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.side_left_name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.side_left_name_lineEdit.setObjectName("side_left_name_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.side_left_name_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.groupBox_10)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.side_right_name_lineEdit = QtWidgets.QLineEdit(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_right_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.side_right_name_lineEdit.setSizePolicy(sizePolicy)
        self.side_right_name_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.side_right_name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.side_right_name_lineEdit.setObjectName("side_right_name_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.side_right_name_lineEdit)
        self.label_6 = QtWidgets.QLabel(self.groupBox_10)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.side_center_name_lineEdit = QtWidgets.QLineEdit(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_center_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.side_center_name_lineEdit.setSizePolicy(sizePolicy)
        self.side_center_name_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.side_center_name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.side_center_name_lineEdit.setObjectName("side_center_name_lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.side_center_name_lineEdit)
        self.reset_side_name_pushButton = QtWidgets.QPushButton(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_side_name_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_side_name_pushButton.setSizePolicy(sizePolicy)
        self.reset_side_name_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reset_side_name_pushButton.setObjectName("reset_side_name_pushButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.reset_side_name_pushButton)
        self.gridLayout.addWidget(self.groupBox_10, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        self.groupBox_12.setObjectName("groupBox_12")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_12)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_12)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.side_joint_left_name_lineEdit = QtWidgets.QLineEdit(self.groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_joint_left_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.side_joint_left_name_lineEdit.setSizePolicy(sizePolicy)
        self.side_joint_left_name_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.side_joint_left_name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.side_joint_left_name_lineEdit.setObjectName("side_joint_left_name_lineEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.side_joint_left_name_lineEdit)
        self.label_10 = QtWidgets.QLabel(self.groupBox_12)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.side_joint_right_name_lineEdit = QtWidgets.QLineEdit(self.groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_joint_right_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.side_joint_right_name_lineEdit.setSizePolicy(sizePolicy)
        self.side_joint_right_name_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.side_joint_right_name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.side_joint_right_name_lineEdit.setObjectName("side_joint_right_name_lineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.side_joint_right_name_lineEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox_12)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.side_joint_center_name_lineEdit = QtWidgets.QLineEdit(self.groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_joint_center_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.side_joint_center_name_lineEdit.setSizePolicy(sizePolicy)
        self.side_joint_center_name_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.side_joint_center_name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.side_joint_center_name_lineEdit.setObjectName("side_joint_center_name_lineEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.side_joint_center_name_lineEdit)
        self.reset_joint_side_name_pushButton = QtWidgets.QPushButton(self.groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_joint_side_name_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_joint_side_name_pushButton.setSizePolicy(sizePolicy)
        self.reset_joint_side_name_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reset_joint_side_name_pushButton.setObjectName("reset_joint_side_name_pushButton")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.reset_joint_side_name_pushButton)
        self.gridLayout.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_13 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy)
        self.groupBox_13.setObjectName("groupBox_13")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_13)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_13)
        self.label_12.setObjectName("label_12")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.ctl_padding_spinBox = QtWidgets.QSpinBox(self.groupBox_13)
        self.ctl_padding_spinBox.setObjectName("ctl_padding_spinBox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ctl_padding_spinBox)
        self.label_13 = QtWidgets.QLabel(self.groupBox_13)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.joint_padding_spinBox = QtWidgets.QSpinBox(self.groupBox_13)
        self.joint_padding_spinBox.setObjectName("joint_padding_spinBox")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.joint_padding_spinBox)
        self.horizontalLayout_4.addWidget(self.groupBox_13)
        self.groupBox_11 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setObjectName("groupBox_11")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_11)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_11)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.ctl_name_ext_lineEdit = QtWidgets.QLineEdit(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctl_name_ext_lineEdit.sizePolicy().hasHeightForWidth())
        self.ctl_name_ext_lineEdit.setSizePolicy(sizePolicy)
        self.ctl_name_ext_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.ctl_name_ext_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ctl_name_ext_lineEdit.setObjectName("ctl_name_ext_lineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ctl_name_ext_lineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox_11)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.joint_name_ext_lineEdit = QtWidgets.QLineEdit(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joint_name_ext_lineEdit.sizePolicy().hasHeightForWidth())
        self.joint_name_ext_lineEdit.setSizePolicy(sizePolicy)
        self.joint_name_ext_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.joint_name_ext_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.joint_name_ext_lineEdit.setObjectName("joint_name_ext_lineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.joint_name_ext_lineEdit)
        self.reset_name_ext_pushButton = QtWidgets.QPushButton(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_name_ext_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_name_ext_pushButton.setSizePolicy(sizePolicy)
        self.reset_name_ext_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reset_name_ext_pushButton.setObjectName("reset_name_ext_pushButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.reset_name_ext_pushButton)
        self.horizontalLayout_4.addWidget(self.groupBox_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 10000, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.load_naming_configuration_pushButton = QtWidgets.QPushButton(Form)
        self.load_naming_configuration_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.load_naming_configuration_pushButton.setObjectName("load_naming_configuration_pushButton")
        self.horizontalLayout_12.addWidget(self.load_naming_configuration_pushButton)
        self.save_naming_configuration_pushButton = QtWidgets.QPushButton(Form)
        self.save_naming_configuration_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.save_naming_configuration_pushButton.setObjectName("save_naming_configuration_pushButton")
        self.horizontalLayout_12.addWidget(self.save_naming_configuration_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.groupBox_8.setTitle(gqt.fakeTranslate("Form", "Controls Naming Rule", None, -1))
        self.ctl_name_rule_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Custom Naming rule:</span></p><p>To configure custom names, please use the following tokes with &quot;<span style=\" font-weight:600;\">{}</span>&quot;</p><p><br/></p><p><span style=\" font-weight:600;\">{component}</span> = The name of the component</p><p><span style=\" font-weight:600;\">{side}</span> = The side of the component</p><p><span style=\" font-weight:600;\">{index</span>} = Index of the component. This is important when more than one component have the same name</p><p><span style=\" font-weight:600;\">{description}</span> = The name of the object inside the component</p><p><span style=\" font-weight:600;\">{extension}</span> = The extension of the object. For example &quot;ctl&quot; for controls or &quot;jnt&quot; for joints</p><p><br/></p><p><span style=\" font-weight:600;\">NOTE:</span> the only valid separator is &quot;_&quot;. This is a Maya limitation.</p><p><br/></p><p><br/></p><p><span style=\" font-weight:600;\">This is the default configuration:</span></p><p>{component}_{side}{index}_{description}_{extension}</p><p><br/></p><p><br/></p><p><span style=\" font-weight:600;\">Other examples of configurations:</span></p><p>{component}{side}{index}{description}{extension}</p><p>{component}{index}_{description}_{extension}_{side}</p><p>{component}{index}_some_random_text_{description}_{extension}_{side}</p><p><br/></p><p><span style=\" font-weight:600;\">It is recommended to use all the tokens to ensure that there is no name clashing</span></p></body></html>", None, -1))
        self.ctl_name_rule_lineEdit.setText(gqt.fakeTranslate("Form", "{component}_{side}{index}_{description}_{extension}", None, -1))
        self.reset_ctl_name_rule_pushButton.setText(gqt.fakeTranslate("Form", "Reset", None, -1))
        self.label.setText(gqt.fakeTranslate("Form", "{descrition} Letter Case", None, -1))
        self.ctl_des_letter_case_comboBox.setItemText(0, gqt.fakeTranslate("Form", "Default", None, -1))
        self.ctl_des_letter_case_comboBox.setItemText(1, gqt.fakeTranslate("Form", "Upper Case", None, -1))
        self.ctl_des_letter_case_comboBox.setItemText(2, gqt.fakeTranslate("Form", "Lower Case", None, -1))
        self.ctl_des_letter_case_comboBox.setItemText(3, gqt.fakeTranslate("Form", "Capitalization", None, -1))
        self.groupBox_9.setTitle(gqt.fakeTranslate("Form", "Joints Naming Rule", None, -1))
        self.joint_name_rule_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Custom Naming rule:</span></p><p>To configure custom names, please use the following tokes with &quot;<span style=\" font-weight:600;\">{}</span>&quot;</p><p><br/></p><p><span style=\" font-weight:600;\">{component}</span> = The name of the component</p><p><span style=\" font-weight:600;\">{side}</span> = The side of the component</p><p><span style=\" font-weight:600;\">{index</span>} = Index of the component. This is important when more than one component have the same name</p><p><span style=\" font-weight:600;\">{description}</span> = The name of the object inside the component</p><p><span style=\" font-weight:600;\">{extension}</span> = The extension of the object. For example &quot;ctl&quot; for controls or &quot;jnt&quot; for joints</p><p><br/></p><p><span style=\" font-weight:600;\">NOTE:</span> the only valid separator is &quot;_&quot;. This is a Maya limitation.</p><p><br/></p><p><br/></p><p><span style=\" font-weight:600;\">This is the default configuration:</span></p><p>{component}_{side}{index}_{description}_{extension}</p><p><br/></p><p><br/></p><p><span style=\" font-weight:600;\">Other examples of configurations:</span></p><p>{component}{side}{index}{description}{extension}</p><p>{component}{index}_{description}_{extension}_{side}</p><p>{component}{index}_some_random_text_{description}_{extension}_{side}</p><p><br/></p><p><span style=\" font-weight:600;\">It is recommended to use all the tokens to ensure that there is no name clashing</span></p></body></html>", None, -1))
        self.joint_name_rule_lineEdit.setText(gqt.fakeTranslate("Form", "{component}_{side}{index}_{description}_{extension}", None, -1))
        self.reset_joint_name_rule_pushButton.setText(gqt.fakeTranslate("Form", "Reset", None, -1))
        self.label_3.setText(gqt.fakeTranslate("Form", "{descrition} Letter Case", None, -1))
        self.joint_des_letter_case_comboBox.setItemText(0, gqt.fakeTranslate("Form", "Default", None, -1))
        self.joint_des_letter_case_comboBox.setItemText(1, gqt.fakeTranslate("Form", "Upper Case", None, -1))
        self.joint_des_letter_case_comboBox.setItemText(2, gqt.fakeTranslate("Form", "Lower Case", None, -1))
        self.joint_des_letter_case_comboBox.setItemText(3, gqt.fakeTranslate("Form", "Capitalization", None, -1))
        self.groupBox_10.setTitle(gqt.fakeTranslate("Form", "Controls Sides Naming", None, -1))
        self.label_4.setText(gqt.fakeTranslate("Form", "Left", None, -1))
        self.side_left_name_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>set the text that will be used for the side:</p><p><br/></p><p><span style=\" font-weight:600;\">for example:</span></p><p>L</p><p>left</p><p>Left</p><p>l</p><p><br/></p><p>r</p><p>right</p><p>Right</p><p>Derecha</p><p>R</p><p><br/></p><p><br/></p></body></html>", None, -1))
        self.side_left_name_lineEdit.setText(gqt.fakeTranslate("Form", "L", None, -1))
        self.label_5.setText(gqt.fakeTranslate("Form", "Right", None, -1))
        self.side_right_name_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>set the text that will be used for the side:</p><p><br/></p><p><span style=\" font-weight:600;\">for example:</span></p><p>L</p><p>left</p><p>Left</p><p>l</p><p><br/></p><p>r</p><p>right</p><p>Right</p><p>Derecha</p><p>R</p><p><br/></p><p><br/></p></body></html>", None, -1))
        self.side_right_name_lineEdit.setText(gqt.fakeTranslate("Form", "R", None, -1))
        self.label_6.setText(gqt.fakeTranslate("Form", "Center", None, -1))
        self.side_center_name_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>set the text that will be used for the side:</p><p><br/></p><p><span style=\" font-weight:600;\">for example:</span></p><p>L</p><p>left</p><p>Left</p><p>l</p><p><br/></p><p>r</p><p>right</p><p>Right</p><p>Derecha</p><p>R</p><p><br/></p><p><br/></p></body></html>", None, -1))
        self.side_center_name_lineEdit.setText(gqt.fakeTranslate("Form", "C", None, -1))
        self.reset_side_name_pushButton.setText(gqt.fakeTranslate("Form", "Reset", None, -1))
        self.groupBox_12.setTitle(gqt.fakeTranslate("Form", "Joints Sides Naming", None, -1))
        self.label_9.setText(gqt.fakeTranslate("Form", "Left", None, -1))
        self.side_joint_left_name_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>set the text that will be used for the side:</p><p><br/></p><p><span style=\" font-weight:600;\">for example:</span></p><p>L</p><p>left</p><p>Left</p><p>l</p><p><br/></p><p>r</p><p>right</p><p>Right</p><p>Derecha</p><p>R</p><p><br/></p><p><br/></p></body></html>", None, -1))
        self.side_joint_left_name_lineEdit.setText(gqt.fakeTranslate("Form", "L", None, -1))
        self.label_10.setText(gqt.fakeTranslate("Form", "Right", None, -1))
        self.side_joint_right_name_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>set the text that will be used for the side:</p><p><br/></p><p><span style=\" font-weight:600;\">for example:</span></p><p>L</p><p>left</p><p>Left</p><p>l</p><p><br/></p><p>r</p><p>right</p><p>Right</p><p>Derecha</p><p>R</p><p><br/></p><p><br/></p></body></html>", None, -1))
        self.side_joint_right_name_lineEdit.setText(gqt.fakeTranslate("Form", "R", None, -1))
        self.label_11.setText(gqt.fakeTranslate("Form", "Center", None, -1))
        self.side_joint_center_name_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>set the text that will be used for the side:</p><p><br/></p><p><span style=\" font-weight:600;\">for example:</span></p><p>L</p><p>left</p><p>Left</p><p>l</p><p><br/></p><p>r</p><p>right</p><p>Right</p><p>Derecha</p><p>R</p><p><br/></p><p><br/></p></body></html>", None, -1))
        self.side_joint_center_name_lineEdit.setText(gqt.fakeTranslate("Form", "C", None, -1))
        self.reset_joint_side_name_pushButton.setText(gqt.fakeTranslate("Form", "Reset", None, -1))
        self.groupBox_13.setTitle(gqt.fakeTranslate("Form", "Index Padding", None, -1))
        self.label_12.setText(gqt.fakeTranslate("Form", "Controls", None, -1))
        self.label_13.setText(gqt.fakeTranslate("Form", "Joints", None, -1))
        self.groupBox_11.setTitle(gqt.fakeTranslate("Form", "Extensions Naming", None, -1))
        self.label_7.setText(gqt.fakeTranslate("Form", "Controls", None, -1))
        self.ctl_name_ext_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>Set the extension name for controls</p><p><br/></p><p><span style=\" font-weight:600;\">For example:</span></p><p>ctl</p><p>control</p><p>mover</p><p>ct</p><p>etc..</p></body></html>", None, -1))
        self.ctl_name_ext_lineEdit.setText(gqt.fakeTranslate("Form", "ctl", None, -1))
        self.label_8.setText(gqt.fakeTranslate("Form", "Joints", None, -1))
        self.joint_name_ext_lineEdit.setToolTip(gqt.fakeTranslate("Form", "<html><head/><body><p>Set the extension name for joints</p><p><br/></p><p><span style=\" font-weight:600;\">For example:</span></p><p>jnt</p><p>joint</p><p>bone</p><p>j</p><p>etc..</p></body></html>", None, -1))
        self.joint_name_ext_lineEdit.setText(gqt.fakeTranslate("Form", "jnt", None, -1))
        self.reset_name_ext_pushButton.setText(gqt.fakeTranslate("Form", "Reset", None, -1))
        self.load_naming_configuration_pushButton.setText(gqt.fakeTranslate("Form", "Load", None, -1))
        self.save_naming_configuration_pushButton.setText(gqt.fakeTranslate("Form", "Save", None, -1))
