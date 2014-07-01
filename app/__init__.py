from flask import Flask

# Create an application instance, a Flask object.
# All requests are passed to this object by webserver via WSGI protocol.
# __name__ (app) is passed to constructor so flask can work out root path to find resources
app = Flask(__name__)

#import ./view.py
from app import views

from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap(app)


##Shit below is to get Flask Debugtoolbar working
#TODO: tidy this up

#app.config is a dictionary to store all kinds of configuration variables
#really shouldn't store SECRET_KEY here, instead use env variable
app.config['SECRET_KEY'] = 'superhardtoguesstring'

app.debug = True
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

