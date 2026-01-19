from flask import Flask, render_template
from datetime import datetime
from config import Config
# Blueprint lists
from auth.routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
print("DB Host:", app.config['DB_HOST'])
print("Debug mode:", app.config['DEBUG'])

# Blueprint for each logic
app.register_blueprint(auth_bp)

@app.context_processor
def get_year():
    return{
        "year" : datetime.now().year
    }

@app.route("/")
def index():
    return render_template("public/home.html")

@app.route("/about")
def about():
    return render_template("public/about.html")


if __name__ == '__main__':
    app.run(debug=True,port=5050)