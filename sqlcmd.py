import mysql.connector as mysql

def createdatabase(sqlcommand):
    database = mysql
    cur = database.cursor(prepared=True)
    cmd = sqlcommand
    cur.execute('''{}''').format(cmd)
