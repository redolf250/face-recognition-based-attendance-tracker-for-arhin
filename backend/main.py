################################################################################
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
################################################################################

from packages.pyqt import *
from packages.system import *
from packages.driver import *
from packages.globals import *
from packages.processing import *

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_dashboard()
        self.saveTimer = QTimer()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())    
        #########################################################################################

        #########################################################################################
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_close.clicked.connect(self.system_exit)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        # self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.reset_home_interface)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_summary.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.summary))
        self.ui.btn_batch_job.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.batch))
        ##########################################################################################################

        ############################################################################################
        self.database = Database()
        self.ui.btn_open_database.clicked.connect(lambda: self.database.show())
        self.database.combo_box(self.get_database_tables())

        self.registration = Registration()
        self.ui.btn_register.clicked.connect(lambda: self.registration.show())

        self.mail = Mail()
        self.ui.btn_send_mail.clicked.connect(lambda: self.mail.show())
        ############################################################################################

        ############################################################################################
        self.ui.btn_connect_detect.clicked.connect(self.start_application_webcam)
        self.ui.btn_disconnect.clicked.connect(self.stop_application_webcam)
        ############################################################################################

        #############################################################################################
        self.ui.btn_search_page.clicked.connect(self.query_database_for_data)
        self.ui.calendarWidget.selectionChanged.connect(self.get_date_on_search_page)
        self.ui.search_page_tables.addItems(self.get_database_tables())
        self.ui.btn_csv.clicked.connect(self.export_records_to_csv)
        self.ui.btn_backup.clicked.connect(self.backup_database)
        ##############################################################################################
        
        
        #####################################################################################################

        self.cordinates=cordinates_list
        self.reference=reference_list
    
        #################################################################################################
        self.ui.btn_scan_range.clicked.connect(self.camera_thread)
        self.ui.database_tables.addItems(self.get_database_tables())
        self.ui.database_summary.addItems(self.get_database_tables())
        self.ui.batch_table.addItems(self.get_database_tables())
        self.ui.btn_refresh.clicked.connect(self.refresh_tables)
        self.ui.btn_summary_load.clicked.connect(self.render_teacher_data)
        self.ui.btn_summary_save.clicked.connect(self.export_summary_data)
        self.ui.btn_summary_browse.clicked.connect(self.load_data_summary_exported_data)
        self.ui.btn_batch_browse.clicked.connect(self.load_batch_data)
        self.ui.btn_start_job.clicked.connect(self.start_insert_job)
        self.ui.menu_frame.hide()
        ##################################################################################################

    def system_exit(self):
        self.close()
        self.registration.close()
        self.database.close()

    def resource_path(self,relative_path):
        path_to_img= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path_to_img
        
    def start_insert_job(self):
        path = self.ui.batch_filename.text()
        db = sqlite3.connect(os.path.abspath(self.database_path()))
        my_cursor = db.cursor()
        table = self.ui.batch_table.currentText()
        if path:
            try:
                with open(path,'r') as filename:
                    data=csv.reader(filename)
                    next(data)
                    self.alert = AlertDialog()
                    self.alert.content("Please the header was skipped...")
                    self.alert.show()
                    for item in data:
                        time = item[5].split(':')
                        time_zone =time[1].split(' ')
                        time_transform = time[0]+':'+time_zone[0]+':'+'00 '+time_zone[1]
                        date = item[4].split('/')
                        date_transformed = datetime.date(int(date[2]),int(date[0]),int(date[1])).strftime('%Y-%m-%d')
                        item[5] = time_transform
                        item[4] = date_transformed
                        date=str(item[4]).split("-")
                        transform_date = datetime.date(int(date[0]),int(date[1]),int(date[2])).strftime("%a, %b %d, %Y")
                        my_cursor.execute(f"INSERT INTO {table} (reference,fullname,contact,date_stamp,time_stamp,attendance_status,date_stamp_,position) VALUES(?,?,?,?,?,?,?,?)",
                        (item[0],item[1],item[2],item[4],item[5],item[6],transform_date,item[3]))
                        self.ui.batch_notification.setText("Please records are been inserted....")
                    db.commit()
                    self.ui.batch_notification.setText("Please records inserted successfully....")          
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"+str(e)))
                self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! provide a file to load load from...")
            self.alert.show() 
        
    def load_batch_data(self):
        file_type = "CSV Files(*.csv);;Text Files(*.txt)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Documents",file_type)
        if path:
            self.ui.batch_filename.setText(path[0])
            try:
                results_list = []
                with open(path[0],'r') as filename:
                    data=csv.reader(filename)
                    next(data)
                    self.alert = AlertDialog()
                    self.alert.content("Please the header was skipped...")
                    self.alert.show()
                    for item in data:
                        time = item[5].split(':')
                        time_zone =time[1].split(' ')
                        date = item[4].split('/')
                        date_transformed = datetime.date(int(date[2]),int(date[0]),int(date[1])).strftime('%Y-%m-%d')
                        time_transform = time[0]+':'+time_zone[0]+':'+'00 '+time_zone[1]
                        item[5] = time_transform
                        item[4] = date_transformed
                        results_list.append(item)
                    self.batch_table(results_list)
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"+str(e)))
                self.alert.show()
        else:
            pass

    def batch_table(self, details:list):
        self.ui.batch_tableWidget.setAutoScroll(True)
        self.ui.batch_tableWidget.setAutoScrollMargin(2)
        self.ui.batch_tableWidget.setTabKeyNavigation(True)
        self.ui.batch_tableWidget.setColumnWidth(0,140)
        self.ui.batch_tableWidget.setColumnWidth(1,270)
        self.ui.batch_tableWidget.setColumnWidth(2,140)
        self.ui.batch_tableWidget.setColumnWidth(3,270)
        self.ui.batch_tableWidget.setColumnWidth(4,190)
        self.ui.batch_tableWidget.setColumnWidth(5,190)
        self.ui.batch_tableWidget.setColumnWidth(6,140)
        self.ui.batch_tableWidget.setRowCount(len(details))
        self.ui.batch_tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.batch_tableWidget.setItem(row_count,0,QTableWidgetItem(str(data[0])))
            self.ui.batch_tableWidget.setItem(row_count,1,QTableWidgetItem(str(data[1])))
            self.ui.batch_tableWidget.setItem(row_count,2,QTableWidgetItem(str(data[2])))
            self.ui.batch_tableWidget.setItem(row_count,3,QTableWidgetItem(str(data[3])))
            self.ui.batch_tableWidget.setItem(row_count,4,QTableWidgetItem(str(data[4])))
            self.ui.batch_tableWidget.setItem(row_count,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.ui.batch_tableWidget.setItem(row_count,6,QTableWidgetItem(str(data[6])))
            row_count = row_count+1

    def load_data_summary_exported_data(self):
        file_type = "CSV Files(*.csv);;Text Files(*.txt)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Documents",file_type)
        if path:
            try:
                self.ui.summary_browse.setText(os.path.basename(str(path[0])))
                with open(path[0],'r') as data:
                    self.alert = AlertDialog()
                    self.alert.content("Please the header was skipped...")
                    self.alert.show()
                    results_list = csv.reader(data)
                    next(results_list)
                    data_list = []
                    for row in results_list:
                        data_list.append(row)
                    if len(data_list):
                        self.summary_table(data_list)
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"))
                self.alert.show()
            return path[0]
        pass

    def export_summary_data(self):
        table=self.ui.tableWidget_summary.item(0,0)
        filename = self.ui.summary_filename.text()
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\weTrack\\export\\'+filename+date+'.csv'
        if table and filename:
            details=self.query_summary_data()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Fullname','Contact','Date stamp (Most Early)','Time stamp (Most Early)','Date stamp (Most Late)','Time stamp (Most Late)','Early Count','Late Count','Total Count'])
            self.alert = AlertDialog()
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! you have no data to export\nor provide filename...")
            self.alert.show()
        
    def render_teacher_data(self):
        self.summary_table(self.query_summary_data())

    def query_summary_data(self):
        table_name = self.ui.database_summary.currentText()
        results= self.query_database(f"SELECT DISTINCT reference FROM {table_name}")
        
        data = []
        early = []
        late = []
        transform = []
        early_data = []
        late_data = []
        early_status_ = "\'{}\'".format('Early')
        late_status_ = "\'{}\'".format('Late')
        for reference in range(len(results)):
            query_parameter="\'{}\'".format(str(results[reference][0]))
            data_list= self.query_database(f"SELECT fullname,contact,COUNT(attendance_status) as active FROM {table_name} WHERE reference={query_parameter} ORDER BY fullname DESC")
            early_status= self.query_database(f"SELECT COUNT(attendance_status) as active FROM {table_name} WHERE reference={query_parameter} AND attendance_status={early_status_} ORDER BY fullname DESC")
            late_status= self.query_database(f"SELECT COUNT(attendance_status) as active FROM {table_name} WHERE reference={query_parameter} AND attendance_status={late_status_}")
            early_result = self.query_database(f"SELECT date_stamp_,time_stamp FROM {table_name} WHERE reference={query_parameter} ORDER BY time_stamp ASC LIMIT 1")
            late_result = self.query_database(f"SELECT date_stamp_,time_stamp FROM {table_name} WHERE reference={query_parameter} ORDER BY time_stamp DESC LIMIT 1")
            data.append(data_list[0])
            early.append(early_status[0])
            late.append(late_status[0])
            early_data.append(early_result[0])
            late_data.append(late_result[0])
    
        for item in data:
            transform.append([str(item[0]),str(item[1]),str(early_data[data.index(item)][0]),
                str(early_data[data.index(item)][1]),str(late_data[data.index(item)][0]),
                str(late_data[data.index(item)][1]),str(early[data.index(item)][0]),
                str(late[data.index(item)][0]),str(item[2])])
        return transform

    def summary_table(self,details:list):
        self.ui.tableWidget_summary.setAutoScroll(True)
        self.ui.tableWidget_summary.setAutoScrollMargin(2)
        self.ui.tableWidget_summary.setTabKeyNavigation(True)
        self.ui.tableWidget_summary.setColumnWidth(0,270)
        self.ui.tableWidget_summary.setColumnWidth(2,180)
        self.ui.tableWidget_summary.setColumnWidth(3,120)
        self.ui.tableWidget_summary.setColumnWidth(4,180)
        self.ui.tableWidget_summary.setColumnWidth(5,120)
        self.ui.tableWidget_summary.setColumnWidth(6,120)
        self.ui.tableWidget_summary.setColumnWidth(7,120)
        self.ui.tableWidget_summary.setColumnWidth(8,110)
        self.ui.tableWidget_summary.setRowCount(len(details))
        self.ui.tableWidget_summary.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget_summary.setItem(row_count,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_summary.setItem(row_count,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.ui.tableWidget_summary.setItem(row_count,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.ui.tableWidget_summary.setItem(row_count,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.ui.tableWidget_summary.setItem(row_count,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget_summary.setItem(row_count,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.ui.tableWidget_summary.setItem(row_count,6,QtWidgets.QTableWidgetItem(str(data[6])))
            self.ui.tableWidget_summary.setItem(row_count,7,QtWidgets.QTableWidgetItem(str(data[7])))
            self.ui.tableWidget_summary.setItem(row_count,8,QtWidgets.QTableWidgetItem(str(data[8])))
            row_count = row_count+1

    def read_only_property(self):
        if self.ui.read_only_property.isChecked():
            self.ui.late_hour.setReadOnly(True)
            self.ui.late_minutes.setReadOnly(True)  
        else:
            self.ui.late_hour.setReadOnly(False)
            self.ui.late_minutes.setReadOnly(False)
       
    def refresh_tables(self):
        self.ui.database_tables.clear()
        self.ui.database_tables.addItems(self.get_database_tables())
        self.ui.search_page_tables.clear()
        self.ui.search_page_tables.addItems(self.get_database_tables())
        self.ui.batch_table.clear()
        self.ui.batch_table.addItems(self.get_database_tables())
        self.ui.database_summary.clear()
        self.ui.database_summary.addItems(self.get_database_tables())

    def database_path(self):
        return 'C:\\ProgramData\\weTrack\\database\\database.db'

    def get_database_tables(self):
        con = sqlite3.connect(self.database_path())
        cursor = con.cursor()
        sql = """SELECT name FROM sqlite_master WHERE type = 'table';"""
        my_cursor = cursor.execute(sql)
        my_cursor=my_cursor.fetchall()
        details = [v[0] for v in my_cursor if v[0] !='sqlite_sequence' and v[0] !='tb_details' and v[0] !='tb_encodings']
        return details

    def backup_history(self):
        path =Path('C:\\ProgramData\\weTrack\\backup\\backup_history.txt')
        path.touch(exist_ok=True)
        file = open(path)
        time =dt.now().time().strftime('%I:%M:%S %p')
        date=dt.now().date().strftime('%a %b %d %Y')
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n{date},{time}')
            file.close()         

    def backup_database(self):
        path='C:\\ProgramData\\weTrack\\backup'
        db_path = self.database_path()
        if os.path.exists(path):
            shutil.copy2(db_path,path)
            self.backup_history()
            self.alert = AlertDialog()
            self.alert.content("Database successfully backed up...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! something went wrong.....")
            self.alert.show()

    def clear_camera_comboBoxes(self):
        self.ui.comboBox.clear()

    def get_active_cameras(self,camera:list):
        self.ui.comboBox.addItems(camera)
        count = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
        self.ui.scan_range_label.setText("Active camera(s): "+str(len(count)))
        self.ui.label_notification.setText("Done scanning for available cameras...")           

    def camera_thread(self):
        scan_range = self.ui.scan_range.text()
        if scan_range:
            self.clear_camera_comboBoxes()
            self.ui.scan_range_label.setText('')
            self.active = ActiveCameras(scan_range)
            self.active.start()
            self.active.cameras.connect(self.get_active_cameras)
            self.ui.label_notification.setText("Scanning for available cameras...")
        else:
            self.alert_builder("Oops! no scan range provided...")
    
    def alert(self, content:str):
        self.alert = AlertDialog()
        self.alert.content(content)
        self.alert.show()
    
    def export_records_to_csv(self):
        table=self.ui.tableWidget.item(0,0)
        filename = self.ui.filename.text()
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\weTrack\\export\\'+filename+date+'.csv'
        if table and filename:
            details=self.query_database_for_data()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Reference','Name','Contact','Date_Stamp','Time_Stamp','Status'])
            self.alert = AlertDialog()
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! you have no data to export\nor provide filename...")
            self.alert.show()
        
    def query_database(self, query: str):
        db = sqlite3.connect(self.database_path())
        my_cursor = db.cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item)
        return details

    def table_search_page(self, details: list):
        self.ui.tableWidget.setAutoScroll(True)
        self.ui.tableWidget.setAutoScrollMargin(2)
        self.ui.tableWidget.setTabKeyNavigation(True)
        self.ui.tableWidget.setColumnWidth(1,230)
        self.ui.tableWidget.setRowCount(len(details))
        self.ui.tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget.setItem(row_count,0,QTableWidgetItem(str(data[1])))
            self.ui.tableWidget.setItem(row_count,1,QTableWidgetItem(str(data[2])))
            self.ui.tableWidget.setItem(row_count,2,QTableWidgetItem(str(data[3])))
            self.ui.tableWidget.setItem(row_count,3,QTableWidgetItem(str(data[7])))
            self.ui.tableWidget.setItem(row_count,4,QTableWidgetItem(str(data[5])))
            self.ui.tableWidget.setItem(row_count,5,QTableWidgetItem(str(data[6])))
            self.ui.tableWidget.setItem(row_count,6,QTableWidgetItem(str(data[8])))
            row_count = row_count+1
    
    def render_details_on_card_view(self):
        try:
            table = self.ui.database_tables.currentText()
            results=self.query_database(f"SELECT * FROM {table} WHERE reference={str(self.ui.search_box.text())}")
            self.table_search_page(results)
            if self.ui.search_box.text():
                db_data=self.query_database_by_reference(self.ui.search_box.text())
                if len(db_data) > 0:
                    helper = str(db_data[2]).split(" ")
                    self.ui.db_firstname.setText(helper[0])
                    self.ui.db_middlename.setText(helper[1])
                    self.ui.db_lastname.setText(helper[2])
                    self.ui.db_refrence.setText(str(db_data[1]))
                    self.ui.db_contact.setText(str(db_data[3]))
                    self.ui.db_status.setText(str(db_data[6]))
                    self.ui.db_incharge.setText(db_data[8])
                    path=f'C:\\ProgramData\\weTrack\\images\\{db_data[1]}.png' 
                    self.ui.db_image_data.setPixmap(QPixmap.fromImage(path))
                    self.ui.db_image_data.setScaledContents(True)  
                else:
                    self.alert_builder("Details not found. Please enter\nyour details to register!")   
            else:
                self.alert_builder("Oops! search field can't be empty.")
        except:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid search parameter...")
            self.alert.show()
    
    def query_database_by_reference(self,reference):
        db = sqlite3.connect(self.database_path())
        my_cursor = db.cursor()
        table = self.ui.database_tables.currentText()
        detail =my_cursor.execute(f"SELECT * FROM {table} WHERE reference={reference}")
        detail= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
        return db_data

    def query_database_for_data(self):
        table=self.ui.search_page_tables.currentText()
        if self.ui.db_start_date.text():
            current_date = self.ui.db_start_date.text()
            current_date = "\'{}\'".format(current_date)
            results = self.query_database(f"SELECT * FROM {table} WHERE date_stamp ={current_date}")
            details = self.query_database(f"SELECT reference,fullname,contact,date_stamp_,time_stamp,attendance_status FROM {table} WHERE date_stamp ={current_date}")
            self.table_search_page(results)
            return details
        elif self.ui.search_box.text():
            self.render_details_on_card_view()
            details=self.query_database(f"SELECT reference,fullname,contact,date_stamp_,time_stamp,attendance_status FROM {table} WHERE reference={str(self.ui.search_box.text())}")
            return details
        else:
            details=self.query_database(f"SELECT * FROM {table}")
            results=self.query_database(f"SELECT reference,fullname,contact,date_stamp_,time_stamp,attendance_status FROM {table}")
            self.table_search_page(details)
            return results                        

    def get_date_on_search_page(self):
        date = self.ui.calendarWidget.selectedDate()
        self.ui.db_start_date.setText(str(date.toPython()))
   
    def alert_builder(self, message:str):
        self.alert = AlertDialog()
        self.alert.content(message)
        self.alert.show()
        
    def reset_home_interface(self):
        self.ui.firstname.setText("Firtname")
        self.ui.othername.setText("Othename")
        self.ui.lastname.setText("Lastname")
        self.ui.reference.setText("Reference")
        self.ui.contact.setText("Contact")
        self.ui.position.setText("Position")
        self.ui.status.setText("Status")
        self.ui.image.setPixmap(u":/icons/asset/image.svg")
        self.ui.image.setScaledContents(False)
        self.ui.label_notification.setText("Notification")

    def retreive_details(self, query: str):
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

    def render_details(self,reference):
        reference="\'{}\'".format(reference)
        details = self.retreive_details(f"SELECT * FROM tb_details WHERE reference={reference}")
        if details:
            name = str(details[2]).split(' ')
            self.ui.firstname.setText(name[0])
            self.ui.othername.setText(name[1])
            self.ui.lastname.setText(details[3])
            self.ui.reference.setText(details[1])
            self.ui.contact.setText(details[4])
            self.ui.position.setText(str(details[5]))
            path=f'C:\\ProgramData\\weTrack\\images\\{details[1]}.png'
            self.ui.image.setPixmap(QPixmap.fromImage(path))
            self.ui.image.setScaledContents(True)
        else:
            self.reset_home_interface()
                        
    def get_attendance_data(self):
        name = self.ui.firstname.text()+" "+self.ui.othername.text()+" "+self.ui.lastname.text()
        attendance = Attendance(
            self.ui.reference.text(),
            name,
            self.ui.contact.text(),
            str(dt.now().date().strftime("%Y-%m-%d")),
            str(dt.now().time().strftime("%I:%M:%S %p")),
            self.ui.status.text(),
            str(dt.now().date().strftime("%a, %b %d, %Y")),
            self.ui.position.text()
            )  
        return attendance              

    def take_attendance(self):
        db = sqlite3.connect(os.path.abspath(self.database_path()))
        my_cursor = db.cursor()
        table = self.ui.database_tables.currentText()
        hour=int(dt.now().time().strftime("%I"))
        minute=int(dt.now().time().strftime("%M"))
        type=str(dt.now().time().strftime("%p"))
        late_hour=self.ui.late_hour.value()
        late_minute=self.ui.late_minutes.value()

        if hour<=late_hour and minute<=late_minute and type == self.ui.time_zone.currentText():
            self.ui.status.setText("Early")
            attendance=self.get_attendance_data()
        else:
            self.ui.status.setText("Late")
            attendance=self.get_attendance_data()
            
        details = []
        date="\'{}\'".format(dt.now().date().strftime("%Y-%m-%d"))
        if self.ui.reference.text() != "Reference" and self.ui.reference.text() !="":
            data=my_cursor.execute(f"SELECT reference,date_stamp FROM {table} WHERE reference={self.ui.reference.text()} AND date_stamp={date}")
            data=my_cursor.fetchone()
            if data:
                for detail in data:
                    details.append(detail)
                db.commit() 
            if not details:
                my_cursor.execute(f"INSERT INTO {table} (reference,fullname,contact,date_stamp,time_stamp,attendance_status,date_stamp_,position) VALUES(?,?,?,?,?,?,?,?)",
                (attendance.reference,attendance.fullname,attendance.contact,attendance.date_stamp,attendance.time_stamp,attendance.attendance_status,attendance.date_formated,attendance.position))
                db.commit()
            elif details:
                winsound.Beep(1000,100)
                self.show_info("Attendance taken, you can proceed!\nNext person please...")
            else:
                self.show_info("Oops! something went wrong...")
        db.close()
 
    def start_application_webcam(self):
        if self.ui.camera_ip.text() or self.ui.comboBox.currentText():
            ip_address = self.ui.camera_ip.text()
            system_attached_camera = self.ui.comboBox.currentText()
            self.network_capture = VideoCapture(ip_address)
            camera_id = int(system_attached_camera)
            self.system_capture = VideoCapture(camera_id)

            if ip_address:  
                if self.network_capture is None or not self.network_capture.isOpened():    
                    self.stop_application_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                    self.show_alert.show()
                else:
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(ip_address)
                
            elif system_attached_camera:       
                if self.system_capture is None or not self.system_capture.isOpened():    
                    self.stop_application_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                    self.show_alert.show()
                else:
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(camera_id) 
                        
            elif self.system_capture.isOpened() and self.network_capture.isOpened():
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(camera_id)

            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.saveTimer.timeout.connect(self.update_webcam_frame)
            self.saveTimer.start(3)
        else:
            self.show_alert = AlertDialog()
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()

    def update_webcam_frame(self):

        thickness = 2
        rectangle_thickness = 1
        color = (255,255,0)
        ret,self.frame = self.capture.read()
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        curent_frame_face = face_recognition.face_locations(gray)
        curent_frame_encode = face_recognition.face_encodings(self.frame,num_jitters=1,model="small")

        self.result= self.frame
        self.read_only_property()
        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(85,85,85),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.now = dt.now()
        self.now = self.now.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.now,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(85,85,85),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

        for encode_face, face_location in zip(curent_frame_encode, curent_frame_face):
            (left,bottom,right,top) = face_location
            cv2.rectangle(self.result, (top,left), (bottom,right), (255,255,0), rectangle_thickness)
            cv2.line(self.result,(top,left),(top+15,left),color,thickness)
            cv2.line(self.result,(top,left),(top,left+15),color,thickness)
            cv2.line(self.result,(bottom,left),(bottom-15,left),color,thickness)
            cv2.line(self.result,(bottom,left),(bottom,left+15),color,thickness)
            cv2.line(self.result,(top,right),(top+15,right),color,thickness)
            cv2.line(self.result,(top,right),(top,right-15),color,thickness)
            cv2.line(self.result,(bottom,right),(bottom-15,right),color,thickness)
            cv2.line(self.result,(bottom,right),(bottom,right-15),color,thickness)

            matches = face_recognition.compare_faces(self.cordinates, encode_face)
            face_distance = face_recognition.face_distance(self.cordinates, encode_face)
            match_index = np.argmin(face_distance)
            if matches[match_index]:
                reference = self.reference[match_index]
                self.render_details(reference)
                self.take_attendance()
            else:
                self.reset_home_interface()
                self.show_info("Oops! no record found for current face...")  
        self.display_webcam_feed(self.result,1)         
        
    def display_webcam_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_view.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui.camera_view.setScaledContents(True)
        
    def stop_application_webcam(self):
        self.show_alert = AlertDialog()
        if self.saveTimer.isActive():
            self.show_alert.content("Hey! wait a second while system\nrelease camera") 
            self.show_alert.show()
            self.ui.camera_view.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui.camera_view.setScaledContents(False)
            self.saveTimer.stop() 
        else:
            self.show_alert.content("Oops! you have no active camera\nto disconnect from.") 
            self.show_alert.show()  

    def show_info(self, content:str):
        self.ui.label_notification.setText(content)         
    
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()    
   
class Launcher(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_MainWindow()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)
        self.create_aplication_working_directory()
        self.create_database_table()
        self.create_default_database()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()
        global cordinates_list
        global reference_list
        cordinates_list = self.load_all_face_ecodings()
        reference_list = self.load_all_reference_numbers()

    def create_database_table(self):
        db = sqlite3.connect(self.database_path())
        db.execute(create_tb_details())
        db.execute(create_tb_encodings())
        db.commit()
        db.close()

    def create_default_database(self):
        con = sqlite3.connect(self.database_path())
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tb_attendance_default(generated_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,reference TEXT,fullname TEXT, contact TEXT,date_stamp TEXT, time_stamp TEXT,attendance_status TEXT,date_stamp_ TEXT,position TEXT)")  
        con.commit()

    def database_path(self):
        return 'C:\\ProgramData\\weTrack\\database\\database.db'

    def create_aplication_working_directory(self):
        root_dir = 'C:\\ProgramData\\weTrack\\'
        list =('export','backup','mailing','database','images')
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
        for item in list:
            path = os.path.join(root_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
        self.create_application_files()

    def load_all_face_ecodings(self):
        cordinates=self.query_database("SELECT face_encoding FROM tb_encodings")
        cordinates_list = []
        for coordinate in range(len(cordinates)):
            cordinates_list.append(eval(cordinates[coordinate][0]))
        return cordinates_list

    def load_all_reference_numbers(self):
        references= self.query_database("SELECT reference FROM tb_encodings")
        reference_list = []
        for reference in range(len(references)):
            reference_list.append(references[reference][0])
        return reference_list

    def query_database(self, query: str):
        db = sqlite3.connect(self.database_path())
        my_cursor = db.cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item)
        return details

    def create_application_files(self):
        mail_credentials = {
                "sender": "Sender",
                "subject": "Subject",
                "mail": "example@example.com",
                "password": "Password"
                }
        details_path =Path('C:\\ProgramData\\weTrack\\mailing\\mailing_credentials.json')
        path =Path(details_path)
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                if os.path.getsize(path)==0:
                    json.dump(mail_credentials,file,indent=2)
    
            file.close()

        report_content = """
        Hello name,
    	        Please attached to this message is the
            report or data you requested for. Feel free 
            to contact us for our services at anytime.
                                        Thank you! """
        content_path =Path('C:\\ProgramData\\weTrack\\mailing\\report_body.txt')
        content_path.touch(exist_ok=True)
        content_file = open(content_path)
        if os.path.exists(content_path):
            with open(content_path,'a+') as content_file:
                if  os.path.getsize(content_path)==0:
                    content_file.write(report_content)
            content_file.close()

    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop() 
            self.close() 
            self.main = MainWindow()
            self.main.show()        
        counter +=1

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Launcher()  
    sys.exit(application.exec_()) 