from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    con=sql.connect("databaseHW2.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        Name=request.form['Name']
        Id=request.form['Id']
        Points=request.form['Points']
        con=sql.connect("databaseHW2.db")
        cur=con.cursor()
        cur.execute("insert into students(Name,Id,Points) values (?,?,?)",(Name,Id,Points))
        con.commit()
        flash('Student entry has been successfully added.','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<int:Id>",methods=['POST','GET'])
def edit_user(Id):
    if request.method=='POST':
        Name=request.form['Name']
        Points=request.form['Points']
        con=sql.connect("databaseHW2.db")
        cur=con.cursor()
        cur.execute("update students set Name=?,Points=? where Id=?",(Name,Points,Id))
        con.commit()
        flash('User Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("databaseHW2.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students where Id=?",(Id,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    
@app.route("/delete_user/<int:Id>",methods=['GET'])
def delete_user(Id):
    con=sql.connect("databaseHW2.db")
    cur=con.cursor()
    cur.execute("delete from students where Id=?",(Id,))
    con.commit()
    flash('Student entry has been successfully deleted.','warning')
    return redirect(url_for("index"))

# for security purposes
if __name__=='__main__':
    app.secret_key='CMSC447SP2024'
    app.run(debug=True)