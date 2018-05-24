import sqlite3          



def connector(db_path, act_result, result = []):	
	"""
	Fetches data from database and compares it with pattern
	"""

    ex_code = 1
    #  foo returns answer "ex_code" 0 - success, 1 - error, 2 - success, but attention required
    try:
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        #  get the list of sent files
        cursor.execute("SELECT conv_file_fname FROM conv_files ORDER BY conv_file_id")
        result = cursor.fetchall()
        #  if the number of intercepted files in DB == number of sent files - Test Passed! 
        if len(result) == act_result:
            ex_code = 0 #  test passed!
        elif len(result) != act_result and len(result) > 0:
            ex_code = 2 #  test passed, but attention required
    except:
        ex_code = 1 #  test failed!
        
    finally:
        print(ex_code)
        with open(r'C:\Sikuli\log_DEBUG.txt', 'a') as log_file:
            # Write a number of intercepted files and their names
            log_file.write("\n------ Messenger files: %s ------\n %s\n" % (len(result), result))


number_of_sent_messages = 5
path_to_db = r"C:\ProgramData\Databases\NewDatabase.db"


connector(path_to_db, number_of_sent_messages)