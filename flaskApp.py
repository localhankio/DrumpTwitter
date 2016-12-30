from flask import Flask
import drump_bg as drump
app = Flask(__name__)

@app.route("/")
def hello():
	print()
	tweetArr = drump.doEverything()

	return "<p>Hello World!</p> <br> <p> Tweet From Trump: " + tweetArr[0] + "</p>"


if __name__ == "__main__":
	app.run()