from flask import Flask, render_template, g, abort, request
from main import main, Allocate
from input import load
import sqlite3
import pickle

DATABASE = 'inputdb.sqlite'
app = Flask(__name__)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	db.row_factory = sqlite3.Row
	return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()


@app.route('/')
def home():
	return 'Hello'

@app.route('/allocate')
def allocate():
	return render_template('allocate.html')

@app.route('/do_allocation')
def do_allocation():
	text = request.args.get('jsdata')
	if text=='init':
		sessions = Allocate()
		with open('temp', 'wb') as f:
			pickle.dump((sessions, 0), f)
	elif text=='comman':
		with open('temp', 'rb+') as f:
			(sessions, _) = pickle.load(f)
			sessions.allocate_comman()
			f.seek(0)
			pickle.dump((sessions, 0), f)
	elif text=='session':
		with open('temp', 'rb+') as f:
			(sessions, i) = pickle.load(f)
			sessions.allocate(i+1)
			f.seek(0)
			pickle.dump((sessions, i+1), f)
	else:
		return abort(404)
	return render_template('chart.html', sessions = sessions.sessions)

@app.route('/input')
def inp():
	return render_template('input.html', fac_list = [fac[0:] for fac in query_db('select * from ece')])

@app.route('/allocate_all')
def allocate_all():
	sessions = main()
	return render_template('allocate_all.html', sessions=sessions.sessions)

@app.route('/admin')
def admin():
	return 'Admin page'

@app.route("/details")
def details():
	fac_list = load()
	return render_template('details.html', fac_list=fac_list)

if __name__=='__main__':
	app.run(debug=True)
