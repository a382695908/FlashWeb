from app import app
from flask import render_template
from flask import request

'''
- The application instance needs to know what code to run for each URL requested.
- It keeps a mapping of URLs to Python functions, this is called a route.
- The easiest way to define a route is via app.route decorator exposed via application instance.
- This registers the decorated function as a route, decorators are a standard feature of the Python language.
'''

#app.route decorators register URLs to index function.
@app.route('/index.html')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/network-tools')
def network_tools():
  ip = request.remote_addr
  headers = request.headers
  return render_template('network-tools.html',
                          headers=headers,
                          ip=ip)
