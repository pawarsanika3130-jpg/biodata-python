from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>My Biodata</h1>
    <h2>Sanika Pawar</h2>
    <p>AWS Cloud Engineer</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
