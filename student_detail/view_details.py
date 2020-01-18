import os

import requests
from PyQt5.Qt import QFileInfo
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import (QAction, QFileDialog, QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel, QMainWindow, QPushButton,
                             QScrollArea, QTextEdit, QToolBar, QVBoxLayout,
                             QWidget)

from components.components import COMPONENTS

APP_URL = "http://127.0.0.1:8000"
# APP_URL = "https://face-recog-server.herokuapp.com"
class VIEW_DETAILS(QMainWindow):
    def __init__(self, title, prev_scrn, profile, super_layout):
        super().__init__()
        self.title = title
        self.title.setWindowTitle("VIEW STUDENT DETAILS")

        self.super_layout = super_layout

        self.previous = prev_scrn

        self.MAIN_VIEW(profile)

    def MAIN_VIEW(self, profile):
        self.comp = COMPONENTS()
        
        _id = int(profile["id"])

        r = requests.get(url=f"{APP_URL}/users/students/{_id}")

        self.profile = r.json()

        self.main_menu = self.menuBar()
        self.toolbar = QToolBar()

        self.file_menu = self.main_menu.addMenu("File")
        self.edit_menu = self.main_menu.addMenu("Edit")

        self.export = QAction(
            QIcon("./assets/icons/export_pdf.png"), "Export PDF", self
        )
        self.export.setShortcut("Ctrl+S")

        self.edit_action = QAction(
            QIcon("./assets/icons/edit_profile.png"), "Edit Student Details", self
        )

        self.exit_action = QAction(QIcon("./assets/icons/exit.png"), "Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.export)
        self.file_menu.addAction(self.exit_action)

        self.edit_menu.addAction(self.edit_action)

        self.export.triggered.connect(self._save_file)
        self.edit_action.triggered.connect(self._edit_screen)
        self.exit_action.triggered.connect(self.previous)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.exit_action)
        self.toolbar.addAction(self.edit_action)
        self.toolbar.addAction(self.export)

        main_widget = QWidget()
        self.vbox = QVBoxLayout()

        self.personal_details()

        self.contact_details()

        self.parent_detail()

        self.other_detail()

        main_widget.setLayout(self.vbox)

        scroll = QScrollArea()
        scroll.setWidget(main_widget)
        scroll.setWidgetResizable(True)

        self.setCentralWidget(scroll)

        self.super_layout.addWidget(self)
        self.super_layout.setCurrentWidget(self)

    def personal_details(self):
        group_box = QGroupBox()
        grid = QGridLayout()
        group_box.setLayout(grid)
        
        group_box.setTitle("Personal Details")

        # for views containing school detail of student
        sd_view = QHBoxLayout()
        sd_detail_view = QGridLayout()

        grid.addLayout(sd_view, 0, 0, 1, 0)

        sd_view.addLayout(sd_detail_view)
        sd_view.addWidget(self.comp.profile_pic)

        r = requests.get(url=self.profile["pic"], stream=True)

        pic = QImage()
        pic.loadFromData(r.content)

        self.comp.profile_pic.setPixmap(QPixmap.fromImage(pic))

        sd_detail_view.addWidget(self.comp.m_num, 0, 0)
        m_num_text = QLabel()
        sd_detail_view.addWidget(m_num_text, 0, 1)
        m_num_text.setText(self.profile["matric_number"])

        sd_detail_view.addWidget(self.comp.j_num, 1, 0)
        j_num_text = QLabel()
        sd_detail_view.addWidget(j_num_text, 1, 1)
        j_num_text.setText(self.profile["jamb_number"])

        sd_detail_view.addWidget(self.comp.college, 2, 0)
        college_text = QLabel()
        sd_detail_view.addWidget(college_text, 2, 1)
        college_text.setText(self.profile["college"])

        sd_detail_view.addWidget(self.comp.dept, 3, 0)
        dept_text = QLabel()
        sd_detail_view.addWidget(dept_text, 3, 1)
        dept_text.setText(self.profile["department"])

        sd_detail_view.addWidget(self.comp.level, 4, 0)
        level_text = QLabel()
        sd_detail_view.addWidget(level_text, 4, 1)
        level_text.setText(self.profile["level"])

        pd_detail_view = QGridLayout()
        name = QLabel("Name:")

        grid.addWidget(name, 1, 0)

        pd_detail_view.addWidget(self.comp.l_name, 0, 0)
        l_name_text = QLabel()
        pd_detail_view.addWidget(l_name_text, 0, 1)
        l_name_text.setText(self.profile["last_name"])

        pd_detail_view.addWidget(self.comp.m_name, 1, 0)
        m_name_text = QLabel()
        pd_detail_view.addWidget(m_name_text, 1, 1)
        m_name_text.setText(self.profile["middle_name"])

        pd_detail_view.addWidget(self.comp.f_name, 2, 0)
        f_name_text = QLabel()
        pd_detail_view.addWidget(f_name_text, 2, 1)
        f_name_text.setText(self.profile["first_name"])

        grid.addLayout(pd_detail_view, 1, 1)

        grid.addWidget(self.comp.age, 2, 0)
        age_text = QLabel()
        grid.addWidget(age_text, 2, 1)
        age_text.setText(str(self.profile["age"]))

        grid.addWidget(self.comp.gender, 3, 0)
        gender_text = QLabel()
        grid.addWidget(gender_text, 3, 1)
        gender_text.setText(self.profile["gender"])

        grid.addWidget(self.comp.dob_label, 4, 0)
        dob_text = QLabel()
        grid.addWidget(dob_text, 4, 1)
        dob_text.setText(str(self.profile["date_of_birth"]))

        grid.addWidget(self.comp.nationality, 5, 0)
        nationality_text = QLabel()
        grid.addWidget(nationality_text, 5, 1)
        nationality_text.setText(self.profile["nationality"])

        grid.addWidget(self.comp.state_origin, 6, 0)
        state_origin_text = QLabel()
        grid.addWidget(state_origin_text, 6, 1)
        state_origin_text.setText(self.profile["state_of_origin"])

        grid.addWidget(self.comp.lga_origin, 7, 0)
        lga_origin_text = QLabel()
        grid.addWidget(lga_origin_text, 7, 1)
        lga_origin_text.setText(self.profile["lga_origin"])

        grid.addWidget(self.comp.marital, 8, 0)
        marital_text = QLabel()
        grid.addWidget(marital_text, 8, 1)
        marital_text.setText(self.profile["marital_status"])

        self.vbox.addWidget(group_box)

    def contact_details(self):
        group_box = QGroupBox()
        grid = QGridLayout()

        group_box.setLayout(grid)


        group_box.setTitle("Contact Details")

        grid.addWidget(self.comp.address, 0, 0)
        address_text = QLabel()
        grid.addWidget(address_text, 0, 1)
        address_text.setText(self.profile["address"])

        grid.addWidget(self.comp.phone, 1, 0)
        phone_text = QLabel()
        grid.addWidget(phone_text, 1, 1)
        phone_text.setText(self.profile["phone_number"])

        grid.addWidget(self.comp.email, 2, 0)
        email_text = QLabel()
        grid.addWidget(email_text, 2, 1)
        email_text.setText(self.profile["email"])

        self.vbox.addWidget(group_box)

    def parent_detail(self):
        group_box = QGroupBox()
        grid = QGridLayout()

        group_box.setLayout(grid)

        group_box.setTitle("Parent's/Sponsor's Details")

        grid.addWidget(self.comp.p_name, 0, 0)
        p_name_text = QLabel()
        grid.addWidget(p_name_text, 0, 1)
        p_name_text.setText(self.profile["parent_name"])

        grid.addWidget(self.comp.p_email, 1, 0)
        p_email_text = QLabel()
        grid.addWidget(p_email_text, 1, 1)
        p_email_text.setText(self.profile["parent_email"])

        grid.addWidget(self.comp.p_phone, 2, 0)
        p_phone_text = QLabel()
        grid.addWidget(p_phone_text, 2, 1)
        p_phone_text.setText(self.profile["parent_phone"])

        self.vbox.addWidget(group_box)

    def other_detail(self):
        group_box = QGroupBox()
        grid = QGridLayout()

        group_box.setLayout(grid)

        grid.addWidget(self.comp.dor, 0, 0)
        self.dor_text = QLabel()
        grid.addWidget(self.dor_text, 0, 1)
        self.dor_text.setText(str(self.profile["date_of_registration"]))

        self.vbox.addWidget(group_box)

    def _save_file(self):
        r = requests.get(url=f"{APP_URL}/recognize/d_stud/")

        name = QFileDialog.getSaveFileName(self, "Export PDF", filter="(*.pdf)")

        file_name = f"{name[0]}"

        if file_name.endswith(".pdf"):
            file = file_name.replace(".pdf", "")
        else:
            file = file_name

        if file != "":
            with open(f"{file}.pdf", "wb") as outputStream:
                outputStream.write(r.content)
                outputStream.close()
        else:
            file = "Student_Details"

    def _edit_screen(self):
        from student_detail.edit_details import EDIT_DETAILS

        edit_details = EDIT_DETAILS(
            self.title, self.previous, self.profile, self.super_layout
        )
