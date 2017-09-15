#merging all sorted data
# copy merge code from filesystem code
import sys

def merge1(cur,conn,no_parts,part_size,init,intr):

    cur.execute("CREATE TABLE IF NOT EXISTS INTRIM1_%s(INDEX INTEGER,VALUE INTEGER, PRIMARY KEY(INDEX))",[intr])
    cur.execute("TRUNCATE TABLE INTRIM1_%s",[intr])
    
    count = [1]*no_parts
    val = [0]*no_parts
    cnt = 1
    
    for j in range(no_parts):
        cur.execute("SELECT VALUE FROM SORTED_%s",[j+init])
        row = cur.fetchone()
        val[j] = row[0]

    while True:
        
        if(min(count) == part_size):
            break
    
        for i in range(no_parts):
            if(val[i] <= min(val) and val[i] != sys.maxsize ):
                cur.execute("INSERT INTO INTRIM1_%s(INDEX,VALUE) VALUES (%s,%s)",(intr,cnt,val[i],))
                count[i] = count[i]+1
                cnt = cnt+1

                if(count[i] <= part_size):
                    cur.execute("SELECT INDEX,VALUE FROM SORTED_%s WHERE INDEX = %s",(i+init,count[i],))
                    row = cur.fetchone()
                    val[i] = row[1]
                else:
                    val[i] = sys.maxsize 

    cur.execute("INSERT INTO INTRIM1_%s(INDEX,VALUE) VALUES (%s,%s)",(intr,cnt,val[i],))
    conn.commit() 
    print("The sorted data is stored in table INTRIM1_",intr)



def merge2(cur,conn,no_parts,part_size,init,intr):

    cur.execute("CREATE TABLE IF NOT EXISTS INTRIM2_%s(INDEX INTEGER,VALUE INTEGER, PRIMARY KEY(INDEX))",[intr])
    cur.execute("TRUNCATE TABLE INTRIM2_%s",[intr])
    
    count = [1]*no_parts
    val = [0]*no_parts
    cnt = 1
    
    for j in range(no_parts):
        cur.execute("SELECT VALUE FROM INTRIM1_%s",[j+init])
        row = cur.fetchone()
        val[j] = row[0]

    while True:
        
        if(min(count) == part_size):
            break
    
        for i in range(no_parts):
            if(val[i] <= min(val) and val[i] != sys.maxsize ):
                cur.execute("INSERT INTO INTRIM2_%s(INDEX,VALUE) VALUES (%s,%s)",(intr,cnt,val[i],))
                count[i] = count[i]+1
                cnt = cnt+1

                if(count[i] <= part_size):
                    cur.execute("SELECT INDEX,VALUE FROM INTRIM1_%s WHERE INDEX = %s",(i+init,count[i],))
                    row = cur.fetchone()
                    val[i] = row[1]
                else:
                    val[i] = sys.maxsize 

    cur.execute("INSERT INTO INTRIM2_%s(INDEX,VALUE) VALUES (%s,%s)",(intr,cnt,val[i],))
    conn.commit() 
    print("The sorted data is stored in table INTRIM2_",intr)


def merge3(cur,conn,no_parts,part_size):

    cur.execute("CREATE TABLE IF NOT EXISTS FINAL_SORTED(INDEX INTEGER,VALUE INTEGER, PRIMARY KEY(INDEX))")
    cur.execute("TRUNCATE TABLE FINAL_SORTED")
    
    count = [1]*no_parts
    val = [0]*no_parts
    cnt = 1
    
    for j in range(no_parts):
        cur.execute("SELECT VALUE FROM INTRIM2_%s",[j])
        row = cur.fetchone()
        val[j] = row[0]

    while True:
        
        if(min(count) == part_size):
            break
    
        for i in range(no_parts):
            if(val[i] <= min(val) and val[i] != sys.maxsize ):
                cur.execute("INSERT INTO FINAL_SORTED(INDEX,VALUE) VALUES (%s,%s)",(cnt,val[i]))
                count[i] = count[i]+1
                cnt = cnt+1

                if(count[i] <= part_size):
                    cur.execute("SELECT INDEX,VALUE FROM INTRIM2_%s WHERE INDEX = %s",(i,count[i],))
                    row = cur.fetchone()
                    val[i] = row[1]
                else:
                    val[i] = sys.maxsize 

    cur.execute("INSERT INTO FINAL_SORTED(INDEX,VALUE) VALUES (%s,%s)",(cnt,val[i],))
    conn.commit() 
    print("The sorted data is stored in table FINAL_SORTED.")