import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='123'")
    except:
        print ("I am unable to connect to the database")
    
    cur = conn.cursor()
    conn.commit()
    return(cur,conn)    