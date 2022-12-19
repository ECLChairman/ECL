from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def test():
	return render_template("ECL.html")
app.debug = True
app.run(host="这里",port=8006)