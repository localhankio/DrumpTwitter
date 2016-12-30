from flask import Flask
import trumpTest_bigram
app = Flask(__name__)

@app.route("/")
def hello():
	print()
	#print(trump).
	return "Hello World!" + trumpTest_bigram.tryme()


if __name__ == "__main__":
	app.run()