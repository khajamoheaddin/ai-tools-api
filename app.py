from flask import Flask
from grammar_checker import grammar_checker_bp  # Import the Blueprint

app = Flask(__name__)

# Register the grammar_checker Blueprint with a URL prefix
app.register_blueprint(grammar_checker_bp, url_prefix="/grammar")

@app.route('/')
def home():
    return "API Running!"

if __name__ == '__main__':
    app.run(debug=True)