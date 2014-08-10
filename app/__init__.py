from flask import Flask

# Create an application instance, a Flask object.
# All requests are passed to this object by webserver via WSGI protocol.
# __name__ (app) is passed to constructor so flask can work out root path to find resources
app = Flask(__name__,instance_relative_config=True)

#import ./view.py
from app import views

from flask.ext.bootstrap import Bootstrap
#to prevent inserting CDN hosted bootstrap files, PITA when I'm coding on train with no WiFi.
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


##Shit below is to get Flask Debugtoolbar working
#TODO: tidy this up

#app.config is a dictionary to store all kinds of configuration variables
#really shouldn't store SECRET_KEY here, instead use env variable
app.config['SECRET_KEY'] = 'superhardtoguesstring'

app.debug = True
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

##Configuration Stuff:

# Load the default configuration
#app.config.from_pyfile('default.py')
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')
