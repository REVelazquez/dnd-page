from flask import Flask, jsonify
# from classes import get_classes
app= Flask(__name__)

@app.route('/')
def hello():
    return 'Hola, este es mi servidor para DnD!'
if __name__== '__main__':
    app.run(debug=True)
