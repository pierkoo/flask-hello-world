# -------- Flask Hello World -------- #

from flask import Flask

# Create the application object
app = Flask(__name__)

# Use the decorator pattern to
# link the view function t oa url
@app.route("/")
@app.route("/hello")

# Define the view using a function, wchich returns a string

def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
