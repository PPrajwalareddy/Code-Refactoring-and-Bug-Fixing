from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return render_template("home.html", notes=notes)

@app.route('/add_note', methods=["POST"])
def add_note():
    note = request.form.get("note")
    notes.append(note)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
