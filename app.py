from flask import Flask, render_template, jsonify
from database import get_jobs_db

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$150,000'
}]


@app.route("/")
def list_jobs():
  jobs = get_jobs_db()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs_json():
  jobs = get_jobs_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
