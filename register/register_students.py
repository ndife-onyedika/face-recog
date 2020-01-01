import cv2
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class REGISTER_STUDENT(QDialog):
    def __init__(self, main_layout, components):
        super().__init__()
        self.main_layout = main_layout

        self.setWindowTitle("REGISTER STUDENT")
        components = components()

        # For other screens
        self.stacked = QStackedLayout()

        self.setupUI(components)


    def setupUI(self, components):
        self.comp = components

        self.personal_details()
        
        # SETTING LAYOUTS
        self.setLayout(self.stacked)

    def personal_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Personal Details")

        _next = QPushButton("Next")
        
        # _next.setLayoutDirection()

        # ADDING WIDGETS
        grid.addWidget(self.comp.f_name, 0, 0)
        grid.addWidget(self.comp.f_name_input, 0, 1)

        grid.addWidget(self.comp.m_name, 1, 0)
        grid.addWidget(self.comp.m_name_input, 1, 1)

        grid.addWidget(self.comp.l_name, 2, 0)
        grid.addWidget(self.comp.l_name_input, 2, 1)

        grid.addWidget(self.comp.dob_label, 3, 0)
        grid.addLayout(self.comp.dob_layout, 3, 1)

        grid.addWidget(self.comp.age, 4, 0)
        grid.addWidget(self.comp.age_input, 4, 1)

        grid.addWidget(self.comp.gender, 5, 0)
        grid.addLayout(self.comp.gender_layout, 5, 1)

        grid.addWidget(self.comp.marital, 6, 0)
        grid.addWidget(self.comp.marital_select, 6, 1)

        grid.addWidget(self.comp.nationality, 7, 0)
        grid.addWidget(self.comp.nationality_input, 7, 1)

        grid.addWidget(self.comp.state_origin, 8, 0)
        grid.addWidget(self.comp.state_origin_input, 8, 1)

        grid.addWidget(self.comp.lga_origin, 9, 0)
        grid.addWidget(self.comp.lga_origin_input, 9, 1)

        grid.addWidget(_next, 10,0,1,0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)


        self.pd_main_widget = QWidget()
        self.pd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.pd_main_widget)
        self.stacked.setCurrentWidget(self.pd_main_widget)

        # When next button is clicked
        _next.clicked.connect(self.school_details)

    def school_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("School Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.j_num, 0, 0)
        grid.addWidget(self.comp.j_num_input, 0, 1)

        grid.addWidget(self.comp.college, 1, 0)
        grid.addWidget(self.comp.college_select, 1, 1)

        grid.addWidget(self.comp.dept, 2, 0)
        grid.addWidget(self.comp.dept_select, 2, 1)

        grid.addWidget(self.comp.level, 3, 0)
        grid.addWidget(self.comp.level_select, 3, 1)

        grid.addWidget(self.comp.m_num, 4, 0)
        grid.addWidget(self.comp.m_num_input, 4, 1)

        grid.addLayout(btn_view, 5,0,1,0)

        # On change of College
        self.comp.college_select.currentIndexChanged.connect(self.school)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.sd_main_widget = QWidget()
        self.sd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.sd_main_widget)
        self.stacked.setCurrentWidget(self.sd_main_widget)


        # When prev button is clicked
        _prev.clicked.connect(lambda: self.stacked.setCurrentWidget(self.pd_main_widget))
        

        # When next button is clicked
        _next.clicked.connect(self.contact_details)
        
        # _next.setLayoutDirection


    def contact_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Contact Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.address, 0, 0)
        grid.addWidget(self.comp.address_input, 0, 1)

        grid.addWidget(self.comp.phone, 1, 0)
        grid.addWidget(self.comp.phone_input, 1, 1)

        grid.addWidget(self.comp.email, 2, 0)
        grid.addWidget(self.comp.email_input, 2, 1)

        grid.addLayout(btn_view, 3,0,1,0)


        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.cd_main_widget = QWidget()
        self.cd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.cd_main_widget)
        self.stacked.setCurrentWidget(self.cd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(lambda: self.stacked.setCurrentWidget(self.sd_main_widget))
        

        # When next button is clicked
        _next.clicked.connect(self.parent_details)
        

    def parent_details(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox("Parent/Sponsor Details")

        btn_view = QHBoxLayout()
        _next = QPushButton("Next")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)

        grid.addWidget(self.comp.p_name, 0, 0)
        grid.addWidget(self.comp.p_name_input, 0, 1)

        grid.addWidget(self.comp.p_email, 1, 0)
        grid.addWidget(self.comp.p_email_input, 1, 1)

        grid.addWidget(self.comp.p_phone, 2, 0)
        grid.addWidget(self.comp.p_phone_input, 2, 1)

        grid.addLayout(btn_view, 3,0,1,0)


        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.psd_main_widget = QWidget()
        self.psd_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.psd_main_widget)
        self.stacked.setCurrentWidget(self.psd_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(lambda: self.stacked.setCurrentWidget(self.cd_main_widget))
        
        

        # When next button is clicked
        _next.clicked.connect(self.done)
        

    def done(self):
        vbox = QVBoxLayout()
        grid = QGridLayout()
        group_box = QGroupBox()

        btn_view = QHBoxLayout()
        _next = QPushButton("Capture Face")
        _prev = QPushButton("Previous")

        btn_view.addWidget(_prev)
        btn_view.addWidget(_next)


        grid.addWidget(self.comp.dor, 0, 0)
        grid.addWidget(self.comp.dor_text, 0, 1)

        grid.addLayout(btn_view, 1,0,1,0)

        group_box.setLayout(grid)
        vbox.addWidget(group_box)

        self.d_main_widget = QWidget()
        self.d_main_widget.setLayout(vbox)

        self.stacked.addWidget(self.d_main_widget)
        self.stacked.setCurrentWidget(self.d_main_widget)

        # When prev button is clicked
        _prev.clicked.connect(lambda: self.stacked.setCurrentWidget(self.psd_main_widget))
        


        # When next button is clicked
        _next.clicked.connect(self.register_student_details)
        _next.setIcon(QIcon("./assets/img/Capture.png"))
        _next.setIconSize(QSize(20,20))


    def school(self, i):
        if i == 0 or i == 1 or i == 4 or i == 6 or i == 7 or i == 9 or i == 10:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300L", "400L"])
        elif i == 2 or i == 3 or i == 5 or i == 8:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(["100L", "200L", "300L", "400L", "500L"])
        elif i == 11:
            self.comp.level_select.clear()
            self.comp.level_select.addItems(
                ["100L", "200L", "300L", "400L", "500L", "600L"]
            )

        if i == 0:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRIBUSINESS MANAGEMENT",
                    "AGRICULTURAL ECONOMICS",
                    "AGRICULTURAL EXTENSION AND RURAL SOCIOLOGY",
                ]
            )

        elif i == 1:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ANIMAL BREEDING AND PHYSIOLOGY",
                    "ANIMAL NUTRITION AND FORAGE SCIENCE",
                    "ANIMAL PRODUCTION AND LIVESTOCK MANAGEMENT",
                ]
            )

        elif i == 2:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FOOD SCIENCE AND TECHNOLOGY",
                    "HOME SCIENCE/HOSPITALITY MANAGEMENT AND TOURISM",
                    "HUMAN NUTRITION AND DIETETICS",
                ]
            )
        elif i == 3:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                ["AGRONOMY", "PLANT HEALTH MANAGEMENT", "SOIL SCIENCE AND METREOLOGY"]
            )
        elif i == 4:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ADULT AND CONTINUING EDUCATION",
                    "EDUCATIONAL FOUNDATION",
                    "INDUSTRIAL TECHNOLOGY EDUCATION",
                    "LIBRARY AND INFORMATION SCIENCE",
                    "PSYCHOLOGY AND COUNSELING",
                    "SCIENCE EDUCATION",
                ]
            )
        elif i == 5:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "AGRICULTURAL AND BIO-RESOURCES ENGINEERING",
                    "CHEMICAL ENGINEERING",
                    "CIVIL ENGINEERING",
                    "COMPUTER ENGINEERING",
                    "ELECTRICAL AND ELECTRONICS ENGINEERING",
                    "MECHANICAL ENGINEERING",
                ]
            )
        elif i == 6:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "FRENCH LANGUAGE",
                    "GERMAN LANGUAGE",
                    "HISTORY AND PHILOSOPHY OF SCIENCE",
                    "NIGERIA HISTORY",
                    "PEACE AND CONFLICT STUDIES",
                    "PHILOSOPHY AND LOGIC",
                    "PHYSICAL AND HEALTH EDUCATION",
                    "SOCIAL SCIENCE",
                ]
            )
        elif i == 7:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ACCOUNTING",
                    "BANKING AND FINANCE",
                    "BUSINESS ADMINISTRATION",
                    "ECONOMICS",
                    "ENTREPRENEURIAL STUDIES",
                    "HUMAN RESOURCE MANAGEMENT",
                    "MARKETING",
                ]
            )
        elif i == 8:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "ENVIRONMENTAL MANAGEMENT AND TOXICOLOGY",
                    "FORESTRY AND ENVIRONMENTAL MANAGEMENT",
                    "FISHERIES AND AQUATIC RESOURCES MANAGEMENT",
                ]
            )
        elif i == 9:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "BIOCHEMISTRY",
                    "MICROBIOLOGY",
                    "PLANT SCIENCE AND BIOTECHNOLOGY",
                    "ZOOLOGY AND ENVIRONMENTAL BIOLOGY",
                ]
            )

        elif i == 10:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "CHEMISTRY",
                    "PHYSICS",
                    "COMPUTER SCIENCE",
                    "STATISTICS",
                    "MATHEMATICS",
                ]
            )

        elif i == 11:
            self.comp.dept_select.clear()
            self.comp.dept_select.addItems(
                [
                    "VERTINARY ANATOMY",
                    "VERTINARY MEDICINE",
                    "VERTINARY PUBLIC HEALTH AND PREVENTIVE MEDICINE",
                ]
            )

    def register_student_details(self):
        # Assigning Variables
        first_name = self.comp.f_name_input.text()
        middle_name = self.comp.m_name_input.text()
        last_name = self.comp.l_name_input.text()
        date_of_birth = self.comp.dob_date_label.text()
        age = self.comp.age_input.text()
        gender = (
            self.comp.gender_1.text()
            if self.comp.gender_1.isChecked()
            else self.comp.gender_2.text()
        )
        nationality = self.comp.nationality_input.text()
        state_of_origin = self.comp.state_origin_input.text()
        lga_origin = self.comp.lga_origin_input.text()
        marital = self.comp.marital_select.currentText()
        # Assigning Variables
        jamb_number = self.comp.j_num_input.text()
        college = self.comp.college_select.currentText()
        dept = self.comp.dept_select.currentText()
        level = self.comp.level_select.currentText()
        matric_number = self.comp.m_num_input.text()
        # Assigning Variables
        address = self.comp.address_input.text()
        phone = self.comp.phone_input.text()
        email = self.comp.email_input.text()
        # Assigning Variables
        p_name = self.comp.p_name_input.text()
        p_email = self.comp.p_email_input.text()
        p_phone = self.comp.p_phone_input.text()
        date_of_reg = self.comp.dor_text.text()

        self.comp.datab.cur.execute(
            f"INSERT INTO recognize_students(first_name, middle_name, last_name,age,date_of_birth, gender, nationality, state_of_origin, lga_origin,marital_status,jamb_number,college,department,level,matric_number,address,phone_number,email,parent_name,parent_email,parent_phone,date_of_registration) VALUES('{first_name}','{middle_name}','{last_name}',{age},'{date_of_birth}','{gender}','{nationality}','{state_of_origin}','{lga_origin}','{marital}','{jamb_number}','{college}','{dept}','{level}','{matric_number}','{address}','{phone}','{email}','{p_name}','{p_email}','{p_phone}','{date_of_reg}')"
        )

        self.register_face()


    def register_face(self):
        self.comp.datab.cur.execute("SELECT * FROM recognize_students")
        self.latest_register = self.comp.datab.cur.fetchall()[-1]

        self._id = self.latest_register[0]
        self.name = f"{self.latest_register[3]}_{self.latest_register[1]}".lower()

        self.face_cascade = cv2.CascadeClassifier(
            "./assets/classifier/haarcascade_frontalface_alt2.xml"
        )

        self.video_widget = QWidget()
        self.video_init_layout = QVBoxLayout()

        # Create Camera View
        self.cam_view = QLabel()
        self.cam_btn = QPushButton('Capture')


        self.video_init_layout.addWidget(self.cam_view)
        self.video_init_layout.addWidget(self.cam_btn)
        self.video_widget.setLayout(self.video_init_layout)

        self.cam_btn.clicked.connect(self.snap)

        self.main_layout.addWidget(self.video_widget)
        self.main_layout.setCurrentWidget(self.video_widget)

        # create a timer
        self.timer = QTimer()

        # set timer timeout callback function
        self.timer.timeout.connect(self._video)

        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0)
            self.timer.start(1)

    def _video(self):
        ret, self.image = self.cam.read()

        image_copy = self.image.copy()

        # Capture Image-by-Image
        gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 255, 255), 1)

        self.image_shown = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

        # get image infos
        self.height, self.width, self.channel = self.image_shown.shape
        self.step = self.channel * self.width

        # create QImage from image
        self.qImg = QImage(
            self.image_shown.data,
            self.width,
            self.height,
            self.step,
            QImage.Format_RGB888,
        )

        # Set the data from qImg to cam_view
        self.cam_view.setPixmap(QPixmap.fromImage(self.qImg))        

    def snap(self):
        image_cropped = self.image[0:480, 80:560]
        if not os.path.exists(f"./face_recog_android/media/image/student/{str(self.name)}"):
            os.makedirs(f"./face_recog_android/media/image/student/{str(self.name)}")
        cv2.imwrite(
            f"./face_recog_android/media/image/student/{str(self.name)}/{str(self.name)}.jpg",
            image_cropped,
        )

        self.timer.stop()
        self.cam.release()

        self.comp.datab.cur.execute(f"INSERT INTO recognize_students(pic) VALUES('image/student/{str(self.name)}/{str(self.name)}.jpg')")

        self.comp.datab.conn.commit()
        self.comp.datab.conn.close()


        self.main_layout.setCurrentIndex(0)