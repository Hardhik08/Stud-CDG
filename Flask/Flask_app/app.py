from flask import Flask

# Flask app instance
app = Flask(__name__)

data = {
    "1": {"name": "Hardhik", "section": "PFS-061", "marks": 45},
    "2": {"name": "Rishi", "section": "PFS-061", "marks": 46},
    "3": {"name": "Vamshi", "section": "PFS-061", "marks": 47},
    "4": {"name": "Shyam", "section": "PFS-061", "marks": 44},
    "5": {"name": "Anil", "section": "PFS-061", "marks": 45},
    "6": {"name": "Meher", "section": "PFS-061", "marks": 46},
    "7": {"name": "Sunil", "section": "PFS-061", "marks": 46},
}


# Routers creation
@app.route("/")  # Home route
def home():
    return "This is home"


@app.route("/students")  # Students route
def students():
    return data


@app.route("/students/1")
def student1():
    return data["1"]


@app.route("/students/<int:id>")
def get_sdata(id):
    if id in data:
        return data[id]
    else:
        return f"ID: {id} not present in databse, check again!"


@app.route("/students/marks/<int:m>")
def get_smarks(m):
    result = {}
    for i in data:
        if data[i]["marks"] == m:
            result[i] = data[i]

    return result if result else "Marks not found"


@app.route("/name/<n>")
def get_name(n):
    result = {}
    for i in data:
        if n in data[i]["name"]:
            result[i] = data[i]
    return result if result else "Name not found"


@app.route("/contact")  # Contacts route
def contact():
    return "This is contact page"


#  Main
if __name__ == "__main__":
    app.run(
        debug=True,
    )
