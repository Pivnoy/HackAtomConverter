import psycopg2
import time
from Algo.lang_process import text_processing

con = psycopg2.connect(
    database="anna",
    user="anna",
    password="",
    host="127.0.0.1",
    port="5432"
)

cursor = con.cursor()

while True:
    cursor.execute("SELECT * FROM TAB WHERE proc=FALSE")
    rows = cursor.fetchall()
    for row in rows:
        cursor.execute("UPDATE TAB SET proc = TRUE WHERE id = %s", [row[0]])
        print('Start processing', row[2])
        all_text = text_processing('../'+row[2])
        print('End processing')
        cursor.execute("INSERT INTO TEXT VALUES (%s, %s, FALSE)", (row[0], all_text))
        con.commit()