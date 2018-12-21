from flask import Flask, render_template
from modles import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)