from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

# Sample data for classrooms
classrooms = [
    {"name": "Math 101", "yearlevel": "Freshman", "capacity": 30},
    {"name": "Science 102", "yearlevel": "Sophomore", "capacity": 25},
    {"name": "History 201", "yearlevel": "Junior", "capacity": 20},
    {"name": "English 202", "yearlevel": "Senior", "capacity": 28}
]

@app.route("/")
def home():
  data = "Test sentence written in app.py"
  return render_template("index.html", data=data)

@app.route("/create", methods=('GET', 'POST'))
def create():
    return render_template('create.html')

@app.route('/view')
def view():
    return render_template('view.html', classrooms = classrooms)

@app.route('/update')
def update():
    return render_template('update.html')

# Running the app in development mode
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)