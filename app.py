##################
# Import Dependencies
from flask import Flask, render_template

################
# Flask Set-Up
################
app = Flask(__name__, static_url_path='/static/js')


@app.route("/app.js")
def index():
    """Return the homepage."""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)