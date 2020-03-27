import sqlite3, re

conn = sqlite3.connect('step104.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file VARCHAR(50) \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('step104.db')
with conn:
    cur = conn.cursor()
    fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
    for file in fileList:
        if re.search('.+txt', file):
            cur.execute("INSERT INTO tbl_txtFiles(col_file) VALUES (?)", \
                  (file,))
            conn.commit()       
conn.close()


conn = sqlite3.connect('step104.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_txtFiles")
    varFile = cur.fetchall()
    for file in varFile:
        msg = "{}".format(file[1])
        print(msg)
conn.close()
