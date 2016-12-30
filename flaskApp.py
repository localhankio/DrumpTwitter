from flask import Flask
import drump_bg as drump
app = Flask(__name__)

@app.route("/")
def hello():
	print()
	tweetArr = drump.doEverything()

	return "Hello World!\n Tweet From Trump: " + tweetArr[0]


if __name__ == "__main__":
	app.run()