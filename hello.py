from flask import Flask
from flask import render_template
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

app = Flask(__name__)

cluster = Cluster(['10.1.1.11', '10.1.1.12', '10.1.1.13',
  '10.2.1.11', '10.2.1.12', '10.2.1.13'],
  load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='1'))

session = cluster.connect('azuredcs')

@app.route("/")
def index():
  rows = session.execute('SELECT * FROM test')
  return render_template('index.html', rows=rows)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
