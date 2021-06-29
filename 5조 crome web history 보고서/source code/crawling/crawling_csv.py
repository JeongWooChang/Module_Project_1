import csv
import pymysql

print("run crawling_csv.py")
def db_update(good_things:list, bad_things:list):
    try:
        with pymysql.connect(
        host="db",
        port=3306,
        user="devuser",
        password="devpass", 
        charset="utf8", 
        database="test_db"
        )as connection:
            with connection.cursor() as cursor:
                create_goodhistory_table ="""
                    create table if not exists goodhistory(
                        id int auto_increment primary key,
                        contents varchar(500),
                        time varchar(100)
                    );
                """
                create_badhistory_table ="""
                    create table if not exists badhistory(
                        id int auto_increment primary key,
                        contents varchar(500),
                        time varchar(100)
                    );
                """

                insert_good= """
                    insert into goodhistory (contents, time)
                    values (%s, %s)
                """
                insert_bad = """
                    insert into badhistory (contents, time)
                    values (%s, %s)
                """
                
                cursor.execute(create_goodhistory_table)
                cursor.execute(create_badhistory_table)
                connection.commit()

                print(good_things)
                print("*" * 10)
                for s in good_things: 
                    print(s)
                    cursor.execute(insert_good, s)
                    



                cursor.executemany(insert_bad, bad_things)
                print(">>>> g")
                connection.commit()
                q = 'select * from quotes'
                cursor.execute(q)
                test = cursor.fetchall()
                for line in test:
                    print(line)

    except Exception as e:
        print(e)
