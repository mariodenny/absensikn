from werkzeug.security import check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn


def login_user(email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT u.id, u.name, u.password, r.code AS role
        FROM users u
        JOIN user_roles ur ON u.id = ur.user_id
        JOIN roles r ON ur.role_id = r.id
        WHERE u.email = %s
    """
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and check_password_hash(user['password'], password):
        return user
    return None

def register():
    return "hey this features still on my head and i think stil dont need it, wait ya!"
