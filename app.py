from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'System Engineer',
#     'location': 'Delhi, NCR',
#     'salary': 'Rs 4,50,000',
#     'company': 'Tata Consultancy Services',
#   },
#     {
#     'id':2,
#     'title': 'Associate System Engineer',
#     'location': 'Delhi, NCR',
#     'salary': 'Rs 3,50,000',
#     'company': 'Tata Consultancy Services',
#   },
#   {
#     'id': 3,
#     'title': 'Developer',
#     'location': 'Pune',
#     'salary': 'Rs 7,50,000',
#     'company': 'Tata Consultancy Services',
#   },
#   {
#     'id': 4,
#     'title': 'IT Analyst',
#     'location': 'Remote, India',
#     'company': 'Tata Consultancy Services',
#   }
# ]

      

@app.route("/")
def hello_bytehire():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
