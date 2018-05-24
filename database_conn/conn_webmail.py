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
        #  get tte list of sent emails
        cursor.execute("SELECT httpsess_mail_id FROM httpsess_mail WHERE httpsess_mail_subject = 'autotest'")
        result = cursor.fetchall()
        #  if the number of intercepted emails in DB >= number of sent emails - Test Passed! 
        if len(result) == act_result:
            ex_code = 0 #  test passed!
        elif len(result) != act_result and len(result) > 0:
            ex_code = 2 #  test passed, but attention required
    except:
        ex_code = 1 #  test failed!
        
    finally:
        print(ex_code)
        with open(r'C:\Sikuli\log_DEBUG.txt', 'a') as log_file:
                log_file.write("------ Web-mail. Intercepted emails: %s\n\n" % len(result))


number_of_sent_emails = 3
path_to_db = r"C:\ProgramData\Databases\NewDatabase.db"


connector(path_to_db, number_of_sent_emails)