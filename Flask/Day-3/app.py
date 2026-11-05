from flask import Flask

# Flask app instance
app = Flask(__name__)


# Routers creation
@app.route("/")  # Home route
def home():
    return "This is home"


@app.route("/students")  # Students route
def students():
    return "This is students page"


@app.route("/contact")  # Contacts route
def contact():
    return "This is contact page"


#  Main
if __name__ == "__main__":
    app.run(
        debug=True,
    )
