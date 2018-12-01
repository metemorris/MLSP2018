from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_book(name):
    query = "INSERT INTO atDoor(Person) VALUES('"+name+"')"
    args = name
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        print(query,args)
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   insert_book('Melissa')
 
if __name__ == '__main__':
    main()