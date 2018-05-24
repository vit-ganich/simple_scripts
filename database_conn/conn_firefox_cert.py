# coding: utf8
import sqlite3          


def connector(db_path):
	'''
	The script returns the number of browser-urls
	without the mark "Unprotected connection".
	Returns answer "ex_code" 0 - success, 1 - error
	'''
    
    ex_code = 1
    try:
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        #  return ID of the Firefox (tuple). For example - ('1,')
        cursor.execute(r'SELECT browser_id FROM browsers WHERE browser_name = "Firefox"')
        browser_id = cursor.fetchall()[0][0]
        print(browser_id)
        
        #  return ID the number of protected urls
        cursor.execute(r'SELECT browser_url_url FROM browsers_urls WHERE browser_id = %s AND browser_url_title != "Незащищённое соединение"' % (browser_id))
        result = cursor.fetchall()
        print(len(result))
        # if the number of protected urls is more than zero - Test Passed
        if len(result) != 0:
            ex_code = 0
    except:
        ex_code = 1
    finally:
        with open(r'C:\Sikuli\db.log', 'a') as opened_file:
            opened_file.write(str(ex_code))


path_to_db = r"C:\ProgramData\Databases\NewDatabase.db"


connector(path_to_db)
