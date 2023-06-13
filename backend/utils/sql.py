def create_tb_details():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_details(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference varchar(10) NOT NULL UNIQUE,
            firstname varchar(50) NOT NULL,
            lastname varchar(25) NOT NULL,
            contact varchar(12) NOT NULL UNIQUE,
            position varchar(50) NOT NULL
            )
        """
    return sql

def create_tb_encodings():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_encodings(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference varchar(10) NOT NULL UNIQUE,
            face_encoding TEXT NOT NULL,
            FOREIGN KEY(reference) REFERENCES tb_details(reference) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """
    return sql