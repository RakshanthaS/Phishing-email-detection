from flask import Flask, render_template
import sqlite3 as sql
app = Flask(__name__)
app.secret_key="randomstring"
con = sql.connect("email_db.db")
con.row_factory = sql.Row
cur = con.cursor()
cur.execute("select * from EMAIL")
rows = cur.fetchall(); 
@app.route('/')
def inbox():
    return render_template("inbox.html",rows = rows)

@app.route('/read_email/<int:id>')
def read_email(id):
    con = sql.connect("email_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from EMAIL where SL_NO = ?",(id,))
    rows = cur.fetchone();
    return render_template("read_email.html",rows = rows)
	
if __name__ == '__main__':
   app.run(debug=True)
   
