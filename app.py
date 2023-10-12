from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'System Engineer',
    'location': 'Delhi, NCR',
    'salary': 'Rs 4,50,000',
    'company': 'Tata Consultancy Services',
  },
    {
    'id':2,
    'title': 'Associate System Engineer',
    'location': 'Delhi, NCR',
    'salary': 'Rs 3,50,000',
    'company': 'Tata Consultancy Services',
  },
  {
    'id': 3,
    'title': 'Developer',
    'location': 'Pune',
    'salary': 'Rs 7,50,000',
    'company': 'Tata Consultancy Services',
  },
  {
    'id': 4,
    'title': 'IT Analyst',
    'location': 'Remote, India',
    'company': 'Tata Consultancy Services',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
