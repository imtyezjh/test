
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello()
    return "welcome to our cloud provider"
    
    
    if__name=="__main__":
        app.run(host="0.0.0.0",debug=True)
