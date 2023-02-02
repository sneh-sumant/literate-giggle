from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return "FrontendHome"

@app.route('/app')
def blog():
  return "Hello, from Frontend App!"

if __name__ == 'main':
  app.run()