from flask import Flask , render_template , request 
from flask import Flask , render_template , request 
import requests
import json
import random
app = Flask(__name__)


@app.route("/")
def index():
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=" +
                            random.choice('abcdefghijklmnopqrstuvwxzy') +
                            "&maxResults=40&key=AIzaSyDtKGwk1aWRFQYwW3qVE7CxoaBfp5VhaYA")
    r1 = r.json()
    print(r1)
    return render_template("index.html",books=r1)

if __name__ == "__main__":
    app.run(debug=True)