'''from flask import Flask
# import drump_bg as drump
application = Flask(__name__)

@application.route("/")
def hello():
	#tweetArr = drump.doEverything()

	#return "<p>Hello World!</p> <br> <p> Tweet From Trump: " + tweetArr[0] + "</p>"
	return "Hello World"

if __name__ == "__main__":
	application.run()
'''
from flask import Flask
import drump_bg as drump
application = Flask(__name__)
# print a nice greeting.
# def say_hello(username = "World"):
#     return '<h1>Hello There! Welcome to Drump Twitter</h1>\n'
@application.route("/")
def showTweet():
    twArr = drump.doEverything()
    # atw = tweetArr[0]
    return '''
        <h1>hyppthetical tweets:</h1>
        <ul>
        <li> %s </li> <li> %s </li> <li> %s </li> <li> %s </li> <li> %s </li> 
        </ul>
        ''' %(twArr[0], twArr[1], twArr[2], twArr[3], twArr[4])
# some bits of text for the page. \
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <h2><em>Hint</em>: This is a hypothetical tweet: %s</h2>\n''' 
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.


# add a rule for the index page.
#application.add_url_rule('/', 'index', (lambda: header_text +
#    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()