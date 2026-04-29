from flask import Flask
app = Flask(__name__) 

@app.route("/") 
def home(): 
    return "Hello, CI/CD! I am Macmac! Your Lingkod from BSCS3A"
