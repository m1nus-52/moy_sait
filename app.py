from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if name == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render сам задает порт
    app.run(host="0.0.0.0", port=port)