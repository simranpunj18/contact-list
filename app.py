from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def Contacts():
    return "<h1>Contact list</h1>"


@app.route("/get-names")
def GetData(): 
    return jsonify({"Name1":"Simran":"Name2": "Sanay": "Name3:":"Shivali": "Name4": "Raviv"})


app.run()