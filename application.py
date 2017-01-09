from flask import Flask
from flask import render_template
import drump_bg as drump
application = Flask(__name__)
# print a nice greeting.
# def say_hello(username = "World"):
#     return '<h1>Hello There! Welcome to Drump Twitter</h1>\n'
@application.route("/")
def showTweet():
    twArr = drump.doEverything()
    # atw = tweetArr[0]
    return render_template("index.html", tweets=twArr)
    '''
        <h1>Hypothetical Trump Tweets:</h1>
        <ul>
        <li> %s </li> <li> %s </li> <li> %s </li> <li> %s </li> <li> %s </li> 
        </ul>
    '''
        
@application.route("/speeches/")
def showSpeech():
    spArr = drump.doEverything("./corpora/speeches.txt")
    return render_template("index.html", speeches=spArr)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()