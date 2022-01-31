from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    return "<p>TODO: Return a word here!</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
