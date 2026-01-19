from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from datetime import datetime
from config import Config
import os
# Blueprint lists
from auth.routes import auth_bp
from admin.routes import admin_bp
from student_advisor.route import student_advisor_bp

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

print("DB Host:", app.config['DB_HOST'])
print("Debug mode:", app.config['DEBUG'])

# Blueprint for each logic
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(student_advisor_bp)

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