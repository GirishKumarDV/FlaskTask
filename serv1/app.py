from flask import Flask,redirect,url_for,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:5000/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Tasks(db.Model):
    id = db.Column("id",db.Integer, primary_key=True)
    title = db.Column("title",db.String(100))
    stack = db.Column("stack",db.String(120))
    mentors = db.Column("mentors",db.String(120))

    def __init__(self,title,stack,mentors):
        self.title = title
        self.stack = stack
        self.mentors = mentors

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        title = request.form['title']
        stack = request.form['stack']
        mentor = request.form['mentors']
        task = Tasks(title=title,stack=stack,mentors=mentor)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("viewTasks"))
    else:
        return render_template("index.html")
 
@app.route("/tasks")
def viewTasks():
    tasks = Tasks.query.order_by(Tasks.id).all()
    return render_template("tasks.html",content = {'tasks':tasks,'count':len(tasks)})


if __name__=="__main__":
    app.run(debug=True)