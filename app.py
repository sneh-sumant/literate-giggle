from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return "HomePage"

@app.route('/app')
def blog():
  return "Hello, from App!"

if __name__ == 'main':
  app.run()