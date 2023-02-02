from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return "Backend Home"

@app.route('/app')
def blog():
  return "Hello, from Backend App!"

if __name__ == 'main':
  app.run()