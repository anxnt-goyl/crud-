

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage (No Database)
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

# CREATE
@app.route("/add", methods=["POST"])
def add():

    title = request.form["title"]
    description = request.form["description"]

    tasks.append({
        "title": title,
        "description": description,
        "status": "Pending"
    })

    return redirect("/")


# UPDATE PAGE
@app.route("/edit/<int:index>")
def edit(index):
    return render_template("edit.html", task=tasks[index], index=index)


# UPDATE
@app.route("/update/<int:index>", methods=["POST"])
def update(index):

    tasks[index]["title"] = request.form["title"]
    tasks[index]["description"] = request.form["description"]
    tasks[index]["status"] = request.form["status"]

    return redirect("/")


# DELETE
@app.route("/delete/<int:index>")
def delete(index):

    tasks.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)