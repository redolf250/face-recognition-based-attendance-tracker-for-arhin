from utils.sql import *
from packages.pyqt import *
from packages.system import *
from packages.processing import *
from registration.ui_registration import Ui_Registration

class Registration(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_registration = Ui_Registration()
        self.ui_registration.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_registration.btn_close.clicked.connect(self.close)
        self.ui_registration.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_registration.frame.mouseMoveEvent = self.MoveWindow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_registration.frame.setGraphicsEffect(self.shadow)

        self.ui_registration.btn_reg_browse.clicked.connect(self.browse_images)
        self.ui_registration.btn_register.clicked.connect(self.register)
        self.ui_registration.btn_search.clicked.connect(self.search_details)
        self.ui_registration.btn_delete.clicked.connect(self.delete_details)
        

    def dump_face_encoding(self):
        encodings=list(self.get_face_encoding(self.ui_registration.filename.text()))
        return self.format_face_encodings(encodings)
        
    def format_face_encodings(self,encoding):
        value="\'{}\'".format(encoding)
        return value

    def save_picture(self):
        path=f'C:\\ProgramData\\weTrack\\images\\{self.ui_registration.reference.text()}.png'
        with open(self.ui_registration.filename.text(),'rb') as file:
            img_data=file.read()
            with open(path,'wb') as out_put:
                out_put.write(img_data)
            out_put.close()
        file.close()

    def register(self):
        _,empty = self.validate_fields()
        db=sqlite3.connect(self.database_path())
        cursor = db.cursor()
        if len(empty)==0:
            details=self.get_text_from_fields()
            db_results=self.query_database(f"SELECT reference FROM tb_details WHERE reference={details[0]}")
            if not db_results:
                encodings = self.dump_face_encoding()
                try:
                    cursor.execute(
                        "INSERT INTO tb_details(reference,firstname,lastname,contact,position) VALUES(?,?,?,?,?)",
                        (details[0],details[1],details[2],details[3],details[4]))
                    cursor.execute(f"INSERT INTO tb_encodings(reference,face_encoding) VALUES({details[0]},{encodings})")
                    db.commit()
                    db.close()
                    self.save_picture()
                    self.ui_registration.label_notification.setText(f"Data captured successfully, for person\n with Reference: {details[0]}")
                except Exception as e:
                    self.ui_registration.label_notification.setText(f"{str(e)}\n details already exists")
            else:
                self.ui_registration.label_notification.setText(f"Oops! data already captured for person\n with Reference: {details[0]}")
        else:
            self.ui_registration.label_notification.setText(f"Oops! some data fields are empty, provide all\ndetails to continue registration")

    def delete_details(self):
        db=sqlite3.connect(self.database_path())
        cursor = db.cursor()
        reference=self.ui_registration.reference.text()
        if reference !='':
            cursor.execute(f"DELETE FROM tb_details WHERE reference={reference}")
            cursor.execute(f"DELETE FROM tb_encodings WHERE reference={reference}")
            db.commit()
            db.close()
            self.reset_interface()
            self.ui_registration.label_notification.setText(f"Record associated with person\nReference: {reference} removed!") 
        else:
            self.reset_interface()
            self.ui_registration.label_notification.setText(f"Oops! reference field can't be empty...") 
             
    def search_details(self):
        reference=self.ui_registration.reference.text()
        if reference !='':
            details=self.query_database(f"SELECT * FROM tb_details WHERE reference={reference}")
            if details:
                self.reset_interface()
                self.update_interfaces_with_details(details)
                self.ui_registration.image.setPixmap(QPixmap.fromImage(f"C:\\ProgramData\\weTrack\\images\\{reference}.png"))
                self.ui_registration.image.setScaledContents(True)
            else:
                self.reset_interface()
                self.ui_registration.label_notification.setText(f"Oops! no record found for person\n with Reference: {reference}")
        else:
            self.ui_registration.label_notification.setText(f"Oops! reference field can't be empty...") 

    def query_database(self, query: str):
        db=sqlite3.connect(self.database_path())
        cursor = db.cursor()
        detail =cursor.execute(query)
        detail= cursor.fetchone()
        db.commit()
        cursor.close()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
            return db_data

    def get_face_encoding(self,image_path: str):
        image = face_recognition.load_image_file(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding

    def validate_fields(self):
        properties_list =  self.get_text_from_fields()
        data_list = []
        empty_list = []
        for field in properties_list:
            if field:
                data_list.append(field)
            else:
               empty_list.append(field)
        return data_list,empty_list

    def get_text_from_fields(self):
        reference=math.floor(np.random.random(1)*10000000)
        self.ui_registration.reference.setText(str(reference))
        firstname = self.ui_registration.firstname.text()
        othername = self.ui_registration.othername.text()
        lastname = self.ui_registration.lastname.text()
        reference = self.ui_registration.reference.text()
        contact = self.ui_registration.contact.text()
        position = self.ui_registration.position.text()
        image = self.ui_registration.filename.text()
        return reference, firstname+' '+othername, lastname, contact, position, image

    def update_interfaces_with_details(self, details):
        name = str(details[2]).split(' ')
        self.ui_registration.firstname.setText(name[0])
        self.ui_registration.othername.setText(name[1])
        self.ui_registration.lastname.setText(details[3])
        self.ui_registration.reference.setText(details[1])
        self.ui_registration.contact.setText(details[4])
        self.ui_registration.position.setText(details[5])

    def reset_interface(self):
        self.ui_registration.firstname.setText('')
        self.ui_registration.othername.setText('')
        self.ui_registration.lastname.setText('')
        self.ui_registration.reference.setText('')
        self.ui_registration.contact.setText('')
        self.ui_registration.position.setText('')
        self.ui_registration.filename.setText('')
        self.ui_registration.image.setPixmap(u":/icons/asset/image.svg")
        self.ui_registration.image.setScaledContents(False)
        self.ui_registration.label_notification.setText("Notification")

    def browse_images(self): 
        file_type = "PNG Files(*.png);;JPG Files(*.jpg);;JPEG Files(*.jpeg)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Pictures",file_type)
        if path:
            self.ui_registration.filename.setText(path[0])
            self.ui_registration.image.setPixmap(QPixmap.fromImage(path[0]))
            self.ui_registration.image.setScaledContents(True)

    def database_path(self):
        return 'C:\\ProgramData\\weTrack\\database\\database.db'

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

   

    
