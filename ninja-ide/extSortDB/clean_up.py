# clean up
import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='123'")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()

for j in range(4):
    cur.execute("DROP TABLE IF EXISTS INTRIM1_%s",[j])       
    cur.execute("DROP TABLE IF EXISTS INTRIM2_%s",[j])       

for j in range(20):
    cur.execute("DROP TABLE IF EXISTS TEST_%s",[j])
    cur.execute("DROP TABLE IF EXISTS SORTED_%s",[j])

cur.execute("DROP TABLE IF EXISTS TEST");
cur.execute("DROP TABLE IF EXISTS FINAL_SORTED");

conn.commit()

print("Clean_up Complete.")