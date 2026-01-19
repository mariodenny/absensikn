from flask_bcrypt import Bcrypt
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

bcrypt = Bcrypt()  # bisa juga di-init di app.py dan import sini

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

    if user:
        # gunakan bcrypt untuk verify
        if bcrypt.check_password_hash(user['password'], password):
            return user

    return None

def register_user(name, email, password, role_code):
    """contoh simple insert user baru dengan bcrypt"""
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = get_db_connection()
    cursor = conn.cursor()
    # insert user
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                   (name, email, hashed_pw))
    user_id = cursor.lastrowid

    # ambil role id
    cursor.execute("SELECT id FROM roles WHERE code = %s", (role_code,))
    role = cursor.fetchone()
    if role:
        cursor.execute("INSERT INTO user_roles (user_id, role_id) VALUES (%s, %s)",
                       (user_id, role[0]))
    
    conn.commit()
    cursor.close()
    conn.close()
    return user_id

