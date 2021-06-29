import socket, sys, csv
import crawling_csv as cr

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as err:
        print('socket create err : ' + str(err))

def socket_bind():
    try:
        global host
        global port
        global s
        print('bind socket to port : ' + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as err:
        print('socket create err : ' + str(err))
        # print('retry...')
        # socket_bind()

def socket_accept():
    conn, addr = s.accept()
    print('connection success')
    print('ip : ' + addr[0] + ' / port : ' + str(addr[1]))
    csv_transfer(conn)
    
    conn.close()


def csv_transfer(conn):
    data = conn.recv(1024)
    if not data:
        print("no data")
        sys.exit()
    with open('web_history.csv', 'wb') as f:
        try:
            while data:
                f.write(data)
                data = conn.recv(1024)
        except Exception as e:
            print(e)
    print('csv file ready')

def history_process():
    
    good_things=[]
    bad_things=[]



    with open('web_history.csv','r', encoding='utf-8') as file:
        datas = csv.reader(file)
        
    # '클라우드' or '도커' or 'Splunk' or 'sql' or 'SQL' or 'Python' or '파이썬'
        for row in datas:
            if '클라우드' in row[0] or '도커' in row[0] or 'Splunk' in row[0] or 'sql' in row[0] or\
                'SQL' in row[0] or 'Python'in row[0] or '파이썬' in row[0] or 'splunk' in row[0] or 'vscode' in row[0] or\
                    '스플렁크' in row[0] or 'php' in row[0] or 'Kali' in row[0] or 'kali' in row[0] or 'Sql' in row[0] or 'vscode' in row[0] or\
                        'docker' in row[0] or 'Stack' in row[0] or 'python' in row[0] or 'Php' in row[0] or 'Window'in row[0] or\
                            '윈도우' in row[0] or 'db' in row[0] or 'localhost' in row[0] or 'PHP' in row[0] or 'HTML' in row[0]:
                good_things.append((row[0],row[1],))
            else: 
                bad_things.append((row[0],row[1],))

    cr.db_update(good_things,bad_things)

    print('db update complete')


def main():
    socket_create()
    socket_bind()
    socket_accept()
    history_process()
    

if __name__ == '__main__':
    main()
