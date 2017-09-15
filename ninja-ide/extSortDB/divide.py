# creating tukde
# break-down of table 'TEST' in database 'POSTGRES'
import psycopg2

def partition(cur,conn,no_parts,part_size):
    for j in range(no_parts):
        cur.execute("CREATE TABLE IF NOT EXISTS TEST_%s (INDEX INTEGER, VALUE INTEGER, PRIMARY KEY(INDEX))",[j])
        cur.execute("TRUNCATE TABLE TEST_%s",[j])
    
    for j in range(no_parts):
        cur.execute("INSERT INTO TEST_%s (INDEX,VALUE) (SELECT INDEX,VALUE FROM TEST WHERE INDEX > %s  AND INDEX <= %s)",(j,j*part_size,(j+1)*part_size))
    
    conn.commit()
    
#    print("Table TEST is broken down into ",no_parts,"tables as TEST_(0,1,...,9).")