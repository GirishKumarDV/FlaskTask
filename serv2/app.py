from flask import Flask,redirect,url_for,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,relationship
app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@db/task_db', pool_timeout=20, pool_recycle=299)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()



class Users(db.Model):
    id = db.Column("id",db.Integer, primary_key=True)
    u_name = db.Column("u_name",db.String(100))
    
    def __init__(self,name):
        self.u_name = name

class Tasks(db.Model):
    id = db.Column("id",db.Integer, primary_key=True)
    title = db.Column("title",db.String(100))
    stack = db.Column("stack",db.String(120))
    mentors = db.Column("mentors",db.String(120))
    def __init__(self,title,stack,mentors):
        self.title = title
        self.stack = stack
        self.mentors = mentors

db.create_all()
@app.route("/",methods=['GET','POST'])
def register():
    if request.method == "POST":
        uname = request.form['name']
        user = Users(name=uname)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("assignedTasks",usr=user.id))
    else:
        return render_template('register.html')

@app.route("/assignedTasks/<usr>")
def assignedTasks(usr):
    tasks = Tasks.query.order_by(Tasks.id).all()
    user = Users.query.get(usr)
    return render_template("tasks.html",content={'tasks':tasks,'user':user})


if __name__=="__main__":
    app.run(debug=True)
