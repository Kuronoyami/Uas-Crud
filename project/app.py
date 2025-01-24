from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data dummy (sebagai pengganti database)
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# Halaman utama (Read)
@app.route("/")
def index():
    return render_template("index.html", data=data)

# Halaman untuk menambah data (Create)
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        new_id = len(data) + 1
        name = request.form["name"]
        data.append({"id": new_id, "name": name})
        return redirect(url_for("index"))
    return render_template("create.html")

# Halaman untuk mengubah data (Update)
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    item = next((item for item in data if item["id"] == id), None)
    if not item:
        return "Item not found", 404
    if request.method == "POST":
        item["name"] = request.form["name"]
        return redirect(url_for("index"))
    return render_template("update.html", item=item)

# Menghapus data (Delete)
@app.route("/delete/<int:id>")
def delete(id):
    global data
    data = [item for item in data if item["id"] != id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
