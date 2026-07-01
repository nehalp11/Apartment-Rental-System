from flask import Flask
from routes import routes

app = Flask(__name__)
app.secret_key = "your_super_secret_key"  # <- this is necessary

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
