from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required,IPAddress

#Each web form is a new class that inherits from flask.ext.wtf.Form
#Each class defines a list of fields in the form, each represented by an object.

class WhoisIPForm(Form):
  whois_ip = StringField('IP to whois:', validators=[IPAddress(),Required()])
  submit = SubmitField('submit')

class WhoisDomainForm(Form):
  whois_domain = StringField('Domain to whois:', validators=[Required()])
  submit = SubmitField('submit')
