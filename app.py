# -------- Flask Hello World -------- #

from flask import Flask

# Create the application object
app = Flask(__name__)

# Error handling
app.config["DEBUG"] = True

# Use the decorator pattern to
# link the view function t oa url
@app.route("/")
@app.route("/hello")

# Define the view using a function, wchich returns a string

def hello_world():
    return "Hello World!????"

# Dynamic route
@app.route("/test")
@app.route("/test/<search_query>")

def search(search_query="hi"):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return f"{value} + 1 = {value +1} correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return f"{value} + 1 = {value +1} correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return value

# Dynamic route witch explicit statuscodes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return f"Hello {name}", 200
    else:
        return "Not Found", 404
if __name__ == "__main__":
    app.run()
