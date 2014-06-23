import socket
from flask import Flask
from flask import render_template, redirect, url_for, request
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

app = Flask(__name__)

cluster = Cluster(['10.1.1.11', '10.1.1.12', '10.1.1.13',
  '10.2.1.11', '10.2.1.12', '10.2.1.13'],
  load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='1'))

session = cluster.connect('azuredcs')

hostname = socket.gethostname()

@app.route("/")
def index():
  rows = session.execute('SELECT * FROM test')
  return render_template('index.html', rows=rows, hostname=hostname)

@app.route("/insert", methods=['POST'])
def insert():
  pk = request.form['pk']
  t = request.form['t']
  s = request.form['s']
  v = request.form['v']
  session.execute('INSERT INTO test (pk, t, s, v) VALUES (%s, %s, %s, %s)', (int(pk), int(t), s, v))
  return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host='0.0.0.0')
