from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Welcome to the Raspberry Pi web application! HELLO Hello World!!!'