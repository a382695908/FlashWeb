from app import app
from flask import render_template
from flask import request
from flask import jsonify
from forms import WhoisIPForm
import subprocess

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

@app.route('/network-tools/ip')
def network_tools_ip():
  ip = request.remote_addr
  return(jsonify(ip=ip))

@app.route('/network-tools/headers')
def network_tools_headers():
  headers = request.headers
  return(jsonify(**headers))

@app.route('/network-tools/whois', methods=['GET', 'POST'])
def network_tools_whois():
  whois_ip = None
  whois_domain = None
  jwhois_output = None

  whois_ip_form = WhoisIPForm()

  if whois_ip_form.validate_on_submit():
    ip = whois_ip_form.whois_ip.data
    whois_ip_form.whois_ip.data = ''
 
    p = subprocess.Popen(["/usr/bin/jwhois", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    jwhois_output = out.split('\n')    
 
  #pass form object as form parameter to render_template function
  return render_template('whois.html', 
                          whois_ip_form=whois_ip_form, 
                          jwhois_output=jwhois_output)
