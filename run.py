#!venv/bin/python
from app import app

#only run development server if script invoked directly
if __name__ == '__main__':
  #enable debugger and automatic reload
  app.run(debug = True)
