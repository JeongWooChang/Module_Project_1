import os, csv, datetime
import socket, sys
import subprocess
import sqlite3


def get_chrome_history():
    history_path = 'C:\\Users\\' +os.getlogin()+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
    con = sqlite3.connect(history_path)
    cursor = con.cursor()

    q = """ 
        SELECT title,datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime') \
                       FROM urls where last_visit_time >= ? order by last_visit_time asc
        """
    cur_time = (datetime.datetime(2021,
                                  datetime.datetime.today().month,
                                  datetime.datetime.today().day,
                                  9,
                                  0
                                  ).timestamp()+11644473600)*1000000


    cursor.execute(q,(cur_time,))
    urls = cursor.fetchall()
    try:
        with open('web_history.csv', 'w', newline='', encoding='utf8') as hist:
            history_writer = csv.writer(hist)
            for line in urls:
                history_writer.writerow(line)
        print('chrome history parsing complete')

    except Exception as e:
        print('chrome history parsing error')
        print(e)
        sys.exit()

def connection():
    try:
        s = socket.socket()

        host = 'localhost'
        port = 9999
        
        s.connect((host,port))
        try:
            with open('web_history.csv','rb') as f:
                data = f.read(1024)
                while data:
                    s.sendall(data)
                    data = f.read(1024)

            print('file transfer complete')
        except Exception as e:
            print('file transfer error')
            print(e)

        

    except Exception as e:
        s.close()
        print('Connection Close')
        sys.exit()

if __name__ == '__main__':
    get_chrome_history()
    connection()
