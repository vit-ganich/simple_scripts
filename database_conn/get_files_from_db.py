# coding utf-8
import sqlite3


def get_from_db(db_path, file_name):
	"""
	Gets files IDs from database and saves them into selected folder
	"""

        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        #  fetch files IDs
        files_id =[item[0] for item in cursor.execute("SELECT printer_doc_id FROM printers_prints ORDER BY printer_doc_id")]
        print(files_id)
        cursor.close()
        
        counter = 0
        #  fetch files from DB and save them in folder
        while counter < len(files_id):
            with open('%s-%s.%s' %(file_name, str(counter),'.pdf'), "wb") as output_file:
                fid = str(counter+1) 			      			    
                connect = sqlite3.connect(db_path)
                cursor = connect.cursor()
                cursor.execute("SELECT printer_print_data FROM printers_prints WHERE printer_doc_id = %s" % fid)
                ablob = cursor.fetchone()
                output_file.write(ablob[0])
                cursor.close()
            counter += 1


db_path = "C:\\ProgramData\\Databases\\DefaultDatabase_00.db"
file_name = "file"

get_from_db(db_path, file_name)