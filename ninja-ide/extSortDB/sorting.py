# sorting tukde
import psycopg2
import sorts as s

def sorter(cur,conn,no_parts,part_size):
    for j in range(no_parts):
        cur.execute("CREATE TABLE IF NOT EXISTS SORTED_%s (INDEX INTEGER,VALUE INTEGER)",[j])
        cur.execute("SELECT VALUE FROM TEST_%s",[j])
        rows = cur.fetchall()
        sorts = s.insertion_sort(rows)
        for i in range(len(sorts)):
            cur.execute("INSERT INTO SORTED_%s (INDEX,VALUE) VALUES (%s,%s)",(j,i+1,sorts[i]))
    
    conn.commit()
    
#    print("Tables sorted and stored in SORTED_(0,1,...,9).")