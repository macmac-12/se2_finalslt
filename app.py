from flask import Flask
app = Flask(__name__) 

@app.route("/") 
def home(): 
    return "Hello, CI/CD! I am Macmac! Your Lingkod from BSCS3A"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)