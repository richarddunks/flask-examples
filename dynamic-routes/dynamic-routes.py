from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    if name == None:
        name = "Robot"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
