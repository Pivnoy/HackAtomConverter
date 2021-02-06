import psycopg2

con = psycopg2.connect(
    database="anna",
    user="anna",
    password="",
    host="127.0.0.1",
    port="5432"
)

cursor = con.cursor()

while True:
    cursor.execute("SELECT * FROM TEXT WHERE proc=FALSE")
    rows = cursor.fetchall()
    for row in rows:
        base_text = row[1]
        fileName = '../OutputFiles/' + str(row[0]) + '.txt'
        file = open(fileName, 'w')
        file.write(base_text)
        file.close()
        cursor.execute("UPDATE TEXT SET proc = TRUE WHERE id = %s", [row[0]])
        con.commit()

