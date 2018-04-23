from flask import Flask , render_template
app = Flask(__name__)

@app.route('/users/')
def users():
	names=['simon', 'thomas','lee','jamie','sylvester']
	return render_template('loop.html',names=names)
if __name__=="__main__":
	app.run(debug=True)