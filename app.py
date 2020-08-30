from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
import dns

load_dotenv()
URI = os.getenv('MONGO_URI')
app = Flask(__name__)

@app.route('/')
def search():
    
    return render_template('search.html')


if __name__ == '__main__':
    app.run()
