from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# make folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    image_name="images.jpg"
    return render_template('index.html', image=image_name)

@app.route('/up')
def render_upload():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_image():

    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    return f"Image uploaded successfully: {file.filename}"

@app.route("/bye")
def bye():
    return "<p>Bye, Flask!</p>"

@app.route("/username/<name>")
def learn(name):
    return f"<h1>{name} is learning Flask!!</h1>"

@app.route("/<name>/<int:number>")
def learn_flask(name, number):
    return f"<h1>{name} is learning Flask!! And wakes up at {number} as well</h1>"


if __name__ == '__main__':
    app.run(debug=True)
