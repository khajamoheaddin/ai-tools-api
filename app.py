<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "API Running!"

if __name__ == '__main__':
=======
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "API Running!"

if __name__ == '__main__':
>>>>>>> d8baaffdd5c29b368f86f61d359253715c4c636d
    app.run(debug=True)